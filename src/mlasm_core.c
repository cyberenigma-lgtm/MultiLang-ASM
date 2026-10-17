/* ============================================================================ */
/* MULTILANG-ASM NATIVE CORE: 100% Standalone ANSI C99 Preprocessor & Assembler */
/* Official Multilingual Assembly Layer of UPL (Universal Polyglot Layer)       */
/* Zero External Dependencies - 0% Python Runtime - Full 57 Language Parity     */
/* ============================================================================ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "masm_tables.h"

#define MLASM_VERSION "1.0.0"
#define MAX_LINE_LEN 4096
#define MAX_TOKEN_LEN 256
#define MAX_MACROS 512

/* Macro table entry */
typedef struct {
    char key[MAX_TOKEN_LEN];
    char val[MAX_TOKEN_LEN];
} MasmMacro;

typedef struct {
    MasmMacro items[MAX_MACROS];
    size_t count;
} MasmMacroTable;

/* Options for transpiler */
typedef struct {
    bool reverse;      /* Translate NASM -> Native language */
    bool verbose;      /* Print detailed processing info */
    bool direct_build; /* Call NASM and GCC to link executable */
} MasmOptions;

/* Case-insensitive string comparison (ASCII) */
static int masm_strcasecmp(const char *s1, const char *s2) {
    while (*s1 && *s2) {
        int c1 = tolower((unsigned char)*s1);
        int c2 = tolower((unsigned char)*s2);
        if (c1 != c2) return c1 - c2;
        s1++;
        s2++;
    }
    return tolower((unsigned char)*s1) - tolower((unsigned char)*s2);
}

/* Case-insensitive string comparison with length limit */
static int masm_strncasecmp(const char *s1, const char *s2, size_t n) {
    for (size_t i = 0; i < n; ++i) {
        if (!s1[i] || !s2[i]) return tolower((unsigned char)s1[i]) - tolower((unsigned char)s2[i]);
        int c1 = tolower((unsigned char)s1[i]);
        int c2 = tolower((unsigned char)s2[i]);
        if (c1 != c2) return c1 - c2;
    }
    return 0;
}

/* Find language by ISO code (case-insensitive) */
static const MasmLanguage* find_language(const char *code) {
    if (!code) return NULL;
    for (size_t i = 0; i < MASM_LANGUAGE_COUNT; ++i) {
        if (masm_strcasecmp(MASM_ALL_LANGUAGES[i].code, code) == 0) {
            return &MASM_ALL_LANGUAGES[i];
        }
    }
    return NULL;
}

/* Convert ASCII string to lowercase in-place */
static void str_tolower_ascii(char *str) {
    for (size_t i = 0; str[i]; ++i) {
        /* Only convert single-byte ASCII characters to preserve UTF-8 sequences */
        if ((unsigned char)str[i] < 128) {
            str[i] = (char)tolower((unsigned char)str[i]);
        }
    }
}

/* Translate native token to standard NASM mnemonic */
static const char* translate_mnemonic(const MasmLanguage *lang, const char *token) {
    if (!lang || !token) return token;

    for (size_t i = 0; i < lang->count; ++i) {
        if (strcmp(lang->keywords[i].native_kw, token) == 0) {
            return lang->keywords[i].nasm_mnemonic;
        }
    }
    return token; /* Passthrough if not found */
}

/* Reverse translate standard NASM mnemonic to native language keyword */
static const char* reverse_mnemonic(const MasmLanguage *lang, const char *nasm_mnemonic) {
    if (!lang || !nasm_mnemonic) return nasm_mnemonic;

    for (size_t i = 0; i < lang->count; ++i) {
        if (strcmp(lang->keywords[i].nasm_mnemonic, nasm_mnemonic) == 0) {
            return lang->keywords[i].native_kw;
        }
    }
    return nasm_mnemonic;
}

/* Add macro to table */
static void add_macro(MasmMacroTable *table, const char *key, const char *val) {
    if (!table || !key || !val || table->count >= MAX_MACROS) return;
    snprintf(table->items[table->count].key, sizeof(table->items[table->count].key), "%s", key);
    snprintf(table->items[table->count].val, sizeof(table->items[table->count].val), "%s", val);
    table->count++;
}

