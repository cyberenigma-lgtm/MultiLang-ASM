# MultiLang-ASM: Manual de Instrucciones [KM]

**Idioma:** Khmer / ភាសាខ្មែរ (`km`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ការហៅប្រព័ន្ធ` | `syscall` |
| `គុណ` | `mul` |
| `គ្មានអ្វី` | `nop` |
| `ចែក` | `div` |
| `ដក` | `sub` |
| `ដកចេញ` | `pop` |
| `ត្រឡប់` | `ret` |
| `និង` | `and` |
| `បញ្ឈប់` | `hlt` |
| `បូក` | `add` |
| `ប្រៀបធៀប` | `cmp` |
| `ផ្ដាច់មុខ` | `xor` |
| `មិន` | `not` |
| `រង្វិលជុំ` | `loop` |
| `រុញ` | `push` |
| `រំកិល` | `mov` |
| `រំខាន` | `int` |
| `លោត` | `jmp` |
| `សាកល្បង` | `test` |
| `ហៅ` | `call` |
| `ឬ` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Khmer / ភាសាខ្មែរ (km)
section .text
global _start

_start:
    រំកិល rax, 1
    រំកិល rdi, 1
    រំកិល rsi, msg
    រំកិល rdx, 13
    ការហៅប្រព័ន្ធ

    រំកិល rax, 60
    រំកិល rdi, 0
    ការហៅប្រព័ន្ធ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm km programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build km programa.masm
```
