# MultiLang-ASM: Manual de Instrucciones [FA]

**Idioma:** Persian / فارسی (`fa`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `افزایش` | `inc` |
| `انتقال` | `mov` |
| `انتقال_بایت` | `movsb` |
| `اگر_بزرگتر` | `jg` |
| `اگر_صفر` | `jz` |
| `اگر_مساوی` | `je` |
| `اگر_نامساوی` | `jne` |
| `اگر_کوچکتر` | `jl` |
| `بارگذاری_آدرس` | `lea` |
| `بارگذاری_بایت` | `lodsb` |
| `بازگشت` | `ret` |
| `بازگشت_سیستم` | `sysret` |
| `بایت_به_کلمه` | `cbw` |
| `تست` | `test` |
| `تعویض` | `xchg` |
| `تفریق` | `sub` |
| `تقسیم` | `div` |
| `توسعه_صفر` | `movzx` |
| `توسعه_علامت` | `movsx` |
| `توقف` | `hlt` |
| `تکرار` | `rep` |
| `جمع` | `add` |
| `حلقه` | `loop` |
| `حلقه_اگر_صفر` | `loopz` |
| `دوبل_به_کواد` | `cdq` |
| `ذخیره_بایت` | `stosb` |
| `ضرب` | `mul` |
| `فراخوانی` | `call` |
| `فراخوانی_سیستم` | `syscall` |
| `فشار` | `push` |
| `فشار_پرچم` | `pushf` |
| `مقایسه` | `cmp` |
| `نفی` | `neg` |
| `هیچی` | `nop` |
| `وقفه` | `int` |
| `پاپ` | `pop` |
| `پاپ_پرچم` | `popf` |
| `پرش` | `jmp` |
| `کاهش` | `dec` |
| `کلمه_به_دوبل` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Persian / فارسی (fa)
section .text
global _start

_start:
    انتقال rax, 1
    انتقال rdi, 1
    انتقال rsi, msg
    انتقال rdx, 13
    فراخوانی_سیستم

    انتقال rax, 60
    انتقال rdi, 0
    فراخوانی_سیستم

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm fa programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fa programa.masm
```
