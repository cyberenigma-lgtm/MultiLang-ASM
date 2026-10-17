# MultiLang-ASM: Manual de Instrucciones [LV]

**Idioma:** Latvian / Latviešu (`lv`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `apturet` | `hlt` |
| `atgriezt` | `ret` |
| `atnemt` | `sub` |
| `cikls` | `loop` |
| `dalit` | `div` |
| `iespiest` | `push` |
| `iznemt` | `pop` |
| `izslegts` | `xor` |
| `lekt` | `jmp` |
| `ne` | `not` |
| `nekas` | `nop` |
| `parbaudit` | `test` |
| `partraukums` | `int` |
| `parvietot` | `mov` |
| `pieskaitit` | `add` |
| `reizinat` | `mul` |
| `salidzinat` | `cmp` |
| `saukt` | `call` |
| `sistemas_izsaukums` | `syscall` |
| `un` | `and` |
| `vai` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Latvian / Latviešu (lv)
section .text
global _start

_start:
    parvietot rax, 1
    parvietot rdi, 1
    parvietot rsi, msg
    parvietot rdx, 13
    sistemas_izsaukums

    parvietot rax, 60
    parvietot rdi, 0
    sistemas_izsaukums

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm lv programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build lv programa.masm
```
