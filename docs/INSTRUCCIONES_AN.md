# MultiLang-ASM: Manual de Instrucciones [AN]

**Idioma:** Aragonese / Aragonés (`an`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `adhibir` | `add` |
| `aturar` | `hlt` |
| `blincar` | `jmp` |
| `clamada_sistema` | `syscall` |
| `clamar` | `call` |
| `comparar` | `cmp` |
| `comprebar` | `test` |
| `corro` | `loop` |
| `cosa` | `nop` |
| `dividir` | `div` |
| `esclusivo` | `xor` |
| `ficar` | `push` |
| `interrupcion` | `int` |
| `mover` | `mov` |
| `multiplicar` | `mul` |
| `no` | `not` |
| `restar` | `sub` |
| `tornar` | `ret` |
| `trayer` | `pop` |
| `u` | `or` |
| `y` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Aragonese / Aragonés (an)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    clamada_sistema

    mover rax, 60
    mover rdi, 0
    clamada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm an programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build an programa.masm
```
