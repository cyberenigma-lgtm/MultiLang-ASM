# MultiLang-ASM: Manual de Instrucciones [PS]

**Idioma:** Pashto / پښتو (`ps`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ازمویل` | `test` |
| `او` | `and` |
| `بلل` | `call` |
| `بهر_کول` | `pop` |
| `بیرته_راتلل` | `ret` |
| `جمع_کول` | `add` |
| `خنډ` | `int` |
| `درېدل` | `hlt` |
| `دننه_کول` | `push` |
| `سیسټم_غوښتنه` | `syscall` |
| `ضرب_کول` | `mul` |
| `لږدول` | `mov` |
| `منفي_کول` | `sub` |
| `نه` | `not` |
| `هیڅ_نه` | `nop` |
| `وېشل` | `div` |
| `ټوپ_وهل` | `jmp` |
| `پر پرتله_کول` | `cmp` |
| `ځانګړی` | `xor` |
| `څرخ` | `loop` |
| `یا` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Pashto / پښتو (ps)
section .text
global _start

_start:
    لږدول rax, 1
    لږدول rdi, 1
    لږدول rsi, msg
    لږدول rdx, 13
    سیسټم_غوښتنه

    لږدول rax, 60
    لږدول rdi, 0
    سیسټم_غوښتنه

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ps programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ps programa.masm
```
