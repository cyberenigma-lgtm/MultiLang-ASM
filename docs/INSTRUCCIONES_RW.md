# MultiLang-ASM: Manual de Instrucciones [RW]

**Idioma:** Kinyarwanda (`rw`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `cyangwa` | `or` |
| `gabanya` | `div` |
| `garuka` | `ret` |
| `gerageza` | `test` |
| `gereranya` | `cmp` |
| `guhagarika` | `int` |
| `guhamagara_sisitemu` | `syscall` |
| `gwandika` | `mul` |
| `hagarara` | `hlt` |
| `hamagara` | `call` |
| `imura` | `mov` |
| `kura` | `sub` |
| `kuramo` | `pop` |
| `na` | `and` |
| `ntakintu` | `nop` |
| `ongera` | `add` |
| `oya` | `not` |
| `shyiramo` | `push` |
| `simbuka` | `jmp` |
| `umwihariko` | `xor` |
| `uruziga` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kinyarwanda (rw)
section .text
global _start

_start:
    imura rax, 1
    imura rdi, 1
    imura rsi, msg
    imura rdx, 13
    guhamagara_sisitemu

    imura rax, 60
    imura rdi, 0
    guhamagara_sisitemu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm rw programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build rw programa.masm
```
