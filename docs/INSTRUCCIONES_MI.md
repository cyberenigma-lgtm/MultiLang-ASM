# MultiLang-ASM: Ngā Tohutohu (Te Reo Māori - mi)

Nau mai ki te tautoko i te reo Māori mō MultiLang-ASM.

## 🛠 Ngā Whakahau Taketake

| MultiLang-ASM | NASM (x86_64) | Whakaahuatanga |
| :--- | :--- | :--- |
| `neke` | `mov` | Neke raraunga |
| `tāpiri` | `add` | Tāpiri uara |
| `tango` | `sub` | Tango uara |
| `whakataurite` | `cmp` | Whakataurite uara |
| `peke` | `jmp` | Peke ki te wāhitau |
| `karanga` | `call` | Karanga i te mahi |
| `hoki` | `ret` | Hoki mai i te mahi |
| `aukati` | `int` | Aukati pūmanawa |
| `karanga_pūnaha` | `syscall` | Karanga pūnaha |

## 📝 Tauira Wahere

```asm
; Kia ora te Ao i te reo Māori
wāhanga .data
    karere: db "Kia ora te Ao!", 10

wāhanga .text
    global _start

_start:
    neke rax, 1          ; syscall: write
    neke rdi, 1          ; fd: stdout
    neke rsi, karere     ; buffer
    neke rdx, 16         ; length
    karanga_pūnaha

    neke rax, 60         ; syscall: exit
    neke rdi, 0          ; exit code
    karanga_pūnaha
```

## 🚀 Whakamahinga

```bash
python mlasm.py mi hōtaka.masm
```
