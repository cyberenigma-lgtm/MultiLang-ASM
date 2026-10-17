# MultiLang-ASM: Manual de Instrucciones [EO]

**Idioma:** Esperanto (`eo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aldoni` | `add` |
| `au` | `or` |
| `buklo` | `loop` |
| `dividi` | `div` |
| `ekskluziva` | `xor` |
| `halti` | `hlt` |
| `interrompo` | `int` |
| `kaj` | `and` |
| `kompari` | `cmp` |
| `movi` | `mov` |
| `multipliki` | `mul` |
| `ne` | `not` |
| `nenio` | `nop` |
| `pusxi` | `push` |
| `reveni` | `ret` |
| `salti` | `jmp` |
| `sistemvoko` | `syscall` |
| `subtrahi` | `sub` |
| `testi` | `test` |
| `tiri` | `pop` |
| `voki` | `call` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Esperanto (eo)
section .text
global _start

_start:
    movi rax, 1
    movi rdi, 1
    movi rsi, msg
    movi rdx, 13
    sistemvoko

    movi rax, 60
    movi rdi, 0
    sistemvoko

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm eo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build eo programa.masm
```
