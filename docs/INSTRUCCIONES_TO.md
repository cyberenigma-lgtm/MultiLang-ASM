# MultiLang-ASM: Manual de Instrucciones [TO]

**Idioma:** Tongan / Lea Faka-Tonga (`to`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `fakafanongo` | `cmp` |
| `fakahohaʻa` | `int` |
| `foki` | `ret` |
| `fusi` | `pop` |
| `hala_ha_meʻa` | `nop` |
| `hiki` | `mov` |
| `hopohopo` | `jmp` |
| `ikai` | `not` |
| `liungofua` | `mul` |
| `makehe` | `xor` |
| `pe` | `or` |
| `pea` | `and` |
| `siviʻi` | `test` |
| `takai` | `loop` |
| `tanaki` | `add` |
| `taʻofi` | `hlt` |
| `teke` | `push` |
| `toʻo` | `sub` |
| `ui` | `call` |
| `ui_fakatoka` | `syscall` |
| `vahevahe` | `div` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tongan / Lea Faka-Tonga (to)
section .text
global _start

_start:
    hiki rax, 1
    hiki rdi, 1
    hiki rsi, msg
    hiki rdx, 13
    ui_fakatoka

    hiki rax, 60
    hiki rdi, 0
    ui_fakatoka

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm to programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build to programa.masm
```
