# MultiLang-ASM: Instructies (Nederlands - nl)

Welkom bij de Nederlandse ondersteuning voor MultiLang-ASM.

## 🛠 Basisopdrachten

| MultiLang-ASM | NASM (x86_64) | Beschrijving |
| :--- | :--- | :--- |
| `verplaats` | `mov` | Verplaats gegevens |
| `optellen` | `add` | Optellen |
| `aftrekken` | `sub` | Aftrekken |
| `vergelijk` | `cmp` | Waarden vergelijken |
| `spring` | `jmp` | Spring naar adres |
| `roep` | `call` | Functie aanroepen |
| `keer_terug` | `ret` | Terugkeren van functie |
| `onderbreking` | `int` | Software-onderbreking |
| `systeemaanroep` | `syscall` | Kernel aanroep |

## 📝 Codevoorbeeld

```asm
; Hello World in het Nederlands
sectie .data
    bericht: db "Hallo wereld!", 10

sectie .text
    globaal _start

_start:
    verplaats rax, 1          ; syscall: write
    verplaats rdi, 1          ; fd: stdout
    verplaats rsi, bericht    ; buffer
    verplaats rdx, 14         ; length
    systeemaanroep

    verplaats rax, 60         ; syscall: exit
    verplaats rdi, 0          ; foutcode
    systeemaanroep
```

## 🚀 Gebruik

```bash
python mlasm.py nl program.masm
```
