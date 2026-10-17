# MultiLang-ASM: Manual de Instrucciones [BO]

**Idioma:** Tibetan / བོད་སྐད་ (`bo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ཅི་ཡང་མེད` | `nop` |
| `ཐུན་མོང_མིན་པ` | `xor` |
| `དང` | `and` |
| `ཕྱིར་ལོག` | `ret` |
| `བགོ` | `div` |
| `བར་ཆད` | `int` |
| `བསྡུར` | `cmp` |
| `མ་ལག_འབོད་པ` | `syscall` |
| `མཆོང` | `jmp` |
| `མཚམས་འཇོག` | `hlt` |
| `མིན` | `not` |
| `ཚོད་ལྟ` | `test` |
| `འཁོར་ལོ` | `loop` |
| `འཇུག` | `push` |
| `འཐེན` | `sub` |
| `འདོན` | `pop` |
| `འབོད` | `call` |
| `ཡང་ན` | `or` |
| `སྒྱུར` | `mul` |
| `སྣོན` | `add` |
| `སྤོ` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tibetan / བོད་སྐད་ (bo)
section .text
global _start

_start:
    སྤོ rax, 1
    སྤོ rdi, 1
    སྤོ rsi, msg
    སྤོ rdx, 13
    མ་ལག_འབོད་པ

    སྤོ rax, 60
    སྤོ rdi, 0
    མ་ལག_འབོད་པ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm bo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build bo programa.masm
```
