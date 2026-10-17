# MultiLang-ASM: Manual de Instrucciones [AST]

**Idioma:** Asturian / Asturianu (`ast`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `amestar` | `add` |
| `blincar` | `jmp` |
| `ciclu` | `loop` |
| `comparar` | `cmp` |
| `dixebrar` | `div` |
| `esclusivu` | `xor` |
| `interrupcion` | `int` |
| `llamada_sistema` | `syscall` |
| `llamar` | `call` |
| `meter` | `push` |
| `mover` | `mov` |
| `multiplicar` | `mul` |
| `nada` | `nop` |
| `non` | `not` |
| `o` | `or` |
| `parar` | `hlt` |
| `prebar` | `test` |
| `restar` | `sub` |
| `sacar` | `pop` |
| `tornar` | `ret` |
| `y` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Asturian / Asturianu (ast)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    llamada_sistema

    mover rax, 60
    mover rdi, 0
    llamada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ast programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ast programa.masm
```
