# MultiLang-ASM: Treoracha (Gaeilge - ga)

Fáilte go dtí an tacaíocht Ghaeilge do MultiLang-ASM.

## 🛠 Bunorduithe

| MultiLang-ASM | NASM (x86_64) | Cur síos |
| :--- | :--- | :--- |
| `bog` | `mov` | Bog sonraí |
| `suimigh` | `add` | Suimigh luachanna |
| `dealú` | `sub` | Dealú luachanna |
| `cuir_i_gcomparáid`| `cmp` | Cuir luachanna i gcomparáid |
| `léim` | `jmp` | Léim go seoladh |
| `glaoch` | `call` | Glaoigh ar fheidhm |
| `filleadh` | `ret` | Fill ón bhfeidhm |
| `idirbhriseadh` | `int` | Idirbhriseadh bogearraí |
| `glaoch_córais` | `syscall` | Glaoch córais |

## 📝 Sampla Cóid

```asm
; Dia duit an domhan i nGaeilge
rannóg .data
    teachtaireacht: db "Dia duit an domhan!", 10

rannóg .text
    global _start

_start:
    bog rax, 1          ; syscall: write
    bog rdi, 1          ; fd: stdout
    bog rsi, teachtaireacht ; buffer
    bog rdx, 20         ; length
    glaoch_córais

    bog rax, 60         ; syscall: exit
    bog rdi, 0          ; exit code
    glaoch_córais
```

## 🚀 Úsáid

```bash
python mlasm.py ga programa.masm
```
