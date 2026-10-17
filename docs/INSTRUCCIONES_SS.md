# MultiLang-ASM: Manual de Instrucciones [SS]

**Idioma:** Swati / SiSwati (`ss`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `bita` | `call` |
| `buyela` | `ret` |
| `engeta` | `add` |
| `faka` | `push` |
| `futhi` | `and` |
| `gcuma` | `jmp` |
| `gudluta` | `mov` |
| `hhayi` | `not` |
| `hlola` | `test` |
| `hlukanisa` | `div` |
| `khetekile` | `xor` |
| `khipha` | `pop` |
| `kubita_sisitemu` | `syscall` |
| `kuphazamisa` | `int` |
| `kute` | `nop` |
| `noma` | `or` |
| `phindzaphindza` | `mul` |
| `qhathanisa` | `cmp` |
| `siyingi` | `loop` |
| `susa` | `sub` |
| `yima` | `hlt` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Swati / SiSwati (ss)
section .text
global _start

_start:
    gudluta rax, 1
    gudluta rdi, 1
    gudluta rsi, msg
    gudluta rdx, 13
    kubita_sisitemu

    gudluta rax, 60
    gudluta rdi, 0
    kubita_sisitemu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ss programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ss programa.masm
```
