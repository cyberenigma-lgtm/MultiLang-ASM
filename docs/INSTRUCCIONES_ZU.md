# MultiLang-ASM: Imiyalo (isiZulu - zu)

Siyakwamukela ekusekelweni kwesiZulu kwe-MultiLang-ASM.

## 🛠 Imiyalo Eyisisekelo

| MultiLang-ASM | NASM (x86_64) | Incazelo |
| :--- | :--- | :--- |
| `hambisa` | `mov` | Hambisa idatha |
| `hlanganisa` | `add` | Hlanganisa inani |
| `susa` | `sub` | Susa inani |
| `qhathanisa` | `cmp` | Qhathanisa amanani |
| `eqa` | `jmp` | Eqa ekhelini |
| `biza` | `call` | Biza umsebenzi |
| `buya` | `ret` | Buya emsebenzini |
| `uphazamiso` | `int` | Uphazamiso lwesoftware |
| `ukubizwa_kwesistimu`| `syscall` | Ukubizwa kwesistimu |

## 📝 Isibonelo Code

```asm
; Sawubona Mhlaba ngesiZulu
isigaba .data
    isaziso: db "Sawubona Mhlaba!", 10

isigaba .text
    global _start

_start:
    hambisa rax, 1          ; syscall: write
    hambisa rdi, 1          ; fd: stdout
    hambisa rsi, isaziso    ; buffer
    hambisa rdx, 17         ; length
    ukubizwa_kwesistimu

    hambisa rax, 60         ; syscall: exit
    hambisa rdi, 0          ; exit code
    ukubizwa_kwesistimu
```

## 🚀 Ukusetshenziswa

```bash
python mlasm.py zu uhlelo.masm
```
