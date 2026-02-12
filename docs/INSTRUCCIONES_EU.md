# MultiLang-ASM: Argibideak (Euskara - eu)

Ongi etorri MultiLang-ASM-ren euskarazko laguntzara.

## 🛠 Oinarrizko Komandoak

| MultiLang-ASM | NASM (x86_64) | Azalpena |
| :--- | :--- | :--- |
| `mugitu` | `mov` | Datuak mugitu |
| `gehitu` | `add` | Balioak gehitu |
| `kendu` | `sub` | Balioak kendu |
| `konparatu` | `cmp` | Balioak konparatu |
| `jauzi` | `jmp` | Helbide batera jauzi egin |
| `deitu` | `call` | Funtzio bati deitu |
| `itzuli` | `ret` | Funtziotik itzuli |
| `etena` | `int` | Software etena |
| `sistema_deia` | `syscall` | Sistema deia |

## 📝 Kode Adibidea

```asm
; Kaixo mundua euskaraz
sektorea .data
    mezua: db "Kaixo mundua!", 10

sektorea .text
    global _start

_start:
    mugitu rax, 1          ; syscall: write
    mugitu rdi, 1          ; fd: stdout
    mugitu rsi, mezua      ; buffer
    mugitu rdx, 14         ; length
    sistema_deia

    mugitu rax, 60         ; syscall: exit
    mugitu rdi, 0          ; errore kodea
    sistema_deia
```

## 🚀 Erabilera

```bash
python mlasm.py eu programa.masm
```
