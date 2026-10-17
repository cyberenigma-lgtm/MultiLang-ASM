# MultiLang-ASM: Manual de Instrucciones [PA]

**Idioma:** Punjabi / ਪੰਜਾਬੀ (`pa`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ਅਤੇ` | `and` |
| `ਕੁਝ_ਨਹੀਂ` | `nop` |
| `ਕੱਢੋ` | `pop` |
| `ਗੁਣਾ` | `mul` |
| `ਘਟਾਓ` | `sub` |
| `ਚੱਕਰ` | `loop` |
| `ਛਾਲ` | `jmp` |
| `ਜਾਂ` | `or` |
| `ਜੋੜੋ` | `add` |
| `ਤੁਲਨਾ` | `cmp` |
| `ਨਹੀਂ` | `not` |
| `ਪਰਖ` | `test` |
| `ਪਾਓ` | `push` |
| `ਬੁਲਾਓ` | `call` |
| `ਭੇਜੋ` | `mov` |
| `ਰੁਕੋ` | `hlt` |
| `ਰੋਕ` | `int` |
| `ਵਾਪਸ` | `ret` |
| `ਵਿਲੱਖਣ` | `xor` |
| `ਵੰਡੋ` | `div` |
| `ਸਿਸਟਮ_ਕਾਲ` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Punjabi / ਪੰਜਾਬੀ (pa)
section .text
global _start

_start:
    ਭੇਜੋ rax, 1
    ਭੇਜੋ rdi, 1
    ਭੇਜੋ rsi, msg
    ਭੇਜੋ rdx, 13
    ਸਿਸਟਮ_ਕਾਲ

    ਭੇਜੋ rax, 60
    ਭੇਜੋ rdi, 0
    ਸਿਸਟਮ_ਕਾਲ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm pa programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build pa programa.masm
```
