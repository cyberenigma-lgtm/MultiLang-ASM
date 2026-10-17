# MultiLang-ASM: Manual de Instrucciones [SI]

**Idioma:** Sinhala / සිංහල (`si`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `අඩු_කරන්න` | `sub` |
| `අමතන්න` | `call` |
| `ඇතුල්_කරන්න` | `push` |
| `ඉවත්_කරන්න` | `pop` |
| `එකතු_කරන්න` | `add` |
| `කිසිවක්_නැත` | `nop` |
| `ගුණ_කරන්න` | `mul` |
| `ගෙනියන්න` | `mov` |
| `නවත්වන්න` | `hlt` |
| `නැත` | `not` |
| `නැවත_එන්න` | `ret` |
| `පද්ධති_ඇමතුම` | `syscall` |
| `පනින්න` | `jmp` |
| `පරීක්ෂා_කරන්න` | `test` |
| `බාධාව` | `int` |
| `බෙදන්න` | `div` |
| `ලූපය` | `loop` |
| `විශේෂ` | `xor` |
| `සසඳන්න` | `cmp` |
| `සහ` | `and` |
| `හෝ` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Sinhala / සිංහල (si)
section .text
global _start

_start:
    ගෙනියන්න rax, 1
    ගෙනියන්න rdi, 1
    ගෙනියන්න rsi, msg
    ගෙනියන්න rdx, 13
    පද්ධති_ඇමතුම

    ගෙනියන්න rax, 60
    ගෙනියන්න rdi, 0
    පද්ධති_ඇමතුම

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm si programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build si programa.masm
```
