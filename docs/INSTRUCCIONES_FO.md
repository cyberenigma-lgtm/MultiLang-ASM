# MultiLang-ASM: Manual de Instrucciones [FO]

**Idioma:** Faroese / Føroyskt (`fo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `avbrot` | `int` |
| `deil` | `div` |
| `drag_fra` | `sub` |
| `einki` | `nop` |
| `ella` | `or` |
| `falda` | `mul` |
| `flyt` | `mov` |
| `ikki` | `not` |
| `kall` | `call` |
| `legg_aftrat` | `add` |
| `leyp` | `jmp` |
| `lykkja` | `loop` |
| `og` | `and` |
| `royn` | `test` |
| `samanber` | `cmp` |
| `serstakt` | `xor` |
| `skipanarkall` | `syscall` |
| `skjot` | `push` |
| `steðga` | `hlt` |
| `tak` | `pop` |
| `vend_aftur` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Faroese / Føroyskt (fo)
section .text
global _start

_start:
    flyt rax, 1
    flyt rdi, 1
    flyt rsi, msg
    flyt rdx, 13
    skipanarkall

    flyt rax, 60
    flyt rdi, 0
    skipanarkall

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm fo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fo programa.masm
```
