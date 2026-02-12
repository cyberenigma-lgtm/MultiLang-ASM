# MultiLang-ASM: Mga Instruksyon (Tagalog/Filipino - tl)

Maligayang pagdating sa suporta para sa Tagalog ng MultiLang-ASM.

## 🛠 Mga Pangunahing Command

| MultiLang-ASM | NASM (x86_64) | Paglalarawan |
| :--- | :--- | :--- |
| `ilipat` | `mov` | Ilipat ang datos |
| `idagdag` | `add` | Magdagdag ng halaga |
| `ibawas` | `sub` | Magbawas ng halaga |
| `ihambing` | `cmp` | Ihambing ang mga halaga |
| `tumalon` | `jmp` | Tumalon sa address |
| `itawag` | `call` | Tumawag ng function |
| `bumalik` | `ret` | Bumalik mula sa function |
| `abala` | `int` | Software interrupt |
| `tawag_system` | `syscall` | System call |

## 📝 Halimbawa ng Code

```asm
; Hello World sa Tagalog
seksyon .data
    mensahe: db "Kumusta mundo!", 10

seksyon .text
    global _start

_start:
    ilipat rax, 1          ; syscall: write
    ilipat rdi, 1          ; fd: stdout
    ilipat rsi, mensahe    ; buffer
    ilipat rdx, 15         ; length
    tawag_system

    ilipat rax, 60         ; syscall: exit
    ilipat rdi, 0          ; exit code
    tawag_system
```

## 🚀 Paggamit

```bash
python mlasm.py tl programa.masm
```
