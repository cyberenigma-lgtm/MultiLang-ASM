# MultiLang-ASM: Manual de Instrucciones [AS]

**Idioma:** Assamese / অসমীয়া (`as`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `আৰু` | `and` |
| `উভতি_যাওক` | `ret` |
| `উলিয়াওক` | `pop` |
| `একো_নাই` | `nop` |
| `জঁপিয়াওক` | `jmp` |
| `তুলনা_কৰক` | `cmp` |
| `নহয়` | `not` |
| `পূৰণ_কৰক` | `mul` |
| `পৰীক্ষা_কৰক` | `test` |
| `বা` | `or` |
| `বাধা` | `int` |
| `বিয়োগ_কৰক` | `sub` |
| `ব্যৱস্থাৰ_আহ্বান` | `syscall` |
| `ভৰাওক` | `push` |
| `মাতক` | `call` |
| `যোগ_কৰক` | `add` |
| `লুপ` | `loop` |
| `স্থানান্তৰ` | `mov` |
| `স্বতন্ত্ৰ` | `xor` |
| `হৰণ_কৰক` | `div` |
| `ৰখক` | `hlt` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Assamese / অসমীয়া (as)
section .text
global _start

_start:
    স্থানান্তৰ rax, 1
    স্থানান্তৰ rdi, 1
    স্থানান্তৰ rsi, msg
    স্থানান্তৰ rdx, 13
    ব্যৱস্থাৰ_আহ্বান

    স্থানান্তৰ rax, 60
    স্থানান্তৰ rdi, 0
    ব্যৱস্থাৰ_আহ্বান

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm as programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build as programa.masm
```
