# MultiLang-ASM: Manual de Instrucciones [MR]

**Idioma:** Marathi / मराठी (`mr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `आणि` | `and` |
| `उडी` | `jmp` |
| `काढा` | `pop` |
| `काहीही_नाही` | `nop` |
| `किंवा` | `or` |
| `कॉल` | `call` |
| `गुणा` | `mul` |
| `टाका` | `push` |
| `तपासा` | `test` |
| `तुलना` | `cmp` |
| `थांबा` | `hlt` |
| `नाही` | `not` |
| `परत` | `ret` |
| `बेरीज` | `add` |
| `भागा` | `div` |
| `लूप` | `loop` |
| `वजा` | `sub` |
| `विशेष` | `xor` |
| `व्यत्यय` | `int` |
| `सिस्टम_कॉल` | `syscall` |
| `हलवा` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Marathi / मराठी (mr)
section .text
global _start

_start:
    हलवा rax, 1
    हलवा rdi, 1
    हलवा rsi, msg
    हलवा rdx, 13
    सिस्टम_कॉल

    हलवा rax, 60
    हलवा rdi, 0
    सिस्टम_कॉल

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mr programa.masm
```
