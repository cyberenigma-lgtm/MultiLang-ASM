# MultiLang-ASM: Manual de Instrucciones [BE]

**Idioma:** Belarusian / Беларуская (`be`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `або` | `or` |
| `адняць` | `sub` |
| `выключнае` | `xor` |
| `выклікаць` | `call` |
| `выняць` | `pop` |
| `вярнуць` | `ret` |
| `дадаць` | `add` |
| `не` | `not` |
| `нічога` | `nop` |
| `падзяліць` | `div` |
| `пакласці` | `push` |
| `памножыць` | `mul` |
| `параўнаць` | `cmp` |
| `перамясціць` | `mov` |
| `перапыненне` | `int` |
| `праверыць` | `test` |
| `скокнуць` | `jmp` |
| `спыніць` | `hlt` |
| `сістэмны_выклік` | `syscall` |
| `цыкл` | `loop` |
| `і` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Belarusian / Беларуская (be)
section .text
global _start

_start:
    перамясціць rax, 1
    перамясціць rdi, 1
    перамясціць rsi, msg
    перамясціць rdx, 13
    сістэмны_выклік

    перамясціць rax, 60
    перамясціць rdi, 0
    сістэмны_выклік

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm be programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build be programa.masm
```
