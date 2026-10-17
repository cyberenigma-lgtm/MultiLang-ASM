# MultiLang-ASM: Manual de Instrucciones [HI]

**Idioma:** Hindi / हिन्दी (`hi`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 39  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `kudo` | `jmp` |
| `pariksha` | `test` |
| `pata_load` | `lea` |
| `कुछ_नहीं` | `nop` |
| `कूदें` | `jmp` |
| `कॉल` | `call` |
| `गुणा` | `mul` |
| `घटाएं` | `sub` |
| `घटाएं_एक` | `dec` |
| `जोड़ें` | `add` |
| `तुलना` | `cmp` |
| `दबाएं` | `push` |
| `दोहराएं` | `rep` |
| `निकालें` | `pop` |
| `पता_लोड` | `lea` |
| `परीक्षण` | `test` |
| `फ्लैग_दबाएं` | `pushf` |
| `फ्लैग_निकालें` | `popf` |
| `बढ़ाएं` | `inc` |
| `बदलें` | `xchg` |
| `बाइट_को_वर्ड` | `cbw` |
| `बाइट_लोड` | `lodsb` |
| `बाइट_संग्रहित` | `stosb` |
| `बाइट_स्थानांतरित` | `movsb` |
| `यदि_छोटा` | `jl` |
| `यदि_नहीं_बराबर` | `jne` |
| `यदि_बड़ा` | `jg` |
| `यदि_बराबर` | `je` |
| `यदि_शून्य` | `jz` |
| `यदि_शून्य_लूप` | `loopz` |
| `रुकें` | `hlt` |
| `लूप` | `loop` |
| `वर्ड_को_डबल` | `cwd` |
| `वापस` | `ret` |
| `विभाजन` | `div` |
| `व्यवधान` | `int` |
| `सिस्टम_कॉल` | `syscall` |
| `सिस्टम_वापसी` | `sysret` |
| `स्थानांतरित` | `mov` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hindi / हिन्दी (hi)
section .text
global _start

_start:
    स्थानांतरित rax, 1
    स्थानांतरित rdi, 1
    स्थानांतरित rsi, msg
    स्थानांतरित rdx, 13
    सिस्टम_कॉल

    स्थानांतरित rax, 60
    स्थानांतरित rdi, 0
    सिस्टम_कॉल

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm hi programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build hi programa.masm
```
