# MultiLang-ASM: Manual de Instrucciones [UZ]

**Idioma:** Uzbek / O'zbek (`uz`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ayir` | `sub` |
| `bol` | `div` |
| `chaqir` | `call` |
| `chiqar` | `pop` |
| `emas` | `not` |
| `hech_narsa` | `nop` |
| `istisno` | `xor` |
| `kirit` | `push` |
| `kochir` | `mov` |
| `kopaytir` | `mul` |
| `qayt` | `ret` |
| `qosh` | `add` |
| `sakrash` | `jmp` |
| `solishtir` | `cmp` |
| `tekshir` | `test` |
| `tizim_chaqiruvi` | `syscall` |
| `toxta` | `hlt` |
| `tsikl` | `loop` |
| `uzilish` | `int` |
| `va` | `and` |
| `yoki` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Uzbek / O'zbek (uz)
section .text
global _start

_start:
    kochir rax, 1
    kochir rdi, 1
    kochir rsi, msg
    kochir rdx, 13
    tizim_chaqiruvi

    kochir rax, 60
    kochir rdi, 0
    tizim_chaqiruvi

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm uz programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build uz programa.masm
```
