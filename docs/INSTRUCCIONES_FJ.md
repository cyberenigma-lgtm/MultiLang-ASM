# MultiLang-ASM: Manual de Instrucciones [FJ]

**Idioma:** Fijian / Na Vosa Vakaviti (`fj`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `biliga` | `push` |
| `cava` | `hlt` |
| `kaci_ni_ivakarau` | `syscall` |
| `kaciva` | `call` |
| `kauta_mai` | `pop` |
| `kauta_tani` | `sub` |
| `kei_na` | `and` |
| `kuria` | `add` |
| `lesu` | `ret` |
| `ria` | `jmp` |
| `se` | `or` |
| `sega` | `not` |
| `sega_na_ka` | `nop` |
| `tarova` | `int` |
| `tosoya` | `mov` |
| `vakalewena` | `mul` |
| `vakatautauvatataka` | `cmp` |
| `vakatikitiki` | `xor` |
| `vakatovolea` | `test` |
| `wasea` | `div` |
| `wavoki` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Fijian / Na Vosa Vakaviti (fj)
section .text
global _start

_start:
    tosoya rax, 1
    tosoya rdi, 1
    tosoya rsi, msg
    tosoya rdx, 13
    kaci_ni_ivakarau

    tosoya rax, 60
    tosoya rdi, 0
    kaci_ni_ivakarau

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm fj programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fj programa.masm
```
