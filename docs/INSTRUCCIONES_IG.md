# MultiLang-ASM: Ntụziaka (Igbo - ig)

Nnọọ na nkwado asụsụ Igbo maka MultiLang-ASM.

## 🛠 Ihe Ndị bụ Isi

| MultiLang-ASM | NASM (x86_64) | Nkọwa |
| :--- | :--- | :--- |
| `bugharịa` | `mov` | Bugharịa data |
| `tinye` | `add` | Tinye uru |
| `wepụ` | `sub` | Wepụ uru |
| `tụnyere` | `cmp` | Tụnyere uru |
| `mali` | `jmp` | Mali gaa adirẹsi |
| `kpọọ` | `call` | Kpọọ ọrụ |
| `lọta` | `ret` | Lọta n'ọrụ |
| `ndabichi` | `int` | Ndabichi software |
| `nkpọ_usoro` | `syscall` | Nkpọ usoro |

## 📝 Ihe Atụ Code

```asm
; Ndewo Ụwa n'asụsụ Igbo
ngalaba .data
    ozi: db "Ndewo Uwa!", 10

ngalaba .text
    global _start

_start:
    bugharịa rax, 1          ; syscall: write
    bugharịa rdi, 1          ; fd: stdout
    bugharịa rsi, ozi        ; buffer
    bugharịa rdx, 11         ; length
    nkpọ_usoro

    bugharịa rax, 60         ; syscall: exit
    bugharịa rdi, 0          ; exit code
    nkpọ_usoro
```

## 🚀 Ojiji

```bash
python mlasm.py ig usoro.masm
```
