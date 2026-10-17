# MultiLang-ASM: Manual de Instrucciones [LT]

**Idioma:** Lithuanian / Lietuvių (`lt`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `arba` | `or` |
| `atimti` | `sub` |
| `ciklas` | `loop` |
| `dalinti` | `div` |
| `dauginti` | `mul` |
| `grazinti` | `ret` |
| `ideti` | `push` |
| `ir` | `and` |
| `isimti` | `pop` |
| `isimtinai` | `xor` |
| `kviesti` | `call` |
| `ne` | `not` |
| `nieko` | `nop` |
| `palyginti` | `cmp` |
| `perkelti` | `mov` |
| `pertrauktis` | `int` |
| `prideti` | `add` |
| `sisteminis_iskvietimas` | `syscall` |
| `sokti` | `jmp` |
| `stabdyti` | `hlt` |
| `testuoti` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Lithuanian / Lietuvių (lt)
section .text
global _start

_start:
    perkelti rax, 1
    perkelti rdi, 1
    perkelti rsi, msg
    perkelti rdx, 13
    sisteminis_iskvietimas

    perkelti rax, 60
    perkelti rdi, 0
    sisteminis_iskvietimas

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm lt programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build lt programa.masm
```
