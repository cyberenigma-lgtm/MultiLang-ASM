# MultiLang-ASM: Manual de Instrucciones [HR]

**Idioma:** Croatian / Hrvatski (`hr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ako_jednako` | `je` |
| `ako_nije` | `jne` |
| `dodaj` | `add` |
| `gurni` | `push` |
| `i` | `and` |
| `ili` | `or` |
| `iskljucivo` | `xor` |
| `izvuci` | `pop` |
| `ne` | `not` |
| `nista` | `nop` |
| `oduzmi` | `sub` |
| `petlja` | `loop` |
| `podijeli` | `div` |
| `pomnozi` | `mul` |
| `povecaj` | `inc` |
| `pozovi` | `call` |
| `prekid` | `int` |
| `premjesti` | `mov` |
| `razmijeni` | `xchg` |
| `sistemski_poziv` | `syscall` |
| `skoci` | `jmp` |
| `smanji` | `dec` |
| `testiraj` | `test` |
| `usporedi` | `cmp` |
| `vrati` | `ret` |
| `zaustavi` | `hlt` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Croatian / Hrvatski (hr)
section .text
global _start

_start:
    premjesti rax, 1
    premjesti rdi, 1
    premjesti rsi, msg
    premjesti rdx, 13
    sistemski_poziv

    premjesti rax, 60
    premjesti rdi, 0
    sistemski_poziv

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm hr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build hr programa.masm
```
