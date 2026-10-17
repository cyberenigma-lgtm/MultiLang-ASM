# MultiLang-ASM: Manual de Instrucciones [TI]

**Idioma:** Tigrinya / ትግርኛ (`ti`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `መርምር` | `test` |
| `መቅል` | `div` |
| `ምቁራጽ` | `int` |
| `ተመለስ` | `ret` |
| `ኣረኣኢ` | `cmp` |
| `ኣራብሕ` | `mul` |
| `ኣንቀሳቕስ` | `mov` |
| `ኣእቱ` | `push` |
| `ኣውጽእ` | `pop` |
| `ኣይኮነን` | `not` |
| `ኣጉድል` | `sub` |
| `ከምኡ_ውን` | `and` |
| `ወስኽ` | `add` |
| `ወይ` | `or` |
| `ዋላ_ሓንቲ` | `nop` |
| `ዑደት` | `loop` |
| `ዝለል` | `jmp` |
| `ደው_በል` | `hlt` |
| `ጸውዕ` | `call` |
| `ጻውዒት_ስርዓት` | `syscall` |
| `ፍሉይ` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tigrinya / ትግርኛ (ti)
section .text
global _start

_start:
    ኣንቀሳቕስ rax, 1
    ኣንቀሳቕስ rdi, 1
    ኣንቀሳቕስ rsi, msg
    ኣንቀሳቕስ rdx, 13
    ጻውዒት_ስርዓት

    ኣንቀሳቕስ rax, 60
    ኣንቀሳቕስ rdi, 0
    ጻውዒት_ስርዓት

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ti programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ti programa.masm
```
