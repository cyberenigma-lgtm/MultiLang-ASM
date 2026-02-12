# MultiLang-ASM: Akwankyerɛ (Akan - ak)

Akwaaba kɔ MultiLang-ASM Akan kasa mu.

## 🛠 Akwankyerɛ Titiriw

| MultiLang-ASM | NASM (x86_64) | Nkyerɛmu |
| :--- | :--- | :--- |
| `tu` | `mov` | Tu nsɛm |
| `ka_ho` | `add` | Ka ho |
| `yi_fi_mu` | `sub` | Yi fi mu |
| `toto` | `cmp` | Toto nsɛm |
| `huri` | `jmp` | Huri kɔ adirese |
| `frɛ` | `call` | Frɛ dwumadi |
| `ba_man` | `ret` | Ba dwumadi mu |
| `gyae` | `int` | Gyae dwumadi |
| `frɛ_nhyehyɛe` | `syscall` | Frɛ nhyehyɛe |

## 📝 Code Mfatoho

```asm
; Maakye Wiase wɔ Akan kasa mu
fa .data
    asɛm: db "Maakye Wiase!", 10

fa .text
    global _start

_start:
    tu rax, 1          ; syscall: write
    tu rdi, 1          ; fd: stdout
    tu rsi, asɛm       ; buffer
    tu rdx, 14         ; length
    frɛ_nhyehyɛe

    tu rax, 60         ; syscall: exit
    tu rdi, 0          ; exit code
    frɛ_nhyehyɛe
```

## 🚀 Dwumadie

```bash
python mlasm.py ak dwumadie.masm
```
