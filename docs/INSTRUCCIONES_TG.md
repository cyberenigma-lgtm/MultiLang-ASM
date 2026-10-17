# MultiLang-ASM: Manual de Instrucciones [TG]

**Idioma:** Tajik / Тоҷикӣ (`tg`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `баргаштан` | `ret` |
| `ва` | `and` |
| `гузоштан` | `push` |
| `давр` | `loop` |
| `даъват_кардан` | `call` |
| `даъвати_системавӣ` | `syscall` |
| `зарб_кардан` | `mul` |
| `истисноӣ` | `xor` |
| `истодан` | `hlt` |
| `кашидан` | `pop` |
| `кӯчонидан` | `mov` |
| `муқоиса_кардан` | `cmp` |
| `не` | `not` |
| `санҷидан` | `test` |
| `тарҳ_кардан` | `sub` |
| `тақсим_кардан` | `div` |
| `чамъ_кардан` | `add` |
| `ё` | `or` |
| `қатъ` | `int` |
| `ҳеҷ_чиз` | `nop` |
| `ҷаҳидан` | `jmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tajik / Тоҷикӣ (tg)
section .text
global _start

_start:
    кӯчонидан rax, 1
    кӯчонидан rdi, 1
    кӯчонидан rsi, msg
    кӯчонидан rdx, 13
    даъвати_системавӣ

    кӯчонидан rax, 60
    кӯчонидан rdi, 0
    даъвати_системавӣ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tg programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tg programa.masm
```
