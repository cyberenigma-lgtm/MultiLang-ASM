# MultiLang-ASM: Instrukcje (Polski - pl)

Witamy w polskim wsparciu dla MultiLang-ASM.

## 🛠 Podstawowe komendy

| MultiLang-ASM | NASM (x86_64) | Opis |
| :--- | :--- | :--- |
| `przenies` | `mov` | Przeniesienie danych |
| `dodaj` | `add` | Dodawanie |
| `odejmij` | `sub` | Odejmowanie |
| `porownaj` | `cmp` | Porównanie wartości |
| `skocz` | `jmp` | Skok pod adres |
| `wolaj` | `call` | Wywołanie funkcji |
| `wroc` | `ret` | Powrót z funkcji |
| `przerwanie` | `int` | Przerwanie programowe |
| `wywolanie_systemowe`| `syscall` | Wywołanie systemowe |

## 📝 Przykład kodu

```asm
; Hello World po polsku
sekcja .data
    wiadomosc: db "Witaj swiecie!", 10

sekcja .text
    globalny _start

_start:
    przenies rax, 1          ; syscall: write
    przenies rdi, 1          ; fd: stdout
    przenies rsi, wiadomosc ; buffer
    przenies rdx, 15         ; length
    wywolanie_systemowe

    przenies rax, 60         ; syscall: exit
    przenies rdi, 0          ; kod bledu
    wywolanie_systemowe
```

## 🚀 Użycie

```bash
python mlasm.py pl program.masm
```
