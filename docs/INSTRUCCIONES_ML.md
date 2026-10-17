# MultiLang-ASM: Manual de Instrucciones [ML]

**Idioma:** Malayalam / മലയാളം (`ml`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `അല്ല` | `not` |
| `അല്ലെങ്കിൽ` | `or` |
| `എടുക്കുക` | `pop` |
| `ഒന്നുമില്ല` | `nop` |
| `കുറയ്ക്കുക` | `sub` |
| `കൂടാതെ` | `and` |
| `കൂട്ടുക` | `add` |
| `ഗുണിക്കുക` | `mul` |
| `ചക്രം` | `loop` |
| `ചാടുക` | `jmp` |
| `തടസ്സം` | `int` |
| `താരതമ്യം` | `cmp` |
| `തിരികെ` | `ret` |
| `നിക്ഷേപിക്കുക` | `push` |
| `നിർത്തുക` | `hlt` |
| `നീക്കുക` | `mov` |
| `പരിശോധിക്കുക` | `test` |
| `പ്രത്യേക` | `xor` |
| `വിളിക്കുക` | `call` |
| `സിസ്റ്റം_കോൾ` | `syscall` |
| `ഹരിക്കുക` | `div` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Malayalam / മലയാളം (ml)
section .text
global _start

_start:
    നീക്കുക rax, 1
    നീക്കുക rdi, 1
    നീക്കുക rsi, msg
    നീക്കുക rdx, 13
    സിസ്റ്റം_കോൾ

    നീക്കുക rax, 60
    നീക്കുക rdi, 0
    സിസ്റ്റം_കോൾ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ml programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ml programa.masm
```