/* Apply macro expansions on a line */
static void apply_macros(const MasmMacroTable *table, const char *src, char *dst, size_t dst_max) {
    if (!table || table->count == 0) {
        snprintf(dst, dst_max, "%s", src);
        return;
    }

    char current[MAX_LINE_LEN];
    snprintf(current, sizeof(current), "%s", src);

    for (size_t m = 0; m < table->count; ++m) {
        const char *key = table->items[m].key;
        const char *val = table->items[m].val;
        size_t klen = strlen(key);
        if (klen == 0) continue;

        char temp[MAX_LINE_LEN];
        temp[0] = '\0';
        size_t tlen = 0;

        const char *p = current;
        while (*p) {
            const char *hit = strstr(p, key);
            if (!hit) {
                /* Append rest */
                size_t rem = strlen(p);
                if (tlen + rem < sizeof(temp) - 1) {
                    strcat(temp, p);
                    tlen += rem;
                }
                break;
            }

            /* Copy prefix before hit */
            size_t prefix_len = (size_t)(hit - p);
            if (tlen + prefix_len < sizeof(temp) - 1) {
                strncat(temp, p, prefix_len);
                tlen += prefix_len;
            }

            /* Boundary check: ensure key is an isolated word/token */
            bool left_boundary = (hit == current || isspace((unsigned char)*(hit - 1)) || *(hit - 1) == ',' || *(hit - 1) == '[' || *(hit - 1) == '+');
            const char *after = hit + klen;
            bool right_boundary = (*after == '\0' || isspace((unsigned char)*after) || *after == ',' || *after == ']' || *after == '+' || *after == ';');

            if (left_boundary && right_boundary) {
                size_t vlen = strlen(val);
                if (tlen + vlen < sizeof(temp) - 1) {
                    strcat(temp, val);
                    tlen += vlen;
                }
            } else {
                if (tlen + klen < sizeof(temp) - 1) {
                    strncat(temp, hit, klen);
                    tlen += klen;
                }
            }

            p = hit + klen;
        }

        snprintf(current, sizeof(current), "%s", temp);
    }

    snprintf(dst, dst_max, "%s", current);
}

/* Translate a single line of MultiLang-ASM */
static void translate_line(const MasmLanguage *lang,
                           MasmMacroTable *macros,
                           const char *src_line,
                           char *out_line,
                           size_t out_max,
                           bool reverse_mode) {
    out_line[0] = '\0';
    if (!src_line) return;

    /* Extract leading whitespace / indentation */
    size_t indent_len = 0;
    while (src_line[indent_len] == ' ' || src_line[indent_len] == '\t') {
        indent_len++;
    }

    char indent[256];
    if (indent_len >= sizeof(indent)) indent_len = sizeof(indent) - 1;
    memcpy(indent, src_line, indent_len);
    indent[indent_len] = '\0';

    const char *content = src_line + indent_len;

    /* Check if comment line or empty */
    if (*content == ';' || *content == '\0' || *content == '\r' || *content == '\n') {
        snprintf(out_line, out_max, "%s", src_line);
        return;
    }

    /* Check for %define MACRO_NAME VALUE */
    if (masm_strncasecmp(content, "%define", 7) == 0 && isspace((unsigned char)content[7])) {
        const char *p = content + 7;
        while (*p && isspace((unsigned char)*p)) p++;
        char k[MAX_TOKEN_LEN] = "", v[MAX_TOKEN_LEN] = "";
        int scanned = sscanf(p, "%255s %255[^\r\n]", k, v);
        if (scanned >= 2 && macros) {
            add_macro(macros, k, v);
            /* Omit or emit as comment */
            snprintf(out_line, out_max, "%s; [MACRO DEFINED] %s = %s\n", indent, k, v);
            return;
        }
    }

    /* Apply macro expansions */
    char expanded[MAX_LINE_LEN];
    apply_macros(macros, content, expanded, sizeof(expanded));

    /* Separate instruction code from trailing comment */
    char code_part[MAX_LINE_LEN];
    char comment_part[MAX_LINE_LEN] = "";
    const char *semicolon = strchr(expanded, ';');

    if (semicolon) {
        size_t code_len = (size_t)(semicolon - expanded);
        if (code_len >= sizeof(code_part)) code_len = sizeof(code_part) - 1;
        memcpy(code_part, expanded, code_len);
        code_part[code_len] = '\0';
        snprintf(comment_part, sizeof(comment_part), "%s", semicolon);
    } else {
        snprintf(code_part, sizeof(code_part), "%s", expanded);
    }

    /* Extract first word (mnemonic / token) */
    char token[MAX_TOKEN_LEN] = "";
    const char *rest = "";
    size_t i = 0;
    while (code_part[i] && !isspace((unsigned char)code_part[i]) && i < sizeof(token) - 1) {
        token[i] = code_part[i];
        i++;
    }
    token[i] = '\0';
    rest = code_part + i;

    /* Check if label definition like "_start:" or "loop:" */
    size_t tok_len = strlen(token);
    if (tok_len > 0 && token[tok_len - 1] == ':') {
        snprintf(out_line, out_max, "%s%s%s", indent, code_part, comment_part);
        return;
    }

    /* Translate mnemonic */
    char lookup_tok[MAX_TOKEN_LEN];
    snprintf(lookup_tok, sizeof(lookup_tok), "%s", token);
    str_tolower_ascii(lookup_tok);

    const char *translated = NULL;
    if (reverse_mode) {
        translated = reverse_mnemonic(lang, lookup_tok);
    } else {
        translated = translate_mnemonic(lang, lookup_tok);
    }

    /* Clean trailing newlines from rest */
    char clean_rest[MAX_LINE_LEN];
    snprintf(clean_rest, sizeof(clean_rest), "%s", rest);
    size_t rlen = strlen(clean_rest);
    while (rlen > 0 && (clean_rest[rlen - 1] == '\r' || clean_rest[rlen - 1] == '\n')) {
        clean_rest[--rlen] = '\0';
    }

    /* Rebuild line */
    snprintf(out_line, out_max, "%s%s%s%s\n", indent, translated, clean_rest, comment_part);
}

