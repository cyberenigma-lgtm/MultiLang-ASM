# MultiLang-ASM: Manual de Instrucciones [NAV]

**Idioma:** Navajo / Diné bizaad (`nav`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ałhąąh` | `cmp` |
| `ałtsʼá` | `int` |
| `ałtsʼą́ą́h` | `div` |
| `bee_bikʼi` | `add` |
| `beesh_bee_haneʼ` | `syscall` |
| `biih_yíníł` | `push` |
| `bąąh_chʼéldzid` | `sub` |
| `chʼéníł` | `pop` |
| `dah_naatłʼo` | `jmp` |
| `dooda` | `not` |
| `dóó` | `and` |
| `nádleeh` | `ret` |
| `názbas` | `loop` |
| `néaltsos` | `test` |
| `néeltʼeʼ` | `mul` |
| `tʼáá_sahee` | `xor` |
| `tʼóó_haziʼ` | `hlt` |
| `yízhí` | `call` |
| `yíłtsood` | `mov` |
| `ádingo` | `nop` |
| `éí_doodaiiʼ` | `or` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Navajo / Diné bizaad (nav)
section .text
global _start

_start:
    yíłtsood rax, 1
    yíłtsood rdi, 1
    yíłtsood rsi, msg
    yíłtsood rdx, 13
    beesh_bee_haneʼ

    yíłtsood rax, 60
    yíłtsood rdi, 0
    beesh_bee_haneʼ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm nav programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build nav programa.masm
```
