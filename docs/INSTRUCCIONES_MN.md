# MultiLang-ASM: Manual de Instrucciones [MN]

**Idioma:** Mongolian / Монгол (`mn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ба` | `and` |
| `биш` | `not` |
| `буцах` | `ret` |
| `давталт` | `loop` |
| `дуудах` | `call` |
| `зогс` | `hlt` |
| `зөөх` | `mov` |
| `нэмэх` | `add` |
| `онцгой` | `xor` |
| `системийн_дуудалт` | `syscall` |
| `тасалдал` | `int` |
| `татах` | `pop` |
| `түлхэх` | `push` |
| `харьцуулах` | `cmp` |
| `хасах` | `sub` |
| `хуваах` | `div` |
| `шалгах` | `test` |
| `эсвэл` | `or` |
| `юу_ч_биш` | `nop` |
| `үржүүлэх` | `mul` |
| `үсрэх` | `jmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Mongolian / Монгол (mn)
section .text
global _start

_start:
    зөөх rax, 1
    зөөх rdi, 1
    зөөх rsi, msg
    зөөх rdx, 13
    системийн_дуудалт

    зөөх rax, 60
    зөөх rdi, 0
    системийн_дуудалт

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mn programa.masm
```
