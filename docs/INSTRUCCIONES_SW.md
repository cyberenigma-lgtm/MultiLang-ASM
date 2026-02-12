# MultiLang-ASM: Maagizo (Kiswahili - sw)

Karibu kwenye usaidizi wa Kiswahili kwa MultiLang-ASM.

## 🛠 Amri za Msingi

| MultiLang-ASM | NASM (x86_64) | Maelezo |
| :--- | :--- | :--- |
| `hamisha` | `mov` | Hamisha data |
| `jumlisha` | `add` | Jumlisha |
| `toa` | `sub` | Toa |
| `linganisha` | `cmp` | Linganisha thamani |
| `rukia` | `jmp` | Rukia kwa anwani |
| `ita` | `call` | Ita chaguo |
| `rudi` | `ret` | Rudi kutoka chaguo |
| `itilafu` | `int` | Itilafu ya programu |
| `ito_mfumo` | `syscall` | Ito ya mfumo |

## 📝 Mfano wa Kanuni

```asm
; Hello World kwa Kiswahili
sehemu .data
    ujumbe: db "Habari Dunia!", 10

sehemu .text
    kote _anza

_anza:
    hamisha rax, 1          ; syscall: write
    hamisha rdi, 1          ; fd: stdout
    hamisha rsi, ujumbe     ; buffer
    hamisha rdx, 14         ; length
    ito_mfumo

    hamisha rax, 60         ; syscall: exit
    hamisha rdi, 0          ; error code
    ito_mfumo
```

## 🚀 Matumizi

```bash
python mlasm.py sw program.masm
```
