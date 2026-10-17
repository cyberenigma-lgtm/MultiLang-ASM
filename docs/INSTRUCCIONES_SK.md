# MultiLang-ASM: Manual de Instrucciones [SK]

**Idioma:** Slovak / Slovenčina (`sk`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `a` | `and` |
| `ak_nerovne` | `jne` |
| `ak_rovne` | `je` |
| `alebo` | `or` |
| `cyklus` | `loop` |
| `exkluzivne` | `xor` |
| `nic` | `nop` |
| `nie` | `not` |
| `odpocitat` | `sub` |
| `porovnat` | `cmp` |
| `prerusenie` | `int` |
| `presunut` | `mov` |
| `pridat` | `add` |
| `skocit` | `jmp` |
| `systemove_volanie` | `syscall` |
| `testovat` | `test` |
| `vlozit` | `push` |
| `vratit` | `ret` |
| `vybrat` | `pop` |
| `vydelit` | `div` |
| `vymenit` | `xchg` |
| `vynasobit` | `mul` |
| `zastavit` | `hlt` |
| `zavolat` | `call` |
| `znizit` | `dec` |
| `zvysit` | `inc` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Slovak / Slovenčina (sk)
section .text
global _start

_start:
    presunut rax, 1
    presunut rdi, 1
    presunut rsi, msg
    presunut rdx, 13
    systemove_volanie

    presunut rax, 60
    presunut rdi, 0
    systemove_volanie

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sk programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sk programa.masm
```
