# MultiLang-ASM: Ol Toktok (Tok Pisin - tpi)

Welkam long sapot bilong Tok Pisin long MultiLang-ASM.

## 🛠 Ol Bikpela Komand

| MultiLang-ASM | NASM (x86_64) | Mining |
| :--- | :--- | :--- |
| `muvim` | `mov` | Muvim data |
| `plusim` | `add` | Putim moa |
| `minusim` | `sub` | Tekewe |
| `sekim` | `cmp` | Sekim tupela samting |
| `kalap` | `jmp` | Kalap i go long narapela sait |
| `singaut` | `call` | Singautim wok |
| `go_bek` | `ret` | Go bek long wok |
| `stopim` | `int` | Stopim wok |
| `singaut_sistem` | `syscall` | Singautim sistem |

## 📝 Wanpela Eksampl

```asm
; Halo olgeta long Tok Pisin
sekson .data
    toktok: db "Halo olgeta!", 10

sekson .text
    global _start

_start:
    muvim rax, 1          ; syscall: write
    muvim rdi, 1          ; fd: stdout
    muvim rsi, toktok     ; buffer
    muvim rdx, 13         ; length
    singaut_sistem

    muvim rax, 60         ; syscall: exit
    muvim rdi, 0          ; exit code
    singaut_sistem
```

## 🚀 Olsem wanem long yusim

```bash
python mlasm.py tpi program.masm
```
