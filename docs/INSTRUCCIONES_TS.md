# MultiLang-ASM: Manual de Instrucciones [TS]

**Idioma:** Tsonga / Xitsonga (`ts`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `a_ku_na_nchumu` | `nop` |
| `andzisa` | `mul` |
| `ava` | `div` |
| `e-e` | `not` |
| `engetela` | `add` |
| `fambisa` | `mov` |
| `hoxekile` | `xor` |
| `humesa` | `pop` |
| `kambela` | `test` |
| `kumbe` | `or` |
| `na` | `and` |
| `nghenisa` | `push` |
| `nsivelo` | `int` |
| `pimanisa` | `cmp` |
| `rhumbu` | `loop` |
| `susa` | `sub` |
| `tlula` | `jmp` |
| `vitana` | `call` |
| `vitano_ra_sisiteme` | `syscall` |
| `vuyela` | `ret` |
| `yima` | `hlt` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tsonga / Xitsonga (ts)
section .text
global _start

_start:
    fambisa rax, 1
    fambisa rdi, 1
    fambisa rsi, msg
    fambisa rdx, 13
    vitano_ra_sisiteme

    fambisa rax, 60
    fambisa rdi, 0
    vitano_ra_sisiteme

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ts programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ts programa.masm
```
