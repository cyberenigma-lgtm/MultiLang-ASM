# MultiLang-ASM: Manual de Instrucciones [MAY]

**Idioma:** Maya / Maaya T'aan (`may`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `byte_li'is` | `stosb` |
| `byte_palk'es` | `lodsb` |
| `byte_túuxt` | `movsb` |
| `byte_wordtech` | `cbw` |
| `ch'enb` | `dec` |
| `ch'íij` | `inc` |
| `chichan` | `jl` |
| `double_quadtech` | `cdq` |
| `flag_jok's` | `popf` |
| `flag_ts'áaj` | `pushf` |
| `je'el_bey` | `je` |
| `jet'` | `int` |
| `jok's` | `pop` |
| `k'ex` | `xchg` |
| `ka'a` | `rep` |
| `ket` | `cmp` |
| `ma'` | `neg` |
| `ma'_bey` | `jne` |
| `mixba'al` | `nop` |
| `mixba'al_bey` | `jz` |
| `mixba'al_jalk'es` | `movzx` |
| `mixba'al_nalkut` | `loopz` |
| `nalkut` | `loop` |
| `nojoch` | `jg` |
| `p'ul` | `hlt` |
| `palk'es` | `lea` |
| `pilis` | `test` |
| `si'it` | `jmp` |
| `suut` | `ret` |
| `suut_sistema` | `sysret` |
| `t'an` | `call` |
| `t'an_sistema` | `syscall` |
| `t'ox` | `div` |
| `ts'áaj` | `add` |
| `ts'áaj_ich` | `push` |
| `túul` | `sub` |
| `túuxt` | `mov` |
| `unancha_jalk'es` | `movsx` |
| `word_doubletech` | `cwd` |
| `ya'abkún` | `mul` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Maya / Maaya T'aan (may)
section .text
global _start

_start:
    túuxt rax, 1
    túuxt rdi, 1
    túuxt rsi, msg
    túuxt rdx, 13
    t'an_sistema

    túuxt rax, 60
    túuxt rdi, 0
    t'an_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm may programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build may programa.masm
```
