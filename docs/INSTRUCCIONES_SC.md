# MultiLang-ASM: Manual de Instrucciones [SC]

**Idioma:** Sardinian / Sardu (`sc`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `azunghere` | `add` |
| `bogare` | `sub` |
| `chircu` | `loop` |
| `ciamadore_sistema` | `syscall` |
| `ciamare` | `call` |
| `cunfrontare` | `cmp` |
| `e` | `and` |
| `esclusivu` | `xor` |
| `firmare` | `hlt` |
| `interrutzione` | `int` |
| `leare` | `pop` |
| `movimentare` | `mov` |
| `multiplicare` | `mul` |
| `non` | `not` |
| `nudda` | `nop` |
| `o` | `or` |
| `partire` | `div` |
| `pompire` | `push` |
| `proare` | `test` |
| `sartare` | `jmp` |
| `torrare` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Sardinian / Sardu (sc)
section .text
global _start

_start:
    movimentare rax, 1
    movimentare rdi, 1
    movimentare rsi, msg
    movimentare rdx, 13
    ciamadore_sistema

    movimentare rax, 60
    movimentare rdi, 0
    ciamadore_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sc programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sc programa.masm
```
