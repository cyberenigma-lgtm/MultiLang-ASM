# MultiLang-ASM: Manual de Instrucciones [HE]

**Idioma:** Hebrew / עברית (`he`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 33  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `אם_אפס` | `jz` |
| `אם_גדול` | `jg` |
| `אם_לא_שווה` | `jne` |
| `אם_קטן` | `jl` |
| `אם_שווה` | `je` |
| `בדוק` | `test` |
| `בייט_לוורד` | `cbw` |
| `דחוף` | `push` |
| `דחוף_דגלים` | `pushf` |
| `הזז` | `mov` |
| `הזז_בייט` | `movsb` |
| `החלף` | `xchg` |
| `השווה` | `cmp` |
| `וורד_לדאבל` | `cwd` |
| `חבר` | `add` |
| `חזור` | `ret` |
| `חזור_על` | `rep` |
| `חזרת_מערכת` | `sysret` |
| `חסר` | `sub` |
| `טען_בייט` | `lodsb` |
| `טען_כתובת` | `lea` |
| `כלום` | `nop` |
| `כפול` | `mul` |
| `לולאה` | `loop` |
| `לולאה_אם_אפס` | `loopz` |
| `משוך` | `pop` |
| `משוך_דגלים` | `popf` |
| `עצור` | `hlt` |
| `פסיקה` | `int` |
| `קפוץ` | `jmp` |
| `קרא` | `call` |
| `קריאת_מערכת` | `syscall` |
| `שמור_בייט` | `stosb` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hebrew / עברית (he)
section .text
global _start

_start:
    הזז rax, 1
    הזז rdi, 1
    הזז rsi, msg
    הזז rdx, 13
    קריאת_מערכת

    הזז rax, 60
    הזז rdi, 0
    קריאת_מערכת

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm he programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build he programa.masm
```
