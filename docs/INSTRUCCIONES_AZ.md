# MultiLang-ASM: Manual de Instrucciones [AZ]

**Idioma:** Azerbaijani / Azərbaycan (`az`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `böl` | `div` |
| `dayan` | `hlt` |
| `deyil` | `not` |
| `dövr` | `loop` |
| `heç_nə` | `nop` |
| `itələ` | `push` |
| `köçür` | `mov` |
| `kəsilmə` | `int` |
| `müqayisə_et` | `cmp` |
| `qayıt` | `ret` |
| `sistem_zəngi` | `syscall` |
| `tullan` | `jmp` |
| `vur` | `mul` |
| `və` | `and` |
| `və_ya` | `or` |
| `xüsusi` | `xor` |
| `yoxla` | `test` |
| `çağır` | `call` |
| `çıx` | `sub` |
| `çıxart` | `pop` |
| `əlavə_et` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Azerbaijani / Azərbaycan (az)
section .text
global _start

_start:
    köçür rax, 1
    köçür rdi, 1
    köçür rsi, msg
    köçür rdx, 13
    sistem_zəngi

    köçür rax, 60
    köçür rdi, 0
    sistem_zəngi

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm az programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build az programa.masm
```
