# MultiLang-ASM: Manual de Instrucciones [CY]

**Idioma:** Welsh / Cymraeg (`cy`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ac` | `and` |
| `anghynhwysol` | `xor` |
| `aros` | `hlt` |
| `cymharu` | `cmp` |
| `ddim` | `not` |
| `dim_byd` | `nop` |
| `dolen` | `loop` |
| `dychwelyd` | `ret` |
| `galw` | `call` |
| `galwad_system` | `syscall` |
| `gwthio` | `push` |
| `lluosi` | `mul` |
| `neidio` | `jmp` |
| `neu` | `or` |
| `profi` | `test` |
| `rhannu` | `div` |
| `symud` | `mov` |
| `torri_ar_draws` | `int` |
| `tynnu` | `sub` |
| `tynnu_allan` | `pop` |
| `ychwanegu` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Welsh / Cymraeg (cy)
section .text
global _start

_start:
    symud rax, 1
    symud rdi, 1
    symud rsi, msg
    symud rdx, 13
    galwad_system

    symud rax, 60
    symud rdi, 0
    galwad_system

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm cy programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build cy programa.masm
```
