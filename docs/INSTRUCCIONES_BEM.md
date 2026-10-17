# MultiLang-ASM: Manual de Instrucciones [BEM]

**Idioma:** Bemba / ChiBemba (`bem`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `akeniko` | `div` |
| `awe` | `not` |
| `bikeni` | `push` |
| `bweleni` | `ret` |
| `cilauke` | `jmp` |
| `esheni` | `test` |
| `fumyapo` | `sub` |
| `fumyeni` | `pop` |
| `fushisheni` | `mul` |
| `ibela` | `xor` |
| `iminina` | `hlt` |
| `ita_system` | `syscall` |
| `iteni` | `call` |
| `kushinguluka` | `loop` |
| `linganyeni` | `cmp` |
| `lundapo` | `add` |
| `na` | `and` |
| `nangu` | `or` |
| `selesha` | `mov` |
| `tapali_kantu` | `nop` |
| `ukulesha` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Bemba / ChiBemba (bem)
section .text
global _start

_start:
    selesha rax, 1
    selesha rdi, 1
    selesha rsi, msg
    selesha rdx, 13
    ita_system

    selesha rax, 60
    selesha rdi, 0
    ita_system

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm bem programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build bem programa.masm
```
