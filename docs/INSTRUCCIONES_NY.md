# MultiLang-ASM: Manual de Instrucciones [NY]

**Idioma:** Chichewa / Nyanja (`ny`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ayi` | `not` |
| `bwererani` | `ret` |
| `chapaderadera` | `xor` |
| `chidule` | `int` |
| `chotsani` | `sub` |
| `chulukitsani` | `mul` |
| `dumpha` | `jmp` |
| `gawani` | `div` |
| `imani` | `hlt` |
| `itanani` | `call` |
| `kankhirani` | `push` |
| `kapena` | `or` |
| `kuitana_makina` | `syscall` |
| `kuzungulira` | `loop` |
| `ndi` | `and` |
| `onjezani` | `add` |
| `palibe` | `nop` |
| `suntha` | `mov` |
| `tulutsani` | `pop` |
| `yerekezerani` | `cmp` |
| `yesani` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Chichewa / Nyanja (ny)
section .text
global _start

_start:
    suntha rax, 1
    suntha rdi, 1
    suntha rsi, msg
    suntha rdx, 13
    kuitana_makina

    suntha rax, 60
    suntha rdi, 0
    kuitana_makina

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ny programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ny programa.masm
```