/* Auto-detect language from source content */
static const MasmLanguage* detect_language_from_file(const char *filepath) {
    FILE *f = fopen(filepath, "r");
    if (!f) return NULL;

    size_t scores[MASM_LANGUAGE_COUNT];
    memset(scores, 0, sizeof(scores));

    char line[MAX_LINE_LEN];
    while (fgets(line, sizeof(line), f)) {
        /* Extract tokens */
        const char *p = line;
        while (*p) {
            while (*p && (isspace((unsigned char)*p) || *p == ',' || *p == ';' || *p == '[' || *p == ']')) {
                if (*p == ';') break; /* Ignore rest of line comment */
                p++;
            }
            if (!*p || *p == ';') break;

            char word[MAX_TOKEN_LEN];
            size_t wlen = 0;
            while (*p && !isspace((unsigned char)*p) && *p != ',' && *p != ';' && *p != '[' && *p != ']' && wlen < sizeof(word) - 1) {
                word[wlen++] = *p++;
            }
            word[wlen] = '\0';
            str_tolower_ascii(word);

            /* Check against all language tables */
            for (size_t lang_idx = 0; lang_idx < MASM_LANGUAGE_COUNT; ++lang_idx) {
                const MasmLanguage *l = &MASM_ALL_LANGUAGES[lang_idx];
                for (size_t k = 0; k < l->count; ++k) {
                    if (strcmp(l->keywords[k].native_kw, word) == 0) {
                        scores[lang_idx]++;
                        break;
                    }
                }
            }
        }
    }
    fclose(f);

    size_t max_score = 0;
    size_t best_idx = 0;
    for (size_t i = 0; i < MASM_LANGUAGE_COUNT; ++i) {
        if (scores[i] > max_score) {
            max_score = scores[i];
            best_idx = i;
        }
    }

    if (max_score > 0) {
        return &MASM_ALL_LANGUAGES[best_idx];
    }
    return NULL;
}

