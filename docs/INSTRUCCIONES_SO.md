# MultiLang-ASM: Manual de Instrucciones [SO]

**Idioma:** Somali / Soomaali (`so`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ama` | `or` |
| `bood` | `jmp` |
| `geli` | `push` |
| `isbarbardhig` | `cmp` |
| `iyo` | `and` |
| `joogso` | `hlt` |
| `ka_jar` | `sub` |
| `kala_goys` | `int` |
| `keliya` | `xor` |
| `ku_dar` | `add` |
| `ku_dhufo` | `mul` |
| `maaha` | `not` |
| `rari` | `mov` |
| `saar` | `pop` |
| `soo_noqo` | `ret` |
| `tijaabi` | `test` |
| `u_qaybi` | `div` |
| `wac` | `call` |
| `wareeg` | `loop` |
| `waxba` | `nop` |
| `yeeritaanka_nidaamka` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Somali / Soomaali (so)
section .text
global _start

_start:
    rari rax, 1
    rari rdi, 1
    rari rsi, msg
    rari rdx, 13
    yeeritaanka_nidaamka

    rari rax, 60
    rari rdi, 0
    yeeritaanka_nidaamka

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm so programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build so programa.masm
```
