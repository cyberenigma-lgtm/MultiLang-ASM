# MultiLang-ASM: Manual de Instrucciones [FF]

**Idioma:** Fula / Fulfulde (`ff`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `darnu` | `hlt` |
| `diw` | `jmp` |
| `e` | `and` |
| `feere` | `xor` |
| `fus` | `nop` |
| `loow` | `push` |
| `ndartor` | `test` |
| `noddaango_laawol` | `syscall` |
| `noddu` | `call` |
| `rutto` | `ret` |
| `saɗɗin` | `mul` |
| `sendu` | `div` |
| `taareede` | `loop` |
| `taƴo` | `int` |
| `ustu` | `sub` |
| `walla` | `or` |
| `wonaa` | `not` |
| `wurtin` | `pop` |
| `yaggal` | `mov` |
| `yerondir` | `cmp` |
| `ɓeydu` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Fula / Fulfulde (ff)
section .text
global _start

_start:
    yaggal rax, 1
    yaggal rdi, 1
    yaggal rsi, msg
    yaggal rdx, 13
    noddaango_laawol

    yaggal rax, 60
    yaggal rdi, 0
    noddaango_laawol

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ff programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ff programa.masm
```
