# MultiLang-ASM: Ohjeet (Suomi - fi)

Tervetuloa suomenkieliseen MultiLang-ASM-tukeen.

## 🛠 Peruskomennot

| MultiLang-ASM | NASM (x86_64) | Kuvaus |
| :--- | :--- | :--- |
| `siirrä` | `mov` | Siirrä tietoa |
| `lisää` | `add` | Lisää arvo |
| `vähennä` | `sub` | Vähennä arvo |
| `vertaa` | `cmp` | Vertaa arvoja |
| `hyppää` | `jmp` | Hyppää osoitteeseen |
| `kutsu` | `call` | Kutsu funktiota |
| `palaa` | `ret` | Palaa funktiosta |
| `keskeytys` | `int` | Ohjelmistokeskeytys |
| `järjestelmäkutsu`| `syscall` | Järjestelmäkutsu |

## 📝 Koodiesimerkki

```asm
; Hei maailma suomeksi
lohko .data
    viesti: db "Hei maailma!", 10

lohko .text
    globaali _start

_start:
    siirrä rax, 1          ; syscall: write
    siirrä rdi, 1          ; fd: stdout
    siirrä rsi, viesti      ; buffer
    siirrä rdx, 13         ; length
    järjestelmäkutsu

    siirrä rax, 60         ; syscall: exit
    siirrä rdi, 0          ; virhekoodi
    järjestelmäkutsu
```

## 🚀 Käyttö

```bash
python mlasm.py fi ohjelma.masm
```
