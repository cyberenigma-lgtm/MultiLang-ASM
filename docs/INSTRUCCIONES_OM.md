# MultiLang-ASM: Manual de Instrucciones [OM]

**Idioma:** Oromo / Afaan Oromoo (`om`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `adda` | `xor` |
| `baasi` | `pop` |
| `baay'isi` | `mul` |
| `deebi'i` | `ret` |
| `dhaabi` | `hlt` |
| `fi` | `and` |
| `galchi` | `push` |
| `gidduu_seensa` | `int` |
| `hir'isi` | `sub` |
| `homaa` | `nop` |
| `ida'i` | `add` |
| `marsoo` | `loop` |
| `miti` | `not` |
| `qodi` | `div` |
| `qori` | `test` |
| `sochoosi` | `mov` |
| `utaali` | `jmp` |
| `waami` | `call` |
| `waamicha_sirnaa` | `syscall` |
| `walbira_qabi` | `cmp` |
| `yookiin` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Oromo / Afaan Oromoo (om)
section .text
global _start

_start:
    sochoosi rax, 1
    sochoosi rdi, 1
    sochoosi rsi, msg
    sochoosi rdx, 13
    waamicha_sirnaa

    sochoosi rax, 60
    sochoosi rdi, 0
    waamicha_sirnaa

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm om programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build om programa.masm
```
