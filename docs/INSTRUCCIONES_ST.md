# MultiLang-ASM: Manual de Instrucciones [ST]

**Idioma:** Sesotho (`st`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `arola` | `div` |
| `bapisa` | `cmp` |
| `biletsa` | `call` |
| `eketsa` | `add` |
| `ema` | `hlt` |
| `eseng` | `not` |
| `ha_ho_letho` | `nop` |
| `kapa` | `or` |
| `kenya` | `push` |
| `kgethehileng` | `xor` |
| `khutla` | `ret` |
| `le` | `and` |
| `leka` | `test` |
| `ngatafatsa` | `mul` |
| `ntsha` | `pop` |
| `piletso_ya_tsamaiso` | `syscall` |
| `sedikadikwe` | `loop` |
| `suthisa` | `mov` |
| `tlola` | `jmp` |
| `tlosa` | `sub` |
| `tshenyo` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Sesotho (st)
section .text
global _start

_start:
    suthisa rax, 1
    suthisa rdi, 1
    suthisa rsi, msg
    suthisa rdx, 13
    piletso_ya_tsamaiso

    suthisa rax, 60
    suthisa rdi, 0
    piletso_ya_tsamaiso

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm st programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build st programa.masm
```
