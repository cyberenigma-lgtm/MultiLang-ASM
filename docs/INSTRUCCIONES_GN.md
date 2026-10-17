# MultiLang-ASM: Manual de Instrucciones [GN]

**Idioma:** Guarani / Avañe'ẽ (`gn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `apu'a` | `loop` |
| `ha` | `and` |
| `ha'a` | `test` |
| `ha'eñomi` | `xor` |
| `henoi` | `call` |
| `henoi_sistema` | `syscall` |
| `jevy` | `ret` |
| `joko` | `int` |
| `mba'eve` | `nop` |
| `mbogue` | `sub` |
| `mbohasa` | `mov` |
| `mboheta` | `mul` |
| `mbojoapy` | `add` |
| `mbojoja` | `cmp` |
| `mbovo` | `div` |
| `moinge` | `push` |
| `nahániri` | `not` |
| `nohê` | `pop` |
| `po` | `jmp` |
| `pytu'u` | `hlt` |
| `térã` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Guarani / Avañe'ẽ (gn)
section .text
global _start

_start:
    mbohasa rax, 1
    mbohasa rdi, 1
    mbohasa rsi, msg
    mbohasa rdx, 13
    henoi_sistema

    mbohasa rax, 60
    mbohasa rdi, 0
    henoi_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm gn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build gn programa.masm
```
