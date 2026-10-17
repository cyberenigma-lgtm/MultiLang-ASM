# MultiLang-ASM: Manual de Instrucciones [WAR]

**Idioma:** Waray (`war`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `bahina` | `div` |
| `balhina` | `mov` |
| `balik` | `ret` |
| `damoa` | `mul` |
| `diri` | `not` |
| `dugangi` | `add` |
| `eksklusibo` | `xor` |
| `ibutong` | `pop` |
| `iduon` | `push` |
| `itanding` | `cmp` |
| `kuhai` | `sub` |
| `libot` | `loop` |
| `lukso` | `jmp` |
| `ngan` | `and` |
| `o` | `or` |
| `pahuway` | `hlt` |
| `tawag_han_sistema` | `syscall` |
| `tawaga` | `call` |
| `testingi` | `test` |
| `ulang` | `int` |
| `waray` | `nop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Waray (war)
section .text
global _start

_start:
    balhina rax, 1
    balhina rdi, 1
    balhina rsi, msg
    balhina rdx, 13
    tawag_han_sistema

    balhina rax, 60
    balhina rdi, 0
    tawag_han_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm war programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build war programa.masm
```