/* Transpile file */
static int transpile_file(const char *lang_code,
                          const char *input_path,
                          const char *output_path,
                          const MasmOptions *opts) {
    const MasmLanguage *lang = NULL;

    if (masm_strcasecmp(lang_code, "auto") == 0) {
        lang = detect_language_from_file(input_path);
        if (lang) {
            printf("[AUTO-DETECT] Idioma identificado con exito: [%s] %s\n", lang->code, lang->name);
        } else {
            printf("[AUTO-DETECT] Advertencia: No se detecto un idioma especifico. Usando 'es' (Espanol).\n");
            lang = find_language("es");
        }
    } else {
        lang = find_language(lang_code);
    }

    if (!lang) {
        fprintf(stderr, "[ERROR] Idioma no soportado: '%s'. Usa '--list-langs' para ver idiomas disponibles.\n", lang_code);
        return 1;
    }

    FILE *fin = fopen(input_path, "r");
    if (!fin) {
        fprintf(stderr, "[ERROR] No se pudo abrir archivo de entrada: %s\n", input_path);
        return 1;
    }

    FILE *fout = stdout;
    if (output_path) {
        fout = fopen(output_path, "w");
        if (!fout) {
            fprintf(stderr, "[ERROR] No se pudo crear archivo de salida: %s\n", output_path);
            fclose(fin);
            return 1;
        }
    }

    MasmMacroTable macros;
    macros.count = 0;

    char line_buf[MAX_LINE_LEN];
    char trans_buf[MAX_LINE_LEN * 2];
    size_t lines_processed = 0;

    while (fgets(line_buf, sizeof(line_buf), fin)) {
        translate_line(lang, &macros, line_buf, trans_buf, sizeof(trans_buf), opts ? opts->reverse : false);
        fputs(trans_buf, fout);
        lines_processed++;
    }

    fclose(fin);
    if (output_path && fout != stdout) {
        fclose(fout);
        printf("[OK] Transpilado con exito: %s -> %s\n", input_path, output_path);
        printf("     Idioma: [%s] %s | Lineas procesadas: %zu\n", lang->code, lang->name, lines_processed);
    }

    return 0;
}

static void list_all_languages(void) {
    printf("====================================================================\n");
    printf("  MULTILANG-ASM NATIVE: Registro de 150 Idiomas Soportados (ANSI C99)\n");
    printf("  Parte del Ecosistema UPL (Universal Polyglot Layer)               \n");
    printf("====================================================================\n");
    for (size_t i = 0; i < MASM_LANGUAGE_COUNT; ++i) {
        printf("  [%-6s] %-36s (%zu mnemónicos)\n",
               MASM_ALL_LANGUAGES[i].code,
               MASM_ALL_LANGUAGES[i].name,
               MASM_ALL_LANGUAGES[i].count);
    }
    printf("====================================================================\n");
    printf("  Total: %d idiomas universales compilados nativamente en C99\n", MASM_LANGUAGE_COUNT);
    printf("====================================================================\n");
}

