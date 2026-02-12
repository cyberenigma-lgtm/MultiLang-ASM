# MultiLang-ASM: Instruksjoner (Norsk - no)

Velkommen til norsk støtte for MultiLang-ASM.

## 🛠 Grunnleggende kommandoer

| MultiLang-ASM | NASM (x86_64) | Beskrivelse |
| :--- | :--- | :--- |
| `flytt` | `mov` | Flytt data |
| `legg_til` | `add` | Legg til verdi |
| `trekk_fra` | `sub` | Trekk fra verdi |
| `sammenlign` | `cmp` | Sammenlign verdier |
| `hopp` | `jmp` | Hopp til adresse |
| `kall` | `call` | Kall en funksjon |
| `returner` | `ret` | Returner fra funksjon |
| `avbrudd` | `int` | Programvareavbrudd |
| `systemkall` | `syscall` | Systemkall |

## 📝 Kodeeksempel

```asm
; Hallo verden på norsk
seksjon .data
    melding: db "Hallo verden!", 10

seksjon .text
    global _start

_start:
    flytt rax, 1          ; syscall: write
    flytt rdi, 1          ; fd: stdout
    flytt rsi, melding    ; buffer
    flytt rdx, 14         ; length
    systemkall

    flytt rax, 60         ; syscall: exit
    flytt rdi, 0          ; feilkode
    systemkall
```

## 🚀 Bruk

```bash
python mlasm.py no programa.masm
```
