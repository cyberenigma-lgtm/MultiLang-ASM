# MultiLang-ASM: Manual de Instrucciones [HAW]

**Idioma:** Hawaiian / ʻŌlelo Hawaiʻi (`haw`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `a_i_ʻole` | `or` |
| `a_me` | `and` |
| `hoʻi` | `ret` |
| `hoʻohui` | `add` |
| `hoʻohālike` | `cmp` |
| `hoʻomaha` | `hlt` |
| `hoʻomāhuahua` | `mul` |
| `hoʻopilikia` | `int` |
| `huki` | `pop` |
| `hōʻoia` | `test` |
| `kāhea` | `call` |
| `kāhea_ʻōnaehana` | `syscall` |
| `kāpae` | `sub` |
| `kūʻokoʻa` | `xor` |
| `lele` | `jmp` |
| `luka` | `loop` |
| `māhele` | `div` |
| `neʻe` | `mov` |
| `pahu` | `push` |
| `ʻaʻohe_mea` | `nop` |
| `ʻaʻole` | `not` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hawaiian / ʻŌlelo Hawaiʻi (haw)
section .text
global _start

_start:
    neʻe rax, 1
    neʻe rdi, 1
    neʻe rsi, msg
    neʻe rdx, 13
    kāhea_ʻōnaehana

    neʻe rax, 60
    neʻe rdi, 0
    kāhea_ʻōnaehana

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm haw programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build haw programa.masm
```
