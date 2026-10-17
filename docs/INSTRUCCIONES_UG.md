# MultiLang-ASM: Manual de Instrucciones [UG]

**Idioma:** Uyghur / ئۇيغۇرچە (`ug`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ئالاھىدە` | `xor` |
| `ئايلانما` | `loop` |
| `ئۈزۈلۈش` | `int` |
| `ئېلىش` | `sub` |
| `ئەمەس` | `not` |
| `بۆلۈش` | `div` |
| `توختاش` | `hlt` |
| `سىستېما_چاقىرىقى` | `syscall` |
| `سىناش` | `test` |
| `سېلىشتۇرۇش` | `cmp` |
| `سەكرەش` | `jmp` |
| `قايتىش` | `ret` |
| `قوشۇش` | `add` |
| `كىرگۈزۈش` | `push` |
| `كۆپەيتىش` | `mul` |
| `ياكى` | `or` |
| `يۆتكەش` | `mov` |
| `چاقىرىش` | `call` |
| `چىقىرىش` | `pop` |
| `ھېچنېمە` | `nop` |
| `ۋە` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Uyghur / ئۇيغۇرچە (ug)
section .text
global _start

_start:
    يۆتكەش rax, 1
    يۆتكەش rdi, 1
    يۆتكەش rsi, msg
    يۆتكەش rdx, 13
    سىستېما_چاقىرىقى

    يۆتكەش rax, 60
    يۆتكەش rdi, 0
    سىستېما_چاقىرىقى

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ug programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ug programa.masm
```
