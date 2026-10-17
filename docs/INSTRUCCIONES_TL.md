# MultiLang-ASM: Manual de Instrucciones [TL]

**Idioma:** Tagalog / Filipino (`tl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `abala` | `int` |
| `balik_system` | `sysret` |
| `bumalik` | `ret` |
| `byte_sa_word` | `cbw` |
| `double_sa_quad` | `cdq` |
| `i-divide` | `div` |
| `i-load` | `lea` |
| `i-load_byte` | `lodsb` |
| `i-multiply` | `mul` |
| `i-negate` | `neg` |
| `i-save_byte` | `stosb` |
| `ibaba` | `dec` |
| `ibawas` | `sub` |
| `idagdag` | `add` |
| `ihambing` | `cmp` |
| `ikot` | `loop` |
| `ikot_kung_zero` | `loopz` |
| `ilipat` | `mov` |
| `ilipat_byte` | `movsb` |
| `itaas` | `inc` |
| `itawag` | `call` |
| `itigil` | `hlt` |
| `itulak` | `push` |
| `itulak_flag` | `pushf` |
| `kung_hindi_pareho` | `jne` |
| `kung_mas_malaki` | `jg` |
| `kung_mas_maliit` | `jl` |
| `kung_pareho` | `je` |
| `kung_zero` | `jz` |
| `kunin` | `pop` |
| `kunin_flag` | `popf` |
| `pagpalit` | `xchg` |
| `palawakin_sign` | `movsx` |
| `palawakin_zero` | `movzx` |
| `subukan` | `test` |
| `tawag_system` | `syscall` |
| `tumalon` | `jmp` |
| `ulitin` | `rep` |
| `wala` | `nop` |
| `word_sa_double` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tagalog / Filipino (tl)
section .text
global _start

_start:
    ilipat rax, 1
    ilipat rdi, 1
    ilipat rsi, msg
    ilipat rdx, 13
    tawag_system

    ilipat rax, 60
    ilipat rdi, 0
    tawag_system

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tl programa.masm
```
