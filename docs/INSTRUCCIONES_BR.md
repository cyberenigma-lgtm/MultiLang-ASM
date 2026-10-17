# MultiLang-ASM: Manual de Instrucciones [BR]

**Idioma:** Breton / Brezhoneg (`br`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `amprouiñ` | `test` |
| `bountañ` | `push` |
| `distreiñ` | `ret` |
| `fiñval` | `mov` |
| `galv_reizhiad` | `syscall` |
| `gervel` | `call` |
| `ha` | `and` |
| `herzel` | `hlt` |
| `ket` | `not` |
| `keñveriañ` | `cmp` |
| `lammat` | `jmp` |
| `lieskemmañ` | `mul` |
| `nemet` | `xor` |
| `netra` | `nop` |
| `ouzhpennañ` | `add` |
| `pe` | `or` |
| `rannañ` | `div` |
| `rodell` | `loop` |
| `tennañ` | `sub` |
| `tennañ_maez` | `pop` |
| `troc'h` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Breton / Brezhoneg (br)
section .text
global _start

_start:
    fiñval rax, 1
    fiñval rdi, 1
    fiñval rsi, msg
    fiñval rdx, 13
    galv_reizhiad

    fiñval rax, 60
    fiñval rdi, 0
    galv_reizhiad

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm br programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build br programa.masm
```
