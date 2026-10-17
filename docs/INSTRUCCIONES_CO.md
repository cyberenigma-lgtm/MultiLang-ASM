# MultiLang-ASM: Manual de Instrucciones [CO]

**Idioma:** Corsican / Corsu (`co`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aghjunghje` | `add` |
| `caccià` | `pop` |
| `chjama_sistema` | `syscall` |
| `chjamà` | `call` |
| `esclusivu` | `xor` |
| `fermà` | `hlt` |
| `giru` | `loop` |
| `interruzzione` | `int` |
| `micca` | `not` |
| `multiplicà` | `mul` |
| `nulla` | `nop` |
| `o` | `or` |
| `paragunà` | `cmp` |
| `pruvà` | `test` |
| `riturnà` | `ret` |
| `saltà` | `jmp` |
| `sparte` | `div` |
| `spinghje` | `push` |
| `spustà` | `mov` |
| `suttrae` | `sub` |
| `è` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Corsican / Corsu (co)
section .text
global _start

_start:
    spustà rax, 1
    spustà rdi, 1
    spustà rsi, msg
    spustà rdx, 13
    chjama_sistema

    spustà rax, 60
    spustà rdi, 0
    chjama_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm co programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build co programa.masm
```
