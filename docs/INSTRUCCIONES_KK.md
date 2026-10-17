# MultiLang-ASM: Manual de Instrucciones [KK]

**Idioma:** Kazakh / Қазақ тілі (`kk`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `азайту` | `sub` |
| `бөлу` | `div` |
| `емес` | `not` |
| `ерекше` | `xor` |
| `ештеңе` | `nop` |
| `жылжыту` | `mov` |
| `жүйелік_шақыру` | `syscall` |
| `және` | `and` |
| `кіргізу` | `push` |
| `көбейту` | `mul` |
| `немесе` | `or` |
| `салыстыру` | `cmp` |
| `секіру` | `jmp` |
| `тексеру` | `test` |
| `тоқтау` | `hlt` |
| `цикл` | `loop` |
| `шақыру` | `call` |
| `шығару` | `pop` |
| `қайтару` | `ret` |
| `қосу` | `add` |
| `үзіліс` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kazakh / Қазақ тілі (kk)
section .text
global _start

_start:
    жылжыту rax, 1
    жылжыту rdi, 1
    жылжыту rsi, msg
    жылжыту rdx, 13
    жүйелік_шақыру

    жылжыту rax, 60
    жылжыту rdi, 0
    жүйелік_шақыру

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm kk programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build kk programa.masm
```
