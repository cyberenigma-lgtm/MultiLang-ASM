# MultiLang-ASM: Manual de Instrucciones [WO]

**Idioma:** Wolof (`wo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ak` | `and` |
| `baaraat` | `mul` |
| `boppam` | `xor` |
| `dagg` | `int` |
| `dank` | `loop` |
| `dara` | `nop` |
| `dellu` | `ret` |
| `du` | `not` |
| `dugal` | `push` |
| `génne` | `pop` |
| `mengale` | `cmp` |
| `natt` | `test` |
| `séddale` | `div` |
| `taxaw` | `hlt` |
| `tëb` | `jmp` |
| `walla` | `or` |
| `woote` | `call` |
| `woote_noste` | `syscall` |
| `wàññi` | `sub` |
| `yokk` | `add` |
| `yóbbu` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Wolof (wo)
section .text
global _start

_start:
    yóbbu rax, 1
    yóbbu rdi, 1
    yóbbu rsi, msg
    yóbbu rdx, 13
    woote_noste

    yóbbu rax, 60
    yóbbu rdi, 0
    woote_noste

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm wo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build wo programa.masm
```
