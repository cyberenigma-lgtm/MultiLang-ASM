# MultiLang-ASM: Manual de Instrucciones [AR]

**Idioma:** Arabic / العربية (`ar`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 45  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `إذا_أصغر` | `jl` |
| `إذا_أكبر` | `jg` |
| `إذا_صفر` | `jz` |
| `إذا_لا_يساوي` | `jne` |
| `إذا_يساوي` | `je` |
| `إضافة` | `add` |
| `اتصل` | `call` |
| `اختبر` | `test` |
| `ادفع` | `push` |
| `ادفع_الأعلام` | `pushf` |
| `استدعاء` | `call` |
| `استدعاء_النظام` | `syscall` |
| `اسحب` | `pop` |
| `اسحب_الأعلام` | `popf` |
| `اقفز` | `jmp` |
| `تبديل` | `xchg` |
| `تحميل_بايت` | `lodsb` |
| `تحميل_فعال` | `lea` |
| `تحويل_بايت_كلمة` | `cbw` |
| `تحويل_كلمة_مزدوجة` | `cwd` |
| `تحويل_مزدوج_رباعي` | `cdq` |
| `تخزين_بايت` | `stosb` |
| `توسيع_إشارة` | `movsx` |
| `توسيع_صفر` | `movzx` |
| `توقف` | `hlt` |
| `جمع` | `add` |
| `حلقة` | `loop` |
| `حلقة_إذا_صفر` | `loopz` |
| `رجوع` | `ret` |
| `زيادة` | `inc` |
| `ضرب` | `mul` |
| `ضرب_إشارة` | `imul` |
| `طرح` | `sub` |
| `عد` | `ret` |
| `عودة_النظام` | `sysret` |
| `قارن` | `cmp` |
| `قسمة` | `div` |
| `قسمة_إشارة` | `idiv` |
| `كرر` | `rep` |
| `لاشيء` | `nop` |
| `مقاطعة` | `int` |
| `نفي` | `neg` |
| `نقص` | `dec` |
| `نقل` | `mov` |
| `نقل_بايت` | `movsb` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Arabic / العربية (ar)
section .text
global _start

_start:
    نقل rax, 1
    نقل rdi, 1
    نقل rsi, msg
    نقل rdx, 13
    استدعاء_النظام

    نقل rax, 60
    نقل rdi, 0
    استدعاء_النظام

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ar programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ar programa.masm
```