static int run_internal_tests(void) {
    printf("====================================================================\n");
    printf("  SUITE DE PRUEBAS: MOTOR NATIVO MULTILANG-ASM (mlasm_core.c)       \n");
    printf("  Tecnologia Soberana UPL - Cero Dependencias Externas               \n");
    printf("====================================================================\n");

    const MasmLanguage *es = find_language("es");
    if (!es) { fprintf(stderr, "[FAIL] Idioma 'es' no encontrado\n"); return 1; }

    char out[MAX_LINE_LEN];
    MasmMacroTable test_macros;
    test_macros.count = 0;

    /* Test 1: Spanish basic MOV */
    translate_line(es, &test_macros, "    mover rax, 1\n", out, sizeof(out), false);
    if (!strstr(out, "mov rax, 1")) {
        fprintf(stderr, "[FAIL] Test 1 fallo: esperado 'mov rax, 1', obtenido: %s\n", out);
        return 1;
    }
    printf("  [PASS] 1. Mnemónico básico en español (mover -> mov)\n");

    /* Test 2: System call & comments */
    translate_line(es, &test_macros, "llamada_sistema ; invoke OS\n", out, sizeof(out), false);
    if (!strstr(out, "syscall") || !strstr(out, "; invoke OS")) {
        fprintf(stderr, "[FAIL] Test 2 fallo: %s\n", out);
        return 1;
    }
    printf("  [PASS] 2. Preservación de comentarios y llamadas al sistema\n");

    /* Test 3: Turkish Unicode Support */
    const MasmLanguage *tr = find_language("tr");
    if (!tr) { fprintf(stderr, "[FAIL] Idioma 'tr' no encontrado\n"); return 1; }
    translate_line(tr, &test_macros, "taşı eax, 10\n", out, sizeof(out), false);
    if (!strstr(out, "mov eax, 10")) {
        fprintf(stderr, "[FAIL] Test 3 fallo (tr): %s\n", out);
        return 1;
    }
    printf("  [PASS] 3. Mnemónicos Unicode en Turco (taşı -> mov)\n");

    /* Test 4: Chinese UTF-8 Support */
    const MasmLanguage *zh = find_language("zh");
    if (!zh) { fprintf(stderr, "[FAIL] Idioma 'zh' no encontrado\n"); return 1; }
    translate_line(zh, &test_macros, "    移動 rax, 60\n", out, sizeof(out), false);
    if (!strstr(out, "mov rax, 60")) {
        fprintf(stderr, "[FAIL] Test 4 fallo (zh): %s\n", out);
        return 1;
    }
    printf("  [PASS] 4. Mnemónicos CJK en Chino (移動 -> mov)\n");

    /* Test 5: Russian Cyrillic Support */
    const MasmLanguage *ru = find_language("ru");
    if (!ru) { fprintf(stderr, "[FAIL] Idioma 'ru' no encontrado\n"); return 1; }
    translate_line(ru, &test_macros, "    перенести rdx, 13\n", out, sizeof(out), false);
    if (!strstr(out, "mov rdx, 13")) {
        fprintf(stderr, "[FAIL] Test 5 fallo (ru): %s\n", out);
        return 1;
    }
    printf("  [PASS] 5. Mnemónicos en Cirílico Ruso (перенести -> mov)\n");

    /* Test 6: Passthrough for standard NASM */
    translate_line(es, &test_macros, "cpuid\n", out, sizeof(out), false);
    if (!strstr(out, "cpuid")) {
        fprintf(stderr, "[FAIL] Test 6 fallo passthrough: %s\n", out);
        return 1;
    }
    printf("  [PASS] 6. Passthrough nativo de instrucciones x86_64 estándar (cpuid)\n");

    /* Test 7: Label preservation */
    translate_line(es, &test_macros, "_start:\n", out, sizeof(out), false);
    if (!strstr(out, "_start:")) {
        fprintf(stderr, "[FAIL] Test 7 fallo etiqueta: %s\n", out);
        return 1;
    }
    printf("  [PASS] 7. Preservación intacta de etiquetas (_start:)\n");

    /* Test 8: Native Macro Support (%define) */
    translate_line(es, &test_macros, "%define BUFFER_SIZE 1024\n", out, sizeof(out), false);
    translate_line(es, &test_macros, "    mover rcx, BUFFER_SIZE\n", out, sizeof(out), false);
    if (!strstr(out, "mov rcx, 1024")) {
        fprintf(stderr, "[FAIL] Test 8 fallo macro: %s\n", out);
        return 1;
    }
    printf("  [PASS] 8. Preprocesador nativo de macros (%%define BUFFER_SIZE 1024)\n");

    /* Test 9: Reverse Mode (NASM -> Native) */
    translate_line(es, &test_macros, "    mov rax, 1\n", out, sizeof(out), true);
    if (!strstr(out, "mover rax, 1")) {
        fprintf(stderr, "[FAIL] Test 9 fallo reverse: %s\n", out);
        return 1;
    }
    printf("  [PASS] 9. Modo inverso reversible (mov -> mover en español)\n");

    printf("====================================================================\n");
    printf("  RESULTADO: 9/9 PRUEBAS DEL MOTOR NATIVO APROBADAS (0 FALLOS)      \n");
    printf("====================================================================\n");
    return 0;
}

static void print_usage(void) {
    printf("MultiLang-ASM v%s (Native C99 / UPL Systems Edition)\n", MLASM_VERSION);
    printf("Motor soberano de ensamblador políglota con soporte para 57 idiomas.\n\n");
    printf("Uso:\n");
    printf("  mlasm <idioma|auto> <archivo.masm> [-o <salida.asm>]\n");
    printf("  mlasm <idioma|auto> <archivo.masm> <salida.asm>\n");
    printf("  mlasm --reverse <idioma> <archivo.asm> -o <salida.masm>\n");
    printf("  mlasm --build <idioma|auto> <archivo.masm>  (Ensambla y enlaza directo a .exe)\n");
    printf("  mlasm --list-langs                         (Lista los 57 idiomas soportados)\n");
    printf("  mlasm --test                               (Ejecuta suite interna de pruebas)\n");
    printf("  mlasm --version                            (Muestra información de versión)\n");
}

