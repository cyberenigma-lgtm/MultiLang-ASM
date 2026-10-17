# MultiLang-ASM: Manual de Instrucciones [DA]

**Idioma:** Danish / Dansk (`da`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `afbrydelse` | `int` |
| `divider` | `div` |
| `eksklusiv` | `xor` |
| `eller` | `or` |
| `flyt` | `mov` |
| `gang` | `mul` |
| `hop` | `jmp` |
| `ikke` | `not` |
| `intet` | `nop` |
| `kald` | `call` |
| `lokke` | `loop` |
| `og` | `and` |
| `returner` | `ret` |
| `sammenlign` | `cmp` |
| `skub` | `push` |
| `stop` | `hlt` |
| `systemkald` | `syscall` |
| `test` | `test` |
| `tilfoj` | `add` |
| `traek` | `pop` |
| `traek_fra` | `sub` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Danish / Dansk (da)
section .text
global _start

_start:
    flyt rax, 1
    flyt rdi, 1
    flyt rsi, msg
    flyt rdx, 13
    systemkald

    flyt rax, 60
    flyt rdi, 0
    systemkald

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm da programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build da programa.masm
```
