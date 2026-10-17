# MultiLang-ASM: Manual de Instrucciones [RN]

**Idioma:** Kirundi (`rn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `canke` | `or` |
| `gabura` | `div` |
| `gereranya` | `cmp` |
| `gereza` | `test` |
| `gwiza` | `mul` |
| `hagarara` | `hlt` |
| `hamagara` | `call` |
| `ihamagara_ry_uburyo` | `syscall` |
| `ikizunguruko` | `loop` |
| `injiza` | `push` |
| `kuraho` | `sub` |
| `na` | `and` |
| `ntakintu` | `nop` |
| `ongerako` | `add` |
| `oya` | `not` |
| `rudende` | `xor` |
| `simbuka` | `jmp` |
| `sokora` | `pop` |
| `subira` | `ret` |
| `uguhagarika` | `int` |
| `yimura` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kirundi (rn)
section .text
global _start

_start:
    yimura rax, 1
    yimura rdi, 1
    yimura rsi, msg
    yimura rdx, 13
    ihamagara_ry_uburyo

    yimura rax, 60
    yimura rdi, 0
    ihamagara_ry_uburyo

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm rn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build rn programa.masm
```
