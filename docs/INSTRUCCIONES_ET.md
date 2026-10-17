# MultiLang-ASM: Manual de Instrucciones [ET]

**Idioma:** Estonian / Eesti (`et`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `huppa` | `jmp` |
| `ja` | `and` |
| `jaga` | `div` |
| `katkestus` | `int` |
| `korruta` | `mul` |
| `kutsu` | `call` |
| `lahuta` | `sub` |
| `liida` | `add` |
| `liiguta` | `mov` |
| `mitte` | `not` |
| `mittemidagi` | `nop` |
| `peata` | `hlt` |
| `susteemikutse` | `syscall` |
| `tagasta` | `ret` |
| `testi` | `test` |
| `tiri` | `pop` |
| `tsukkel` | `loop` |
| `tuka` | `push` |
| `valistav` | `xor` |
| `voi` | `or` |
| `vordle` | `cmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Estonian / Eesti (et)
section .text
global _start

_start:
    liiguta rax, 1
    liiguta rdi, 1
    liiguta rsi, msg
    liiguta rdx, 13
    susteemikutse

    liiguta rax, 60
    liiguta rdi, 0
    susteemikutse

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm et programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build et programa.masm
```
