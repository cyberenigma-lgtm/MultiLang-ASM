# MultiLang-ASM: Manual de Instrucciones [KN]

**Idioma:** Kannada / ಕನ್ನಡ (`kn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ಅಥವಾ` | `or` |
| `ಇಲ್ಲ` | `not` |
| `ಏನೂ_ಇಲ್ಲ` | `nop` |
| `ಕರೆ` | `call` |
| `ಕಳೆಯಿರಿ` | `sub` |
| `ಕೂಡಿಸು` | `add` |
| `ಗುಣಿಸು` | `mul` |
| `ಜಿಗಿ` | `jmp` |
| `ತಡೆ` | `int` |
| `ತೆಗೆಯಿರಿ` | `pop` |
| `ನಿಲ್ಲಿಸು` | `hlt` |
| `ಪರೀಕ್ಷಿಸಿ` | `test` |
| `ಭಾಗಿಸು` | `div` |
| `ಮತ್ತು` | `and` |
| `ವಿಶೇಷ` | `xor` |
| `ವ್ಯವಸ್ಥೆ_ಕರೆ` | `syscall` |
| `ಸುತ್ತು` | `loop` |
| `ಸ್ಥಳಾಂತರಿಸಿ` | `mov` |
| `ಹಾಕಿ` | `push` |
| `ಹಿಂತಿರುಗಿ` | `ret` |
| `ಹೋಲಿಸಿ` | `cmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kannada / ಕನ್ನಡ (kn)
section .text
global _start

_start:
    ಸ್ಥಳಾಂತರಿಸಿ rax, 1
    ಸ್ಥಳಾಂತರಿಸಿ rdi, 1
    ಸ್ಥಳಾಂತರಿಸಿ rsi, msg
    ಸ್ಥಳಾಂತರಿಸಿ rdx, 13
    ವ್ಯವಸ್ಥೆ_ಕರೆ

    ಸ್ಥಳಾಂತರಿಸಿ rax, 60
    ಸ್ಥಳಾಂತರಿಸಿ rdi, 0
    ವ್ಯವಸ್ಥೆ_ಕರೆ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm kn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build kn programa.masm
```
