# MultiLang-ASM: Manual de Instrucciones [RM]

**Idioma:** Romansh / Rumantsch (`rm`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `agiuntar` | `add` |
| `betg` | `not` |
| `chalar` | `hlt` |
| `clamada_sistem` | `syscall` |
| `clamar` | `call` |
| `cumparegliar` | `cmp` |
| `divider` | `div` |
| `e` | `and` |
| `exclusiv` | `xor` |
| `interrupziun` | `int` |
| `metter` | `push` |
| `mover` | `mov` |
| `multiplitgar` | `mul` |
| `nagut` | `nop` |
| `provar` | `test` |
| `rudien` | `loop` |
| `siglir` | `jmp` |
| `sulevar` | `sub` |
| `trair` | `pop` |
| `turnar` | `ret` |
| `u` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Romansh / Rumantsch (rm)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    clamada_sistem

    mover rax, 60
    mover rdi, 0
    clamada_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm rm programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build rm programa.masm
```
