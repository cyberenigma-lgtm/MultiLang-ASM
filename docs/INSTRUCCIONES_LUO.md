# MultiLang-ASM: Manual de Instrucciones [LUO]

**Idioma:** Luo / Dholuo (`luo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `chik` | `jmp` |
| `chung'` | `hlt` |
| `dog` | `ret` |
| `geng'o` | `int` |
| `gi` | `and` |
| `gol` | `mov` |
| `gol_kuom` | `sub` |
| `gol_oko` | `pop` |
| `kata` | `or` |
| `ket_iye` | `push` |
| `kikwette` | `loop` |
| `luong` | `call` |
| `luongo_mar_chenro` | `syscall` |
| `makende` | `xor` |
| `med` | `add` |
| `nyuol` | `mul` |
| `ok` | `not` |
| `onge_gimoro` | `nop` |
| `pim` | `cmp` |
| `pok` | `div` |
| `tem` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Luo / Dholuo (luo)
section .text
global _start

_start:
    gol rax, 1
    gol rdi, 1
    gol rsi, msg
    gol rdx, 13
    luongo_mar_chenro

    gol rax, 60
    gol rdi, 0
    luongo_mar_chenro

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm luo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build luo programa.masm
```
