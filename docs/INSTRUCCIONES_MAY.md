# MultiLang-ASM: Áantaj (Maya - may)

Tuláakal áantaj ti'al MultiLang-ASM ich Maaya T'aan.

## 🛠 Núukulo'ob

| MultiLang-ASM | NASM (x86_64) | Ba'ax ku ya'alik |
| :--- | :--- | :--- |
| `túuxt` | `mov` | Peeksaj raraunga |
| `ts'áaj` | `add` | Ts'áaj xook |
| `túul` | `sub` | Túul xook |
| `ket` | `cmp` | Ket xook |
| `si'it` | `jmp` | Si'it |
| `t'an` | `call` | T'an |
| `suut` | `ret` | Suut |
| `jet'` | `int` | Jet' |
| `t'an_sistema` | `syscall` | T'an sistema |

## 📝 Adibidea

```asm
; Ki'imak óolal yóok'ol kaab ich Maaya
lohko .data
    kiimak: db "Kiimak oolal yookol kaab!", 10

lohko .text
    global _start

_start:
    túuxt rax, 1          ; syscall: write
    túuxt rdi, 1          ; fd: stdout
    túuxt rsi, kiimak     ; buffer
    túuxt rdx, 26         ; length
    t'an_sistema

    túuxt rax, 60         ; syscall: exit
    túuxt rdi, 0          ; exit code
    t'an_sistema
```

## 🚀 Úsáid

```bash
python mlasm.py may programa.masm
```
