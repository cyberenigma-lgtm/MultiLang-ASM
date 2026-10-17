# MultiLang-ASM: Manual de Instrucciones [IT]

**Idioma:** Italian / Italiano (`it`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `carica_byte` | `lodsb` |
| `caricare_effettivo` | `lea` |
| `chiamare` | `call` |
| `chiamata_sistema` | `syscall` |
| `ciclo` | `loop` |
| `ciclo_se_zero` | `loopz` |
| `confrontare` | `cmp` |
| `conv_byte_parola` | `cbw` |
| `conv_doppio_quad` | `cdq` |
| `conv_parola_doppio` | `cwd` |
| `copiare` | `mov` |
| `decrementare` | `dec` |
| `dividere` | `div` |
| `estendere_segno` | `movsx` |
| `estendere_zero` | `movzx` |
| `ferma` | `hlt` |
| `incrementare` | `inc` |
| `interruzione` | `int` |
| `mettere` | `push` |
| `mettere_flag` | `pushf` |
| `moltiplicare` | `mul` |
| `muovi_byte` | `movsb` |
| `niente` | `nop` |
| `ripeti` | `rep` |
| `ritornare` | `ret` |
| `ritorno_sistema` | `sysret` |
| `saltare` | `jmp` |
| `salva_byte` | `stosb` |
| `scambiare` | `xchg` |
| `se_maggiore` | `jg` |
| `se_minore` | `jl` |
| `se_non_uguale` | `jne` |
| `se_uguale` | `je` |
| `se_zero` | `jz` |
| `sommare` | `add` |
| `sottrarre` | `sub` |
| `spostare` | `mov` |
| `testare` | `test` |
| `togliere` | `pop` |
| `togliere_flag` | `popf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Italian / Italiano (it)
section .text
global _start

_start:
    spostare rax, 1
    spostare rdi, 1
    spostare rsi, msg
    spostare rdx, 13
    chiamata_sistema

    spostare rax, 60
    spostare rdi, 0
    chiamata_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm it programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build it programa.masm
```
