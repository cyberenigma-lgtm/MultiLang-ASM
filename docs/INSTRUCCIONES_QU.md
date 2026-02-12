# MultiLang-ASM: Kamachiykuna (Quechua - qu)

Allin hamuy MultiLang-ASM yanapayman Quechua simipi.

## 🛠 Sananchakuna

| MultiLang-ASM | NASM (x86_64) | Imapaq |
| :--- | :--- | :--- |
| `astay` | `mov` | Datoskuna astay |
| `yapay` | `add` | Yupaykunay yapay |
| `qichuy` | `sub` | Yupaykunay qichuy |
| `tupachiy` | `cmp` | Yupaykunay tupachiy |
| `paway` | `jmp` | Huk kitiman paway |
| `waqyay` | `call` | Ruwayta waqyay |
| `kutimuy` | `ret` | Ruwaymanta kutimuy |
| `samachiy` | `int` | Samachiy |
| `llanu_waqyay` | `syscall` | Llanu waqyay |

## 📝 Ejemplo Codi

```asm
; Napaykullayki Teqsimuyu Quechuapi
t'aqa .data
    napay: db "Napaykullayki Teqsimuyu!", 10

t'aqa .text
    global _start

_start:
    astay rax, 1          ; syscall: write
    astay rdi, 1          ; fd: stdout
    astay rsi, napay      ; buffer
    astay rdx, 25         ; length
    llanu_waqyay

    astay rax, 60         ; syscall: exit
    astay rdi, 0          ; error yupay
    llanu_waqyay
```

## 🚀 Imayna Ruway

```bash
python mlasm.py qu programa.masm
```
