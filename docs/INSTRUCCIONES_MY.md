# MultiLang-ASM: Manual de Instrucciones [MY]

**Idioma:** Burmese / မြန်မာစာ (`my`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ကြားဖြတ်` | `int` |
| `ခုန်` | `jmp` |
| `ခေါ်` | `call` |
| `စစ်ဆေး` | `test` |
| `စနစ်ခေါ်ဆိုမှု` | `syscall` |
| `စား` | `div` |
| `ထည့်` | `push` |
| `ထုတ်` | `pop` |
| `နှင့်` | `and` |
| `နှိုင်းယှဉ်` | `cmp` |
| `နှုတ်` | `sub` |
| `ပတ်လမ်း` | `loop` |
| `ပေါင်း` | `add` |
| `ပြန်` | `ret` |
| `ဘာမှမရှိ` | `nop` |
| `မဟုတ်` | `not` |
| `မြှောက်` | `mul` |
| `ရပ်` | `hlt` |
| `ရွှေ့` | `mov` |
| `သို့မဟုတ်` | `or` |
| `သီးသန့်` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Burmese / မြန်မာစာ (my)
section .text
global _start

_start:
    ရွှေ့ rax, 1
    ရွှေ့ rdi, 1
    ရွှေ့ rsi, msg
    ရွှေ့ rdx, 13
    စနစ်ခေါ်ဆိုမှု

    ရွှေ့ rax, 60
    ရွှေ့ rdi, 0
    စနစ်ခေါ်ဆိုမှု

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm my programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build my programa.masm
```
