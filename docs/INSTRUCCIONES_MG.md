# MultiLang-ASM: Manual de Instrucciones [MG]

**Idioma:** Malagasy (`mg`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `afindrao` | `mov` |
| `ajanony` | `hlt` |
| `ampio` | `add` |
| `ampitahao` | `cmp` |
| `ampitomboy` | `mul` |
| `antsoy` | `call` |
| `atsofohy` | `push` |
| `avoahy` | `pop` |
| `esory` | `sub` |
| `fampiantsoana_rafitra` | `syscall` |
| `fanelingelenana` | `int` |
| `fihodinana` | `loop` |
| `manokana` | `xor` |
| `mitsambikina` | `jmp` |
| `miverena` | `ret` |
| `na` | `or` |
| `sy` | `and` |
| `tsia` | `not` |
| `tsy_misy` | `nop` |
| `zahao` | `test` |
| `zarazarao` | `div` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Malagasy (mg)
section .text
global _start

_start:
    afindrao rax, 1
    afindrao rdi, 1
    afindrao rsi, msg
    afindrao rdx, 13
    fampiantsoana_rafitra

    afindrao rax, 60
    afindrao rdi, 0
    fampiantsoana_rafitra

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mg programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mg programa.masm
```
