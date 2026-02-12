# MultiLang-ASM: Instruksies (Afrikaans - af)

Welkom by die Afrikaanse ondersteuning vir MultiLang-ASM.

## 🛠 Basiese Opdragte

| MultiLang-ASM | NASM (x86_64) | Beskrywing |
| :--- | :--- | :--- |
| `skuif` | `mov` | Skuif data |
| `tel_by` | `add` | Tel waarde by |
| `trek_af` | `sub` | Trek waarde af |
| `vergelyk` | `cmp` | Vergelyk waardes |
| `spring` | `jmp` | Spring na adres |
| `roep` | `call` | Roep 'n funksie |
| `keer_terug` | `ret` | Keer terug van funksie |
| `onderbreking` | `int` | Sagteware-onderbreking |
| `stelselroep` | `syscall` | Stelselroep |

## 📝 Kodevoorbeeld

```asm
; Hallo wêreld in Afrikaans
afdeling .data
    boodskap: db "Hallo wereld!", 10

afdeling .text
    global _start

_start:
    skuif rax, 1          ; syscall: write
    skuif rdi, 1          ; fd: stdout
    skuif rsi, boodskap   ; buffer
    skuif rdx, 14         ; length
    stelselroep

    skuif rax, 60         ; syscall: exit
    skuif rdi, 0          ; exit code
    stelselroep
```

## 🚀 Gebruik

```bash
python mlasm.py af program.masm
```
