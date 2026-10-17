# MultiLang-ASM: Manual de Instrucciones [SM]

**Idioma:** Samoan / Gagana Sāmoa (`sm`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `faalavelave` | `int` |
| `faaopoopo` | `add` |
| `faapitoa` | `xor` |
| `faatele` | `mul` |
| `faatusatusa` | `cmp` |
| `leai` | `not` |
| `leai_se_mea` | `nop` |
| `ma` | `and` |
| `matasele` | `loop` |
| `oso` | `jmp` |
| `pe` | `or` |
| `sui` | `mov` |
| `taofi` | `hlt` |
| `toe_foi` | `ret` |
| `toese` | `sub` |
| `tofotofo` | `test` |
| `toso` | `pop` |
| `tulei` | `push` |
| `vaevae` | `div` |
| `valaau` | `call` |
| `valaau_faiga` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Samoan / Gagana Sāmoa (sm)
section .text
global _start

_start:
    sui rax, 1
    sui rdi, 1
    sui rsi, msg
    sui rdx, 13
    valaau_faiga

    sui rax, 60
    sui rdi, 0
    valaau_faiga

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sm programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sm programa.masm
```
