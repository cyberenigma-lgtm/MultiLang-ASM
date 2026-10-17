# MultiLang-ASM: Manual de Instrucciones [NR]

**Idioma:** Southern Ndebele / isiNdebele (`nr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `awa` | `not` |
| `ayikho_into` | `nop` |
| `begodu` | `and` |
| `biza` | `call` |
| `buyela` | `ret` |
| `faka` | `push` |
| `hlukanisa` | `div` |
| `isondo` | `loop` |
| `jama` | `hlt` |
| `khethekileko` | `xor` |
| `khipha` | `pop` |
| `linga` | `test` |
| `mannisa` | `cmp` |
| `namkha` | `or` |
| `ngezelela` | `add` |
| `phindaphinda` | `mul` |
| `sitjhobo` | `int` |
| `stjhidla` | `jmp` |
| `susa` | `sub` |
| `tjhugulula` | `mov` |
| `ukubiza_isistimu` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Southern Ndebele / isiNdebele (nr)
section .text
global _start

_start:
    tjhugulula rax, 1
    tjhugulula rdi, 1
    tjhugulula rsi, msg
    tjhugulula rdx, 13
    ukubiza_isistimu

    tjhugulula rax, 60
    tjhugulula rdi, 0
    ukubiza_isistimu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm nr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build nr programa.masm
```
