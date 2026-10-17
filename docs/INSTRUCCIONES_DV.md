# MultiLang-ASM: Manual de Instrucciones [DV]

**Idioma:** Dhivehi / ދިވެހި (`dv`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ހުއްޓާ` | `hlt` |
| `ހުއްޓުން` | `int` |
| `ނަގާ` | `pop` |
| `ނުވަތަ` | `or` |
| `ނޫން` | `not` |
| `ބަހާ` | `div` |
| `ބަދަލުކުރޭ` | `mov` |
| `ބުރު` | `loop` |
| `ކަނޑާ` | `sub` |
| `އަނބުރާ` | `ret` |
| `އަޅާކިޔާ` | `cmp` |
| `އަދި` | `and` |
| `އެއްކުރޭ` | `add` |
| `އެއްވެސް_އެއްޗެއް_ނޫން` | `nop` |
| `ވަކި` | `xor` |
| `ފުންމާ` | `jmp` |
| `ލާ` | `push` |
| `ގުނަކުރޭ` | `mul` |
| `ގޮވާ` | `call` |
| `ސިސްޓަމް_ކޯލް` | `syscall` |
| `ޓެސްޓު` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Dhivehi / ދިވެހި (dv)
section .text
global _start

_start:
    ބަދަލުކުރޭ rax, 1
    ބަދަލުކުރޭ rdi, 1
    ބަދަލުކުރޭ rsi, msg
    ބަދަލުކުރޭ rdx, 13
    ސިސްޓަމް_ކޯލް

    ބަދަލުކުރޭ rax, 60
    ބަދަލުކުރޭ rdi, 0
    ސިސްޓަމް_ކޯލް

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm dv programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build dv programa.masm
```
