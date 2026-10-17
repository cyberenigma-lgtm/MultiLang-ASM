# MultiLang-ASM: Manual de Instrucciones [IS]

**Idioma:** Icelandic / Íslenska (`is`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `baeta` | `add` |
| `bera_saman` | `cmp` |
| `deila` | `div` |
| `draga` | `sub` |
| `draga_ut` | `pop` |
| `eda` | `or` |
| `einka` | `xor` |
| `ekkert` | `nop` |
| `ekki` | `not` |
| `faera` | `mov` |
| `haetta` | `hlt` |
| `kalla` | `call` |
| `kerfiskall` | `syscall` |
| `lykkja` | `loop` |
| `marga` | `mul` |
| `og` | `and` |
| `profa` | `test` |
| `skila` | `ret` |
| `stoppa` | `jmp` |
| `truflun` | `int` |
| `yta` | `push` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Icelandic / Íslenska (is)
section .text
global _start

_start:
    faera rax, 1
    faera rdi, 1
    faera rsi, msg
    faera rdx, 13
    kerfiskall

    faera rax, 60
    faera rdi, 0
    kerfiskall

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm is programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build is programa.masm
```
