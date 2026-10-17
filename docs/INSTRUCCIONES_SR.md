# MultiLang-ASM: Manual de Instrucciones [SR]

**Idioma:** Serbian / Српски (`sr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ако_није` | `jne` |
| `ако_једнако` | `je` |
| `врати` | `ret` |
| `гурни` | `push` |
| `заустави` | `hlt` |
| `и` | `and` |
| `извуци` | `pop` |
| `или` | `or` |
| `искључиво` | `xor` |
| `не` | `not` |
| `ништа` | `nop` |
| `одузми` | `sub` |
| `петља` | `loop` |
| `повећај` | `inc` |
| `подели` | `div` |
| `позови` | `call` |
| `помножи` | `mul` |
| `прекид` | `int` |
| `премести` | `mov` |
| `размени` | `xchg` |
| `сабери` | `add` |
| `системски_позив` | `syscall` |
| `скочи` | `jmp` |
| `смањи` | `dec` |
| `тестирај` | `test` |
| `упореди` | `cmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Serbian / Српски (sr)
section .text
global _start

_start:
    премести rax, 1
    премести rdi, 1
    премести rsi, msg
    премести rdx, 13
    системски_позив

    премести rax, 60
    премести rdi, 0
    системски_позив

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sr programa.masm
```
