# MultiLang-ASM: Manual de Instrucciones [OC]

**Idioma:** Occitan / Lenga d'òc (`oc`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `apondre` | `add` |
| `arrestar` | `hlt` |
| `bocla` | `loop` |
| `comparar` | `cmp` |
| `desplaçar` | `mov` |
| `devesir` | `div` |
| `e` | `and` |
| `empenher` | `push` |
| `ensajar` | `test` |
| `exclusiu` | `xor` |
| `interrupcion` | `int` |
| `multiplicar` | `mul` |
| `o` | `or` |
| `pas` | `not` |
| `ren` | `nop` |
| `retornar` | `ret` |
| `sautar` | `jmp` |
| `sonada_sistema` | `syscall` |
| `sonar` | `call` |
| `sustraire` | `sub` |
| `traire` | `pop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Occitan / Lenga d'òc (oc)
section .text
global _start

_start:
    desplaçar rax, 1
    desplaçar rdi, 1
    desplaçar rsi, msg
    desplaçar rdx, 13
    sonada_sistema

    desplaçar rax, 60
    desplaçar rdi, 0
    sonada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm oc programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build oc programa.masm
```
