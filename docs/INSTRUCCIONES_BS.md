# MultiLang-ASM: Manual de Instrucciones [BS]

**Idioma:** Bosnian / Bosanski (`bs`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `gurni` | `push` |
| `i` | `and` |
| `ili` | `or` |
| `iskljucivo` | `xor` |
| `izvadi` | `pop` |
| `ne` | `not` |
| `nista` | `nop` |
| `oduzmi` | `sub` |
| `petlja` | `loop` |
| `podijeli` | `div` |
| `pomjeri` | `mov` |
| `pomnozi` | `mul` |
| `pozovi` | `call` |
| `prekid` | `int` |
| `provjeri` | `test` |
| `saberi` | `add` |
| `sistemski_poziv` | `syscall` |
| `skoci` | `jmp` |
| `uporedi` | `cmp` |
| `vrati` | `ret` |
| `zaustavi` | `hlt` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Bosnian / Bosanski (bs)
section .text
global _start

_start:
    pomjeri rax, 1
    pomjeri rdi, 1
    pomjeri rsi, msg
    pomjeri rdx, 13
    sistemski_poziv

    pomjeri rax, 60
    pomjeri rdi, 0
    sistemski_poziv

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm bs programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build bs programa.masm
```
