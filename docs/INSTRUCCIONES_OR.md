# MultiLang-ASM: Manual de Instrucciones [OR]

**Idioma:** Odia / ଓଡ଼ିଆ (`or`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ଅଟକନ୍ତୁ` | `hlt` |
| `ଏବଂ` | `and` |
| `କାଢ଼ନ୍ତୁ` | `pop` |
| `କିଛି_ନାହିଁ` | `nop` |
| `କିମ୍ବା` | `or` |
| `ଗୁଣନ` | `mul` |
| `ଘୁଞ୍ଚାଅ` | `mov` |
| `ଚକ୍ର` | `loop` |
| `ଡାକନ୍ତୁ` | `call` |
| `ଡେଇଁବା` | `jmp` |
| `ତୁଳନା` | `cmp` |
| `ନାହିଁ` | `not` |
| `ପରୀକ୍ଷା` | `test` |
| `ଫେଡ଼` | `sub` |
| `ଫେରସ୍ତ` | `ret` |
| `ବ୍ୟାଘାତ` | `int` |
| `ଯୋଡ଼` | `add` |
| `ରଖନ୍ତୁ` | `push` |
| `ସିଷ୍ଟମ_କଲ୍` | `syscall` |
| `ସ୍ୱତନ୍ତ୍ର` | `xor` |
| `ହରଣ` | `div` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Odia / ଓଡ଼ିଆ (or)
section .text
global _start

_start:
    ଘୁଞ୍ଚାଅ rax, 1
    ଘୁଞ୍ଚାଅ rdi, 1
    ଘୁଞ୍ଚାଅ rsi, msg
    ଘୁଞ୍ଚାଅ rdx, 13
    ସିଷ୍ଟମ_କଲ୍

    ଘୁଞ୍ଚାଅ rax, 60
    ଘୁଞ୍ଚାଅ rdi, 0
    ସିଷ୍ଟମ_କଲ୍

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm or programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build or programa.masm
```
