# MultiLang-ASM: Manual de Instrucciones [LG]

**Idioma:** Ganda / Luganda (`lg`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `buuka` | `jmp` |
| `ennetoloola` | `loop` |
| `gabanako` | `div` |
| `geraageranya` | `cmp` |
| `gyamu` | `pop` |
| `kebera` | `test` |
| `komawo` | `ret` |
| `kubisaamu` | `mul` |
| `kyawukana` | `xor` |
| `ne` | `and` |
| `nedda` | `not` |
| `oba` | `or` |
| `okusalako` | `int` |
| `omulanga_gw_enkola` | `syscall` |
| `sindiika` | `mov` |
| `tewali` | `nop` |
| `toolako` | `sub` |
| `yimirira` | `hlt` |
| `yingiza` | `push` |
| `yita` | `call` |
| `yongerako` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Ganda / Luganda (lg)
section .text
global _start

_start:
    sindiika rax, 1
    sindiika rdi, 1
    sindiika rsi, msg
    sindiika rdx, 13
    omulanga_gw_enkola

    sindiika rax, 60
    sindiika rdi, 0
    omulanga_gw_enkola

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm lg programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build lg programa.masm
```
