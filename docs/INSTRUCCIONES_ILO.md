# MultiLang-ASM: Manual de Instrucciones [ILO]

**Idioma:** Ilocano / Ilokano (`ilo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `agsardeng` | `hlt` |
| `awag_ti_sistema` | `syscall` |
| `awagan` | `call` |
| `awan` | `nop` |
| `bingayen` | `div` |
| `idilig` | `cmp` |
| `iduron` | `push` |
| `iguyod` | `pop` |
| `ikkat` | `sub` |
| `inayon` | `add` |
| `ket` | `and` |
| `lagto` | `jmp` |
| `naisangayan` | `xor` |
| `paaduen` | `mul` |
| `rikos` | `loop` |
| `saan` | `not` |
| `singa` | `int` |
| `subli` | `ret` |
| `suboken` | `test` |
| `wenno` | `or` |
| `yakar` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Ilocano / Ilokano (ilo)
section .text
global _start

_start:
    yakar rax, 1
    yakar rdi, 1
    yakar rsi, msg
    yakar rdx, 13
    awag_ti_sistema

    yakar rax, 60
    yakar rdi, 0
    awag_ti_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ilo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ilo programa.masm
```
