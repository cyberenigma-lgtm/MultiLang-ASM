# MultiLang-ASM: Manual de Instrucciones [AM]

**Idioma:** Amharic / አማርኛ (`am`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ሁለት_ወደ_አራት` | `cdq` |
| `ሉፕ` | `loop` |
| `ምልክት_አስፋ` | `movsx` |
| `ምንም` | `nop` |
| `ሲስተም_ተመለስ` | `sysret` |
| `ሲስተም_ጥራ` | `syscall` |
| `ቀንስ` | `sub` |
| `ቀንስ_አንድ` | `dec` |
| `ቀይር` | `xchg` |
| `ቃል_ወደ_ሁለት` | `cwd` |
| `ባንዲራ_አውጣ` | `popf` |
| `ባንዲራ_ክተት` | `pushf` |
| `ባይት_አስቀምጥ` | `stosb` |
| `ባይት_አንቀሳቅስ` | `movsb` |
| `ባይት_ወደ_ቃል` | `cbw` |
| `ባይት_ጫን` | `lodsb` |
| `ተመለስ` | `ret` |
| `አሳድግ` | `inc` |
| `አቁም` | `hlt` |
| `አቋርጥ` | `int` |
| `አባዛ` | `mul` |
| `አንቀሳቅስ` | `mov` |
| `አካፍል` | `div` |
| `አወዳድር` | `cmp` |
| `አውጣ` | `pop` |
| `አድራሻ_ጫን` | `lea` |
| `እኩል_ከሆነ` | `je` |
| `እኩል_ካልሆነ` | `jne` |
| `ካድ` | `neg` |
| `ክተት` | `push` |
| `ዜሮ_ሉፕ` | `loopz` |
| `ዜሮ_አስፋ` | `movzx` |
| `ዜሮ_ከሆነ` | `jz` |
| `ዝለል` | `jmp` |
| `የበለጠ_ከሆነ` | `jg` |
| `ያነሰ_ከሆነ` | `jl` |
| `ደጋግም` | `rep` |
| `ጥራ` | `call` |
| `ጨምር` | `add` |
| `ፈትን` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Amharic / አማርኛ (am)
section .text
global _start

_start:
    አንቀሳቅስ rax, 1
    አንቀሳቅስ rdi, 1
    አንቀሳቅስ rsi, msg
    አንቀሳቅስ rdx, 13
    ሲስተም_ጥራ

    አንቀሳቅስ rax, 60
    አንቀሳቅስ rdi, 0
    ሲስተም_ጥራ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm am programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build am programa.masm
```