int main(int argc, char **argv) {
    if (argc < 2) {
        print_usage();
        return 1;
    }

    if (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
        print_usage();
        return 0;
    }

    if (strcmp(argv[1], "--version") == 0 || strcmp(argv[1], "-v") == 0) {
        printf("MultiLang-ASM v%s (UPL Systems Standard - ANSI C99)\n", MLASM_VERSION);
        printf("0%% Python - Cero dependencias externas - 57 Idiomas soportados\n");
        return 0;
    }

    if (strcmp(argv[1], "--list-langs") == 0 || strcmp(argv[1], "-l") == 0) {
        list_all_languages();
        return 0;
    }

    if (strcmp(argv[1], "--test") == 0 || strcmp(argv[1], "-t") == 0) {
        return run_internal_tests();
    }

    /* Build command: mlasm --build <lang> <file.masm> */
    if (strcmp(argv[1], "--build") == 0) {
        if (argc < 4) {
            fprintf(stderr, "[ERROR] Uso: mlasm --build <idioma> <archivo.masm>\n");
            return 1;
        }
        const char *lang = argv[2];
        const char *src = argv[3];
        size_t slen = strlen(src);
        if (slen < 5 || strcmp(src + slen - 5, ".masm") != 0) {
            fprintf(stderr, "[ERROR] El archivo debe tener extension .masm\n");
            return 1;
        }

        char asm_path[512], obj_path[512], exe_path[512];
        snprintf(asm_path, sizeof(asm_path), "%.*s.asm", (int)(slen - 5), src);
        snprintf(obj_path, sizeof(obj_path), "%.*s.o", (int)(slen - 5), src);
        snprintf(exe_path, sizeof(exe_path), "%.*s.exe", (int)(slen - 5), src);

        MasmOptions opts = { .reverse = false, .verbose = true, .direct_build = true };

        printf("[1/3] Traduciendo %s (%s) -> %s...\n", src, lang, asm_path);
        if (transpile_file(lang, src, asm_path, &opts) != 0) return 1;

        printf("[2/3] Ensamblando con NASM (win64)...\n");
        char cmd_nasm[2048];
        snprintf(cmd_nasm, sizeof(cmd_nasm), "nasm -f win64 \"%s\" -o \"%s\"", asm_path, obj_path);
        if (system(cmd_nasm) != 0) {
            fprintf(stderr, "[ERROR] Fallo en NASM al compilar %s\n", asm_path);
            return 1;
        }

        printf("[3/3] Enlazando con GCC...\n");
        char cmd_gcc[2048];
        snprintf(cmd_gcc, sizeof(cmd_gcc), "gcc \"%s\" -o \"%s\" -nostartfiles", obj_path, exe_path);
        if (system(cmd_gcc) != 0) {
            fprintf(stderr, "[ERROR] Fallo en GCC al enlazar %s\n", obj_path);
            return 1;
        }

        printf("[OK] Binario ejecutable generado con exito: %s\n", exe_path);
        return 0;
    }

    /* Reverse mode: mlasm --reverse <lang> <input.asm> -o <output.masm> */
    MasmOptions opts = { .reverse = false, .verbose = false, .direct_build = false };
    int arg_offset = 1;
    if (strcmp(argv[1], "--reverse") == 0 || strcmp(argv[1], "-r") == 0) {
        opts.reverse = true;
        arg_offset = 2;
    }

    if (arg_offset >= argc) {
        print_usage();
        return 1;
    }

    const char *lang = argv[arg_offset++];
    const char *input = NULL;
    const char *output = NULL;

    while (arg_offset < argc) {
        if (strcmp(argv[arg_offset], "-o") == 0 && arg_offset + 1 < argc) {
            output = argv[++arg_offset];
        } else if (!input && argv[arg_offset][0] != '-') {
            input = argv[arg_offset];
        } else if (!output && argv[arg_offset][0] != '-') {
            output = argv[arg_offset];
        }
        arg_offset++;
    }

    if (!input) {
        fprintf(stderr, "[ERROR] No se especifico archivo de entrada.\n");
        return 1;
    }

    return transpile_file(lang, input, output, &opts);
}
