# MultiLang-ASM: Umarni (Hausa - ha)

Sannu da zuwa tallafin Hausa don MultiLang-ASM.

## 🛠 Muhimman Umarni

| MultiLang-ASM | NASM (x86_64) | Bayani |
| :--- | :--- | :--- |
| `motsa` | `mov` | Motsa bayanai |
| `kara` | `add` | Kara harka |
| `rage` | `sub` | Rage harka |
| `gwada` | `cmp` | Gwada bayanai |
| `tsallaka` | `jmp` | Tsallaka zuwa adireshi |
| `kira` | `call` | Kira aiki |
| `koma` | `ret` | Koma daga aiki |
| `tsayawa` | `int` | Tsayawar software |
| `kiran_tsarin` | `syscall` | Kiran tsarin aiki |

## 📝 Misalan Lambar

```asm
; Sannu Duniya a yaren Hausa
fannin .data
    sako: db "Sannu Duniya!", 10

fannin .text
    global _start

_start:
    motsa rax, 1          ; syscall: write
    motsa rdi, 1          ; fd: stdout
    motsa rsi, sako       ; buffer
    motsa rdx, 14         ; length
    kiran_tsarin

    motsa rax, 60         ; syscall: exit
    motsa rdi, 0          ; exit code
    kiran_tsarin
```

## 🚀 Amfani

```bash
python mlasm.py ha shiri.masm
```
