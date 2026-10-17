# MultiLang-ASM: Manual de Instrucciones [TA]

**Idioma:** Tamil / தமிழ் (`ta`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `அதிகரி` | `inc` |
| `அமைப்பு_அழைப்பு` | `syscall` |
| `அமைப்பு_திரும்பு` | `sysret` |
| `அழை` | `call` |
| `இரண்டு_நான்கு` | `cdq` |
| `எடு` | `pop` |
| `ஒன்றுமில்லை` | `nop` |
| `ஒப்பிடு` | `cmp` |
| `கழி` | `sub` |
| `குறி_விரிவாக்கம்` | `movsx` |
| `குறை` | `dec` |
| `கூட்டு` | `add` |
| `கொடி_எடு` | `popf` |
| `கொடி_தள்ளு` | `pushf` |
| `சமமில்லை_என்றால்` | `jne` |
| `சமம்_என்றால்` | `je` |
| `சிறிது_என்றால்` | `jl` |
| `சுழற்சி` | `loop` |
| `சோதி` | `test` |
| `தடை` | `int` |
| `தள்ளு` | `push` |
| `தாவு` | `jmp` |
| `திரும்பு` | `ret` |
| `நகர்த்து` | `mov` |
| `நிறுத்து` | `hlt` |
| `பூஜ்ஜிய_விரிவாக்கம்` | `movzx` |
| `பூஜ்ஜியம்_என்றால்` | `jz` |
| `பூஜ்ஜியம்_சுழற்சி` | `loopz` |
| `பெரிது_என்றால்` | `jg` |
| `பெருக்கு` | `mul` |
| `பைட்_ஏற்று` | `lodsb` |
| `பைட்_சேமி` | `stosb` |
| `பைட்_நகர்த்து` | `movsb` |
| `பைட்_வார்த்தை` | `cbw` |
| `மறு` | `neg` |
| `மாற்று` | `xchg` |
| `மீண்டும்_செய்` | `rep` |
| `முகவரி_ஏற்று` | `lea` |
| `வகு` | `div` |
| `வார்த்தை_இரண்டு` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tamil / தமிழ் (ta)
section .text
global _start

_start:
    நகர்த்து rax, 1
    நகர்த்து rdi, 1
    நகர்த்து rsi, msg
    நகர்த்து rdx, 13
    அமைப்பு_அழைப்பு

    நகர்த்து rax, 60
    நகர்த்து rdi, 0
    அமைப்பு_அழைப்பு

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ta programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ta programa.masm
```
