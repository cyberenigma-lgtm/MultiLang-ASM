# MultiLang-ASM: Manual de Instrucciones [SL]

**Idioma:** Slovenian / Slovenščina (`sl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ali` | `or` |
| `deli` | `div` |
| `dodaj` | `add` |
| `in` | `and` |
| `izkljucno` | `xor` |
| `ne` | `not` |
| `nic` | `nop` |
| `odstej` | `sub` |
| `poklici` | `call` |
| `pomnozi` | `mul` |
| `porini` | `push` |
| `prekinitev` | `int` |
| `premakni` | `mov` |
| `primerjaj` | `cmp` |
| `sistemski_klic` | `syscall` |
| `skoci` | `jmp` |
| `testiraj` | `test` |
| `ustavi` | `hlt` |
| `vrni` | `ret` |
| `vzemi` | `pop` |
| `zanka` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Slovenian / Slovenščina (sl)
section .text
global _start

_start:
    premakni rax, 1
    premakni rdi, 1
    premakni rsi, msg
    premakni rdx, 13
    sistemski_klic

    premakni rax, 60
    premakni rdi, 0
    sistemski_klic

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sl programa.masm
```
