# MultiLang-ASM: Manual de Instrucciones [SN]

**Idioma:** Shona / ChiShona (`sn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `buda` | `pop` |
| `bvisa` | `sub` |
| `chikanganiso` | `int` |
| `daidza` | `call` |
| `denderedzwa` | `loop` |
| `dzoka` | `ret` |
| `edza` | `test` |
| `enzanisa` | `cmp` |
| `fambisa` | `mov` |
| `gova` | `div` |
| `hapana` | `nop` |
| `kana` | `or` |
| `kudana_sisitimu` | `syscall` |
| `kwete` | `not` |
| `mira` | `hlt` |
| `oga` | `xor` |
| `pinda` | `push` |
| `svetuka` | `jmp` |
| `uye` | `and` |
| `wanza` | `mul` |
| `wedzera` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Shona / ChiShona (sn)
section .text
global _start

_start:
    fambisa rax, 1
    fambisa rdi, 1
    fambisa rsi, msg
    fambisa rdx, 13
    kudana_sisitimu

    fambisa rax, 60
    fambisa rdi, 0
    kudana_sisitimu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sn programa.masm
```
