# MultiLang-ASM: Manual de Instrucciones [MT]

**Idioma:** Maltese / Malti (`mt`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aqbez` | `jmp` |
| `aqsam` | `div` |
| `esklussiv` | `xor` |
| `imbutta` | `push` |
| `immoltiplika` | `mul` |
| `interruzzjoni` | `int` |
| `irritorna` | `ret` |
| `ittestja` | `test` |
| `jew` | `or` |
| `linja` | `loop` |
| `mexxi` | `mov` |
| `mhux` | `not` |
| `naqqas` | `sub` |
| `ohrog` | `pop` |
| `qabbel` | `cmp` |
| `sejha_sistema` | `syscall` |
| `sejjaħ` | `call` |
| `u` | `and` |
| `waqqaf` | `hlt` |
| `xejn` | `nop` |
| `zid` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Maltese / Malti (mt)
section .text
global _start

_start:
    mexxi rax, 1
    mexxi rdi, 1
    mexxi rsi, msg
    mexxi rdx, 13
    sejha_sistema

    mexxi rax, 60
    mexxi rdi, 0
    sejha_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mt programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mt programa.masm
```
