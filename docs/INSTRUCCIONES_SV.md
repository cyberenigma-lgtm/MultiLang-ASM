# MultiLang-ASM: Instruktioner (Svenska - sv)

Välkommen till det svenska stödet för MultiLang-ASM.

## 🛠 Grundläggande kommandon

| MultiLang-ASM | NASM (x86_64) | Beskrivning |
| :--- | :--- | :--- |
| `flytta` | `mov` | Flytta data |
| `addera` | `add` | Addera |
| `subtrahera` | `sub` | Subtrahera |
| `jamfor` | `cmp` | Jämför värden |
| `hoppa` | `jmp` | Hoppa till adress |
| `anropa` | `call` | Anropa funktion |
| `returnera` | `ret` | Returnera från funktion |
| `avbrott` | `int` | Programvaruavbrott |
| `systemanrop` | `syscall` | Kärnanrop |

## 📝 Kodexempel

```asm
; Hello World på svenska
sektion .data
    meddelande: db "Hej varlden!", 10

sektion .text
    global _start

_start:
    flytta rax, 1          ; syscall: write
    flytta rdi, 1          ; fd: stdout
    flytta rsi, meddelande ; buffer
    flytta rdx, 13         ; length
    systemanrop

    flytta rax, 60         ; syscall: exit
    flytta rdi, 0          ; felkod
    systemanrop
```

## 🚀 Användning

```bash
python mlasm.py sv program.masm
```
