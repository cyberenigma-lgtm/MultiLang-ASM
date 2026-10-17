# MultiLang-ASM: Manual de Instrucciones [GD]

**Idioma:** Scottish Gaelic / Gàidhlig (`gd`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `agus` | `and` |
| `as-aithneach` | `xor` |
| `briseadh` | `int` |
| `cha` | `not` |
| `coimeas` | `cmp` |
| `cuir_ris` | `add` |
| `dad` | `nop` |
| `deuchainn` | `test` |
| `gairm` | `call` |
| `gairm_siostam` | `syscall` |
| `gluais` | `mov` |
| `iomadaich` | `mul` |
| `leum` | `jmp` |
| `lùb` | `loop` |
| `no` | `or` |
| `put` | `push` |
| `roinn` | `div` |
| `stad` | `hlt` |
| `tarraing` | `pop` |
| `till` | `ret` |
| `toir_air_falbh` | `sub` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Scottish Gaelic / Gàidhlig (gd)
section .text
global _start

_start:
    gluais rax, 1
    gluais rdi, 1
    gluais rsi, msg
    gluais rdx, 13
    gairm_siostam

    gluais rax, 60
    gluais rdi, 0
    gairm_siostam

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm gd programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build gd programa.masm
```
