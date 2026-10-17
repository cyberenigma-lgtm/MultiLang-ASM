# MultiLang-ASM: Manual de Instrucciones [TK]

**Idioma:** Turkmen / Türkmençe (`tk`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aýlaw` | `loop` |
| `aýratyn` | `xor` |
| `aýyr` | `sub` |
| `barla` | `test` |
| `bök` | `jmp` |
| `böl` | `div` |
| `deňeşdir` | `cmp` |
| `däl` | `not` |
| `gaýt` | `ret` |
| `geçir` | `mov` |
| `goş` | `add` |
| `hiç_zat` | `nop` |
| `it` | `push` |
| `kesilme` | `int` |
| `köpelt` | `mul` |
| `saklan` | `hlt` |
| `ulgam_çagyryşy` | `syscall` |
| `we` | `and` |
| `çagyr` | `call` |
| `çek` | `pop` |
| `ýa-da` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Turkmen / Türkmençe (tk)
section .text
global _start

_start:
    geçir rax, 1
    geçir rdi, 1
    geçir rsi, msg
    geçir rdx, 13
    ulgam_çagyryşy

    geçir rax, 60
    geçir rdi, 0
    ulgam_çagyryşy

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tk programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tk programa.masm
```
