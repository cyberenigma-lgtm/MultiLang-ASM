# MultiLang-ASM: Manual de Instrucciones [BG]

**Idioma:** Bulgarian / Български (`bg`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ако_равно` | `je` |
| `ако_различно` | `jne` |
| `върни` | `ret` |
| `добави` | `add` |
| `и` | `and` |
| `извади` | `sub` |
| `извади_стек` | `pop` |
| `извикай` | `call` |
| `изключващо` | `xor` |
| `или` | `or` |
| `намали` | `dec` |
| `не` | `not` |
| `нищо` | `nop` |
| `постави` | `push` |
| `прекъсване` | `int` |
| `премести` | `mov` |
| `раздели` | `div` |
| `размени` | `xchg` |
| `системно_повикване` | `syscall` |
| `скочи` | `jmp` |
| `спри` | `hlt` |
| `сравни` | `cmp` |
| `тествай` | `test` |
| `увеличи` | `inc` |
| `умножи` | `mul` |
| `цикъл` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Bulgarian / Български (bg)
section .text
global _start

_start:
    премести rax, 1
    премести rdi, 1
    премести rsi, msg
    премести rdx, 13
    системно_повикване

    премести rax, 60
    премести rdi, 0
    системно_повикване

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm bg programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build bg programa.masm
```
