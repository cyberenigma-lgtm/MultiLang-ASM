# MultiLang-ASM: Manual de Instrucciones [KG]

**Idioma:** Kongo / Kikongo (`kg`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `binga` | `call` |
| `fwanisa` | `cmp` |
| `kabula` | `div` |
| `katula` | `sub` |
| `kima_ve` | `nop` |
| `kotesa` | `push` |
| `kudisa` | `mul` |
| `mbila_nkandikila` | `syscall` |
| `mpambula` | `xor` |
| `natisa` | `mov` |
| `solola` | `test` |
| `telama` | `hlt` |
| `tenda` | `int` |
| `tina` | `jmp` |
| `to` | `or` |
| `vaikisa` | `pop` |
| `ve` | `not` |
| `vutuka` | `ret` |
| `ye` | `and` |
| `yika` | `add` |
| `zietolo` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kongo / Kikongo (kg)
section .text
global _start

_start:
    natisa rax, 1
    natisa rdi, 1
    natisa rsi, msg
    natisa rdx, 13
    mbila_nkandikila

    natisa rax, 60
    natisa rdi, 0
    mbila_nkandikila

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm kg programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build kg programa.masm
```
