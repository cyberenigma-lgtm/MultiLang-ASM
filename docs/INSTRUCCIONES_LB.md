# MultiLang-ASM: Manual de Instrucciones [LB]

**Idioma:** Luxembourgish / Lëtzebuergesch (`lb`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `an` | `and` |
| `beweegen` | `mov` |
| `deelen` | `div` |
| `dobaidinn` | `add` |
| `drécken` | `push` |
| `exklusiv` | `xor` |
| `huelen` | `pop` |
| `multiplizéieren` | `mul` |
| `net` | `not` |
| `näischt` | `nop` |
| `oder` | `or` |
| `ofzéien` | `sub` |
| `ruffen` | `call` |
| `schläif` | `loop` |
| `sprangen` | `jmp` |
| `stoppen` | `hlt` |
| `systemruff` | `syscall` |
| `testen` | `test` |
| `vergläichen` | `cmp` |
| `zréckgoen` | `ret` |
| `ënnerbriechung` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Luxembourgish / Lëtzebuergesch (lb)
section .text
global _start

_start:
    beweegen rax, 1
    beweegen rdi, 1
    beweegen rsi, msg
    beweegen rdx, 13
    systemruff

    beweegen rax, 60
    beweegen rdi, 0
    systemruff

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm lb programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build lb programa.masm
```
