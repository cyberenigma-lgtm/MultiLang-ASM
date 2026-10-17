# MultiLang-ASM: Manual de Instrucciones [NE]

**Idioma:** Nepali / नेपाली (`ne`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `अवरोध` | `int` |
| `उफ्रनुहोस्` | `jmp` |
| `केही_छैन` | `nop` |
| `गुणन_गर्नुहोस्` | `mul` |
| `घटाउनुहोस्` | `sub` |
| `जाँच्नुहोस्` | `test` |
| `जोड्नुहोस्` | `add` |
| `तुलना_गर्नुहोस्` | `cmp` |
| `निकाल्नुहोस्` | `pop` |
| `प्रणाली_कल` | `syscall` |
| `फर्कनुहोस्` | `ret` |
| `बोलाउनुहोस्` | `call` |
| `भाग_गर्नुहोस्` | `div` |
| `र` | `and` |
| `राख्नुहोस्` | `push` |
| `रोक्नुहोस्` | `hlt` |
| `लुप` | `loop` |
| `वा` | `or` |
| `विशेष` | `xor` |
| `सार्नुहोस्` | `mov` |
| `होइन` | `not` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Nepali / नेपाली (ne)
section .text
global _start

_start:
    सार्नुहोस् rax, 1
    सार्नुहोस् rdi, 1
    सार्नुहोस् rsi, msg
    सार्नुहोस् rdx, 13
    प्रणाली_कल

    सार्नुहोस् rax, 60
    सार्नुहोस् rdi, 0
    प्रणाली_कल

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ne programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ne programa.masm
```
