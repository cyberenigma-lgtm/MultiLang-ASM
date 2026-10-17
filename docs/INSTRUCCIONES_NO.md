# MultiLang-ASM: Manual de Instrucciones [NO]

**Idioma:** Norwegian / Norsk (`no`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `avbrudd` | `int` |
| `byte_til_ord` | `cbw` |
| `divider` | `div` |
| `dobbel_til_quad` | `cdq` |
| `flytt` | `mov` |
| `flytt_byte` | `movsb` |
| `gjenta` | `rep` |
| `hent` | `pop` |
| `hent_flagg` | `popf` |
| `hopp` | `jmp` |
| `hvis_ikke_lik` | `jne` |
| `hvis_lik` | `je` |
| `hvis_mindre` | `jl` |
| `hvis_null` | `jz` |
| `hvis_større` | `jg` |
| `ingen` | `nop` |
| `kall` | `call` |
| `lagre_byte` | `stosb` |
| `last_byte` | `lodsb` |
| `last_effektiv` | `lea` |
| `legg_til` | `add` |
| `løkke` | `loop` |
| `løkke_hvis_null` | `loopz` |
| `minsk` | `dec` |
| `multipliser` | `mul` |
| `neger` | `neg` |
| `ord_til_dobbel` | `cwd` |
| `returner` | `ret` |
| `sammenlign` | `cmp` |
| `skyv` | `push` |
| `skyv_flagg` | `pushf` |
| `stopp` | `hlt` |
| `systemkall` | `syscall` |
| `systemretur` | `sysret` |
| `test` | `test` |
| `trekk_fra` | `sub` |
| `utvid_null` | `movzx` |
| `utvid_tegn` | `movsx` |
| `veksle` | `xchg` |
| `øk` | `inc` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Norwegian / Norsk (no)
section .text
global _start

_start:
    flytt rax, 1
    flytt rdi, 1
    flytt rsi, msg
    flytt rdx, 13
    systemkall

    flytt rax, 60
    flytt rdi, 0
    systemkall

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm no programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build no programa.masm
```
