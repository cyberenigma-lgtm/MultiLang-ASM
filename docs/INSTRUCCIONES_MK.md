# MultiLang-ASM: Manual de Instrucciones [MK]

**Idioma:** Macedonian / Македонски (`mk`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `врати` | `ret` |
| `и` | `and` |
| `извади` | `pop` |
| `или` | `or` |
| `исклучиво` | `xor` |
| `не` | `not` |
| `ништо` | `nop` |
| `одземи` | `sub` |
| `повикај` | `call` |
| `подели` | `div` |
| `помножи` | `mul` |
| `прекин` | `int` |
| `премести` | `mov` |
| `системски_повик` | `syscall` |
| `скокни` | `jmp` |
| `собери` | `add` |
| `сопри` | `hlt` |
| `спореди` | `cmp` |
| `тестирај` | `test` |
| `турни` | `push` |
| `јамка` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Macedonian / Македонски (mk)
section .text
global _start

_start:
    премести rax, 1
    премести rdi, 1
    премести rsi, msg
    премести rdx, 13
    системски_повик

    премести rax, 60
    премести rdi, 0
    системски_повик

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mk programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mk programa.masm
```
