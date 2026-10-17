# MultiLang-ASM: Manual de Instrucciones [UR]

**Idioma:** Urdu / اردو (`ur`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `اور` | `and` |
| `تفریق` | `sub` |
| `تقسیم` | `div` |
| `جانچ` | `test` |
| `جمع` | `add` |
| `خلل` | `int` |
| `روکیں` | `hlt` |
| `سسٹم_کال` | `syscall` |
| `ضرب` | `mul` |
| `منتقل` | `mov` |
| `منفرد` | `xor` |
| `موازنہ` | `cmp` |
| `نکالیں` | `pop` |
| `نہیں` | `not` |
| `واپسی` | `ret` |
| `چکر` | `loop` |
| `چھلانگ` | `jmp` |
| `ڈالیں` | `push` |
| `کال` | `call` |
| `کچھ_نہیں` | `nop` |
| `یا` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Urdu / اردو (ur)
section .text
global _start

_start:
    منتقل rax, 1
    منتقل rdi, 1
    منتقل rsi, msg
    منتقل rdx, 13
    سسٹم_کال

    منتقل rax, 60
    منتقل rdi, 0
    سسٹم_کال

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ur programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ur programa.masm
```
