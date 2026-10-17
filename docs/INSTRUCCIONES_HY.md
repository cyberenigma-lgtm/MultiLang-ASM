# MultiLang-ASM: Manual de Instrucciones [HY]

**Idioma:** Armenian / Հայերեն (`hy`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `բազմապատկել` | `mul` |
| `բաժանել` | `div` |
| `բացառիկ` | `xor` |
| `գումարել` | `add` |
| `ընդհատում` | `int` |
| `կամ` | `or` |
| `կանգնել` | `hlt` |
| `կանչել` | `call` |
| `համակարգային_կանչ` | `syscall` |
| `համեմատել` | `cmp` |
| `հանել` | `sub` |
| `հանել_ստեկից` | `pop` |
| `մտցնել` | `push` |
| `ոչ` | `not` |
| `ոչինչ` | `nop` |
| `վերադառնալ` | `ret` |
| `տեղափոխել` | `mov` |
| `ցատկել` | `jmp` |
| `ցիկլ` | `loop` |
| `փորձարկել` | `test` |
| `և` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Armenian / Հայերեն (hy)
section .text
global _start

_start:
    տեղափոխել rax, 1
    տեղափոխել rdi, 1
    տեղափոխել rsi, msg
    տեղափոխել rdx, 13
    համակարգային_կանչ

    տեղափոխել rax, 60
    տեղափոխել rdi, 0
    համակարգային_կանչ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm hy programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build hy programa.masm
```
