# MultiLang-ASM: Tlapalhuiliztli (Nahuatl - nah)

Nahuatlahtolli tlapalhuiliztli MultiLang-ASM-techcopa.

## 🛠 Tlatequiliztli

| MultiLang-ASM | NASM (x86_64) | Tlen quihtoa |
| :--- | :--- | :--- |
| `huica` | `mov` | Tlapohualli huica |
| `tlapohua` | `add` | Tlapohualli tlapohua |
| `tlatzacuia` | `sub` | Tlapohualli tlatzacuia |
| `tlanonotza` | `cmp` | Tlapohualli tlanonotza |
| `choloa` | `jmp` | Choloa |
| `notza` | `call` | Notza |
| `cuepa` | `ret` | Cuepa |
| `tzacuia` | `int` | Tzacuia |
| `tequitl_notza` | `syscall` | Tequitl notza |

## 📝 Code Adibidea

```asm
; Niltze Cemanahuatl Nahuatl-techcopa
tlaxelzolli .data
    niltze: db "Niltze Cemanahuatl!", 10

tlaxelzolli .text
    global _start

_start:
    huica rax, 1          ; syscall: write
    huica rdi, 1          ; fd: stdout
    huica rsi, niltze     ; buffer
    huica rdx, 20         ; length
    tequitl_notza

    huica rax, 60         ; syscall: exit
    huica rdi, 0          ; exit code
    tequitl_notza
```

## 🚀 Tlatequiliztli

```bash
python mlasm.py nah programa.masm
```
