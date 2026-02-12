# MultiLang-ASM: Pituduh (Basa Sunda - su)

Wilujeng sumping di pangrojong basa Sunda pikeun MultiLang-ASM.

## 🛠 Parentah Dasar

| MultiLang-ASM | NASM (x86_64) | Katerangan |
| :--- | :--- | :--- |
| `pindah` | `mov` | Mindahkeun data |
| `tambah` | `add` | Nambah nilai |
| `kurang` | `sub` | Ngurangan nilai |
| `banding` | `cmp` | Ngabandingkeun nilai |
| `luncat` | `jmp` | Luncat ka alamat |
| `ngagero` | `call` | Ngagero fungsi |
| `balik` | `ret` | Balik ti fungsi |
| `sela` | `int` | Sela software |
| `gero_sistem` | `syscall` | Gero sistem |

## 📝 Conto Kode

```asm
; Halo Dunya dina basa Sunda
bagean .data
    talatah: db "Halo Dunya!", 10

bagean .text
    global _start

_start:
    pindah rax, 1          ; syscall: write
    pindah rdi, 1          ; fd: stdout
    pindah rsi, talatah    ; buffer
    pindah rdx, 12         ; length
    gero_sistem

    pindah rax, 60         ; syscall: exit
    pindah rdi, 0          ; exit code
    gero_sistem
```

## 🚀 Pamakéan

```bash
python mlasm.py su program.masm
```
