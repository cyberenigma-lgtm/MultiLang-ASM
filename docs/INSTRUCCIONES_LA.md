# MultiLang-ASM: Manual de Instrucciones [LA]

**Idioma:** Latin / Latina (`la`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `addere` | `add` |
| `aut` | `or` |
| `circulus` | `loop` |
| `comparare` | `cmp` |
| `disiunctivum` | `xor` |
| `dividere` | `div` |
| `et` | `and` |
| `interruptio` | `int` |
| `movere` | `mov` |
| `multiplicare` | `mul` |
| `nihil` | `nop` |
| `non` | `not` |
| `probare` | `test` |
| `redire` | `ret` |
| `saltare` | `jmp` |
| `sistere` | `hlt` |
| `subtrahere` | `sub` |
| `trahere` | `pop` |
| `trudere` | `push` |
| `vocare` | `call` |
| `vocatio_systematis` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Latin / Latina (la)
section .text
global _start

_start:
    movere rax, 1
    movere rdi, 1
    movere rsi, msg
    movere rdx, 13
    vocatio_systematis

    movere rax, 60
    movere rdi, 0
    vocatio_systematis

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm la programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build la programa.masm
```
