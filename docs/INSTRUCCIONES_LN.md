# MultiLang-ASM: Manual de Instrucciones [LN]

**Idioma:** Lingala (`ln`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `bakisa` | `add` |
| `benga` | `call` |
| `bimisa` | `pop` |
| `boma` | `mov` |
| `eloko_te` | `nop` |
| `kabola` | `div` |
| `kakeseni` | `xor` |
| `kobienga_ebongiseli` | `syscall` |
| `kokatisa` | `int` |
| `kotisa` | `push` |
| `longola` | `sub` |
| `matisa` | `mul` |
| `meka` | `test` |
| `mekanisa` | `cmp` |
| `pe` | `and` |
| `pumbwa` | `jmp` |
| `te` | `not` |
| `telemisa` | `hlt` |
| `to` | `or` |
| `zinga` | `loop` |
| `zonga` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Lingala (ln)
section .text
global _start

_start:
    boma rax, 1
    boma rdi, 1
    boma rsi, msg
    boma rdx, 13
    kobienga_ebongiseli

    boma rax, 60
    boma rdi, 0
    kobienga_ebongiseli

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ln programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ln programa.masm
```
