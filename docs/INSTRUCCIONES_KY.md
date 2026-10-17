# MultiLang-ASM: Manual de Instrucciones [KY]

**Idioma:** Kyrgyz / Кыргызча (`ky`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `алуу` | `pop` |
| `бөлүү` | `div` |
| `жана` | `and` |
| `же` | `or` |
| `жылдыруу` | `mov` |
| `кайтуу` | `ret` |
| `кемитүү` | `sub` |
| `киргизүү` | `push` |
| `кошуу` | `add` |
| `көбөйтүү` | `mul` |
| `салыштыруу` | `cmp` |
| `секирүү` | `jmp` |
| `системалык_чакыруу` | `syscall` |
| `сыноо` | `test` |
| `токто` | `hlt` |
| `цикл` | `loop` |
| `чакыруу` | `call` |
| `эмес` | `not` |
| `эч_нерсе` | `nop` |
| `үзгүлтүк` | `int` |
| `өзгөчө` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Kyrgyz / Кыргызча (ky)
section .text
global _start

_start:
    жылдыруу rax, 1
    жылдыруу rdi, 1
    жылдыруу rsi, msg
    жылдыруу rdx, 13
    системалык_чакыруу

    жылдыруу rax, 60
    жылдыруу rdi, 0
    системалык_чакыруу

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ky programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ky programa.masm
```
