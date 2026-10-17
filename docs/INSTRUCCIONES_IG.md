# MultiLang-ASM: Manual de Instrucciones [IG]

**Idioma:** Igbo (`ig`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `abụọ_gaa_na_anọ` | `cdq` |
| `akaghị` | `loop` |
| `akaghị_ma_ọ_bụrụ_na_efu` | `loopz` |
| `belata_otu` | `dec` |
| `bubata_adirẹsi` | `lea` |
| `bubata_byte` | `lodsb` |
| `bugharịa` | `mov` |
| `bugharịa_byte` | `movsb` |
| `byte_gaa_na_okwu` | `cbw` |
| `chekwaa_byte` | `stosb` |
| `gbanwee` | `xchg` |
| `gbasaa_akara` | `movsx` |
| `gbasaa_efu` | `movzx` |
| `jụọ` | `neg` |
| `kewa` | `div` |
| `kpọọ` | `call` |
| `lọta` | `ret` |
| `ma_ọ_bụrụ_na_anaghị_nhata` | `jne` |
| `ma_ọ_bụrụ_na_efu` | `jz` |
| `ma_ọ_bụrụ_na_ka_ibu` | `jg` |
| `ma_ọ_bụrụ_na_ka_ntakị` | `jl` |
| `ma_ọ_bụrụ_na_nhata` | `je` |
| `maka` | `hlt` |
| `mali` | `jmp` |
| `meghachi_omume` | `rep` |
| `mụbaa` | `mul` |
| `mụbaa_otu` | `inc` |
| `ndabichi` | `int` |
| `nkpọ_usoro` | `syscall` |
| `nlọta_usoro` | `sysret` |
| `ntakịrị` | `nop` |
| `nwale` | `test` |
| `okwu_gaa_na_abụọ` | `cwd` |
| `tinye` | `add` |
| `tinye_n'ime` | `push` |
| `tinye_ọkọlọtọ` | `pushf` |
| `tụnyere` | `cmp` |
| `wepụ` | `sub` |
| `wepụ_n'ime` | `pop` |
| `wepụ_ọkọlọtọ` | `popf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Igbo (ig)
section .text
global _start

_start:
    bugharịa rax, 1
    bugharịa rdi, 1
    bugharịa rsi, msg
    bugharịa rdx, 13
    nkpọ_usoro

    bugharịa rax, 60
    bugharịa rdi, 0
    nkpọ_usoro

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ig programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ig programa.masm
```
