# MultiLang-ASM: Àwọn Ìtọ́ni (Yoruba - yo)

Kaabo si atilẹyin ede Yoruba fun MultiLang-ASM.

## 🛠 Àwọn Àṣẹ Gboogi

| MultiLang-ASM | NASM (x86_64) | Ìtumọ̀ |
| :--- | :--- | :--- |
| `gbe` | `mov` | Gbe data |
| `fikun` | `add` | Fikun iye |
| `yọkuro` | `sub` | Yọ iye kuro |
| `fiwe` | `cmp` | Fi iye we |
| `mẹfọ` | `jmp` | Mẹfọ si adirẹsi |
| `pè` | `call` | Pè iṣẹ́ |
| `padà` | `ret` | Padà kuro ninu iṣẹ́ |
| `da_duro` | `int` | Da duro |
| `pe_eto` | `syscall` | Pe eto iṣẹ́ |

## 📝 Àpẹẹrẹ Code

```asm
; Kaabo Ayé ni ede Yoruba
apa .data
    ìran: db "Kaabo Aye!", 10

apa .text
    global _start

_start:
    gbe rax, 1          ; syscall: write
    gbe rdi, 1          ; fd: stdout
    gbe rsi, ìran       ; buffer
    gbe rdx, 11         ; length
    pe_eto

    gbe rax, 60         ; syscall: exit
    gbe rdi, 0          ; exit code
    pe_eto
```

## 🚀 Ìlò

```bash
python mlasm.py yo eto.masm
```
