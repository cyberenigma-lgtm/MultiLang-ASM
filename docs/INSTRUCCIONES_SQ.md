# MultiLang-ASM: Manual de Instrucciones [SQ]

**Idioma:** Albanian / Shqip (`sq`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `asgje` | `nop` |
| `cikel` | `loop` |
| `dhe` | `and` |
| `ekskluzive` | `xor` |
| `fut` | `push` |
| `jo` | `not` |
| `kerce` | `jmp` |
| `krahaso` | `cmp` |
| `kthe` | `ret` |
| `leviz` | `mov` |
| `ndalo` | `hlt` |
| `nderprerje` | `int` |
| `nxirr` | `pop` |
| `ose` | `or` |
| `pjeseto` | `div` |
| `shto` | `add` |
| `shumezo` | `mul` |
| `testo` | `test` |
| `therrit` | `call` |
| `thirrje_sistemi` | `syscall` |
| `zbrit` | `sub` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Albanian / Shqip (sq)
section .text
global _start

_start:
    leviz rax, 1
    leviz rdi, 1
    leviz rsi, msg
    leviz rdx, 13
    thirrje_sistemi

    leviz rax, 60
    leviz rdi, 0
    thirrje_sistemi

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sq programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sq programa.masm
```
