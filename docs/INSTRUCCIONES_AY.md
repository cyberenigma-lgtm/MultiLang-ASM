# MultiLang-ASM: Kamachinaka (Aymara - ay)

Uñachayañataki MultiLang-ASM Aymara aruna.

## 🛠 Kamachinaka

| MultiLang-ASM | NASM (x86_64) | Kuna |
| :--- | :--- | :--- |
| `kuna` | `mov` | Datoskuna kuna |
| `yapaña` | `add` | Jakhuña yapaña |
| `apaqaña` | `sub` | Jakhuña apaqaña |
| `kipkaña` | `cmp` | Jakhuña kipkaña |
| `t'it'iña` | `jmp` | T'it'iña |
| `jawsaña` | `call` | Jawsaña |
| `kutiña` | `ret` | Kutiña |
| `samaña` | `int` | Samaña |
| `sistema_jawsaña`| `syscall` | Sistema jawsaña |

## 📝 Ejemplo Code

```asm
; Kamisaraki uraqpacha Aymarana
t'aqa .data
    kamisaraki: db "Kamisaraki uraqpacha!", 10

t'aqa .text
    global _start

_start:
    kuna rax, 1          ; syscall: write
    kuna rdi, 1          ; fd: stdout
    kuna rsi, kamisaraki ; buffer
    kuna rdx, 22         ; length
    sistema_jawsaña

    kuna rax, 60         ; syscall: exit
    kuna rdi, 0          ; jani error
    sistema_jawsaña
```

## 🚀 Luraña

```bash
python mlasm.py ay programa.masm
```
