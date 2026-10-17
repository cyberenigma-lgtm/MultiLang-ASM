# MultiLang-ASM: Manual de Instrucciones [HU]

**Idioma:** Hungarian / Magyar (`hu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `betesz` | `push` |
| `ciklus` | `loop` |
| `csere` | `xchg` |
| `csokkent` | `dec` |
| `es` | `and` |
| `ha_egyenlo` | `je` |
| `ha_nem_egyenlo` | `jne` |
| `hiv` | `call` |
| `hozzaad` | `add` |
| `kivesz` | `pop` |
| `kivon` | `sub` |
| `kizaro` | `xor` |
| `megall` | `hlt` |
| `megszakitas` | `int` |
| `mozgat` | `mov` |
| `nem` | `not` |
| `novel` | `inc` |
| `osszehasonlit` | `cmp` |
| `oszt` | `div` |
| `rendszerhivas` | `syscall` |
| `semmi` | `nop` |
| `szoroz` | `mul` |
| `tesztel` | `test` |
| `ugrik` | `jmp` |
| `vagy` | `or` |
| `visszater` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hungarian / Magyar (hu)
section .text
global _start

_start:
    mozgat rax, 1
    mozgat rdi, 1
    mozgat rsi, msg
    mozgat rdx, 13
    rendszerhivas

    mozgat rax, 60
    mozgat rdi, 0
    rendszerhivas

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm hu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build hu programa.masm
```
