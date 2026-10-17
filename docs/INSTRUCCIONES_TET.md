# MultiLang-ASM: Manual de Instrucciones [TET]

**Idioma:** Tetum / Lia-Tetun (`tet`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aumenta` | `add` |
| `bolu` | `call` |
| `bolu_sistema` | `syscall` |
| `dudu` | `push` |
| `eskluzivu` | `xor` |
| `fahe` | `div` |
| `fila` | `ret` |
| `haksoit` | `jmp` |
| `hasai` | `sub` |
| `ho` | `and` |
| `interrupsaun` | `int` |
| `ka` | `or` |
| `koko` | `test` |
| `kompara` | `cmp` |
| `la_iha` | `nop` |
| `lae` | `not` |
| `muda` | `mov` |
| `multiplika` | `mul` |
| `para` | `hlt` |
| `puxa` | `pop` |
| `siklu` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tetum / Lia-Tetun (tet)
section .text
global _start

_start:
    muda rax, 1
    muda rdi, 1
    muda rsi, msg
    muda rdx, 13
    bolu_sistema

    muda rax, 60
    muda rdi, 0
    bolu_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tet programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tet programa.masm
```
