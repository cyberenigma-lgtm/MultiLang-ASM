# MultiLang-ASM: Manual de Instrucciones [CEB]

**Idioma:** Cebuano / Sinugboanon (`ceb`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `abal` | `int` |
| `ambak` | `jmp` |
| `bahin` | `div` |
| `balhin` | `mov` |
| `balik` | `ret` |
| `dili` | `not` |
| `dugang` | `add` |
| `eksklusibo` | `xor` |
| `hunong` | `hlt` |
| `ibira` | `pop` |
| `iduso` | `push` |
| `kuha` | `sub` |
| `libot` | `loop` |
| `o` | `or` |
| `padaghan` | `mul` |
| `sulay` | `test` |
| `tandi` | `cmp` |
| `tawag` | `call` |
| `tawag_sa_sistema` | `syscall` |
| `ug` | `and` |
| `wala` | `nop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Cebuano / Sinugboanon (ceb)
section .text
global _start

_start:
    balhin rax, 1
    balhin rdi, 1
    balhin rsi, msg
    balhin rdx, 13
    tawag_sa_sistema

    balhin rax, 60
    balhin rdi, 0
    tawag_sa_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ceb programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ceb programa.masm
```
