# MultiLang-ASM: Manual de Instrucciones [KA]

**Idioma:** Georgian / ქართული (`ka`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ამოღება` | `pop` |
| `ან` | `or` |
| `არა` | `not` |
| `არაფერი` | `nop` |
| `გადატანა` | `mov` |
| `გადახტომა` | `jmp` |
| `გამოკლება` | `sub` |
| `გამორიცხვითი` | `xor` |
| `გამოძახება` | `call` |
| `გამრავლება` | `mul` |
| `გაყოფა` | `div` |
| `გაჩერება` | `hlt` |
| `და` | `and` |
| `დაბრუნება` | `ret` |
| `მიმატება` | `add` |
| `სისტემური_ზარი` | `syscall` |
| `შედარება` | `cmp` |
| `შემოწმება` | `test` |
| `შეწყვეტა` | `int` |
| `ჩადება` | `push` |
| `ციკლი` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Georgian / ქართული (ka)
section .text
global _start

_start:
    გადატანა rax, 1
    გადატანა rdi, 1
    გადატანა rsi, msg
    გადატანა rdx, 13
    სისტემური_ზარი

    გადატანა rax, 60
    გადატანა rdi, 0
    სისტემური_ზარი

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ka programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ka programa.masm
```
