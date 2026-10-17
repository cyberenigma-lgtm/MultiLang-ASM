# MultiLang-ASM: Manual de Instrucciones [KI]

**Idioma:** Kikuyu / Gĩkũyũ (`ki`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aaca` | `not` |
| `coka` | `ret` |
| `eheria` | `sub` |
| `gaya` | `div` |
| `gwĩta_kĩbũrũri` | `syscall` |
| `gũtirĩ_kĩndũ` | `nop` |
| `ikĩa` | `push` |
| `ingĩhia` | `mul` |
| `kana` | `or` |
| `kũhingĩcĩrĩrio` | `int` |
| `mwanya` | `xor` |
| `mũthiũrũrũko` | `loop` |
| `na` | `and` |
| `ongerera` | `add` |
| `ringithania` | `cmp` |
| `rũga` | `jmp` |
| `rũgama` | `hlt` |
| `rũta` | `pop` |
| `thaama` | `mov` |
| `thima` | `test` |
| `ĩta` | `call` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kikuyu / Gĩkũyũ (ki)
section .text
global _start

_start:
    thaama rax, 1
    thaama rdi, 1
    thaama rsi, msg
    thaama rdx, 13
    gwĩta_kĩbũrũri

    thaama rax, 60
    thaama rdi, 0
    gwĩta_kĩbũrũri

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ki programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ki programa.masm
```
