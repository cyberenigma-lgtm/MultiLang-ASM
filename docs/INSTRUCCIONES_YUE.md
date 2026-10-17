# MultiLang-ASM: Manual de Instrucciones [YUE]

**Idioma:** Cantonese / 粵語 (`yue`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `中斷` | `int` |
| `乘` | `mul` |
| `乜都唔做` | `nop` |
| `位元組變字` | `cbw` |
| `停` | `hlt` |
| `加` | `add` |
| `加一` | `inc` |
| `叫` | `call` |
| `叫系統` | `syscall` |
| `圈` | `loop` |
| `如果唔等` | `jne` |
| `如果大` | `jg` |
| `如果等` | `je` |
| `如果細` | `jl` |
| `如果零` | `jz` |
| `字變雙字` | `cwd` |
| `存位元組` | `stosb` |
| `彈出` | `pop` |
| `彈標誌` | `popf` |
| `推入` | `push` |
| `推標誌` | `pushf` |
| `換` | `xchg` |
| `搬` | `mov` |
| `搬位元組` | `movsb` |
| `攞位元組` | `lodsb` |
| `攞有效地址` | `lea` |
| `比` | `cmp` |
| `減` | `sub` |
| `減一` | `dec` |
| `符號擴展` | `movsx` |
| `試` | `test` |
| `變負` | `neg` |
| `跳` | `jmp` |
| `返` | `ret` |
| `返系統` | `sysret` |
| `重複` | `rep` |
| `除` | `div` |
| `雙字變四字` | `cdq` |
| `零圈` | `loopz` |
| `零擴展` | `movzx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Cantonese / 粵語 (yue)
section .text
global _start

_start:
    搬 rax, 1
    搬 rdi, 1
    搬 rsi, msg
    搬 rdx, 13
    叫系統

    搬 rax, 60
    搬 rdi, 0
    叫系統

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm yue programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build yue programa.masm
```
