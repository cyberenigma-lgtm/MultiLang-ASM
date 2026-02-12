# MultiLang-ASM: Instrucțiuni (Română - ro)

Bun venit la suportul pentru limba română în MultiLang-ASM.

## 🛠 Comenzi de Bază

| MultiLang-ASM | NASM (x86_64) | Descriere |
| :--- | :--- | :--- |
| `muta` | `mov` | Mută date |
| `aduna` | `add` | Adună valoare |
| `scade` | `sub` | Scade valoare |
| `compara` | `cmp` | Compară valori |
| `sari` | `jmp` | Sari la adresă |
| `apeleaza` | `call` | Apelează funcție |
| `returneaza` | `ret` | Revenire din funcție |
| `intrerupere` | `int` | Întrerupere software |
| `apel_sistem` | `syscall` | Apel de sistem |

## 📝 Exemplu de Cod

```asm
; Salut lume în română
secțiune .data
    mesaj: db "Salut lume!", 10

secțiune .text
    global _start

_start:
    muta rax, 1          ; syscall: write
    muta rdi, 1          ; fd: stdout
    muta rsi, mesaj      ; buffer
    muta rdx, 12         ; length
    apel_sistem

    muta rax, 60         ; syscall: exit
    muta rdi, 0          ; cod eroare
    apel_sistem
```

## 🚀 Utilizare

```bash
python mlasm.py ro program.masm
```
