# MultiLang-ASM: Manual de Instrucciones [CHR]

**Idioma:** Cherokee / ᏣᎳᎩ (`chr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ᎠᎴ` | `and` |
| `ᎠᎵᏖᎸᏗ` | `jmp` |
| `ᎠᏂᏏᏍᏗ_ᎤᎵᏍᎨᏛ` | `syscall` |
| `ᎠᏎᎵᏙᏗ` | `test` |
| `ᎠᏓᏅᏖᏗ` | `sub` |
| `ᎠᏛᎯᏍᏙᏗ` | `add` |
| `ᎠᏟᎶᏍᏗ` | `cmp` |
| `ᎠᏠᏯᏍᏗ` | `mul` |
| `ᎠᏯᏂᏍᏗ` | `call` |
| `ᎠᏯᏙᎯᏍᏗ` | `div` |
| `ᎠᏲᏍᏙᏗ` | `int` |
| `ᎤᎴᏅᏛ` | `hlt` |
| `ᎤᏓᏅᏒ` | `xor` |
| `ᎤᏨᏒ` | `ret` |
| `ᎥᏝ` | `not` |
| `ᎦᎶᎯᏍᏗ` | `push` |
| `ᎦᏂᎩᏛ` | `pop` |
| `ᎦᏅᏍᏙᏗ` | `mov` |
| `ᎦᏛᏗ` | `loop` |
| `Ꮭ_ᎪᎱᏍᏗ` | `nop` |
| `ᏱᎩ` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Cherokee / ᏣᎳᎩ (chr)
section .text
global _start

_start:
    ᎦᏅᏍᏙᏗ rax, 1
    ᎦᏅᏍᏙᏗ rdi, 1
    ᎦᏅᏍᏙᏗ rsi, msg
    ᎦᏅᏍᏙᏗ rdx, 13
    ᎠᏂᏏᏍᏗ_ᎤᎵᏍᎨᏛ

    ᎦᏅᏍᏙᏗ rax, 60
    ᎦᏅᏍᏙᏗ rdi, 0
    ᎠᏂᏏᏍᏗ_ᎤᎵᏍᎨᏛ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm chr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build chr programa.masm
```
