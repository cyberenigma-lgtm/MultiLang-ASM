# MultiLang-ASM: Manual de Instrucciones [TN]

**Idioma:** Setswana (`tn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `atafatsa` | `mul` |
| `bipitsa` | `call` |
| `boa` | `ret` |
| `ema` | `hlt` |
| `eseng` | `not` |
| `fokotsa` | `sub` |
| `ga_go_sepe` | `nop` |
| `kgaoganya` | `div` |
| `kgethegileng` | `xor` |
| `kgoreletso` | `int` |
| `kgotsa` | `or` |
| `le` | `and` |
| `lekeletsa` | `test` |
| `ntsha` | `pop` |
| `oketsa` | `add` |
| `pitso_ya_tsamaiso` | `syscall` |
| `tidiko` | `loop` |
| `tlola` | `jmp` |
| `tsamaisa` | `mov` |
| `tsenya` | `push` |
| `tshwantshanya` | `cmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Setswana (tn)
section .text
global _start

_start:
    tsamaisa rax, 1
    tsamaisa rdi, 1
    tsamaisa rsi, msg
    tsamaisa rdx, 13
    pitso_ya_tsamaiso

    tsamaisa rax, 60
    tsamaisa rdi, 0
    pitso_ya_tsamaiso

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tn programa.masm
```
