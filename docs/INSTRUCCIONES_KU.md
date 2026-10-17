# MultiLang-ASM: Manual de Instrucciones [KU]

**Idioma:** Kurdish / Kurdî (`ku`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `an` | `or` |
| `bang_bike` | `call` |
| `banga_pergalê` | `syscall` |
| `berawird_bike` | `cmp` |
| `biceribîne` | `test` |
| `bipirse` | `jmp` |
| `bisekine` | `hlt` |
| `caran` | `mul` |
| `derxe` | `sub` |
| `deyne` | `push` |
| `navbir` | `int` |
| `ne` | `not` |
| `parve_bike` | `div` |
| `rake` | `pop` |
| `taybet` | `xor` |
| `tiştek_tune` | `nop` |
| `vegere` | `ret` |
| `veguhezîne` | `mov` |
| `zivirandin` | `loop` |
| `zêde_bike` | `add` |
| `û` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kurdish / Kurdî (ku)
section .text
global _start

_start:
    veguhezîne rax, 1
    veguhezîne rdi, 1
    veguhezîne rsi, msg
    veguhezîne rdx, 13
    banga_pergalê

    veguhezîne rax, 60
    veguhezîne rdi, 0
    banga_pergalê

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ku programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ku programa.masm
```
