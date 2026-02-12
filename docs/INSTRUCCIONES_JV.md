# MultiLang-ASM: Pituduh (Basa Jawa - jv)

Sugeng rawuh ing panyengkuyung basa Jawa kagem MultiLang-ASM.

## 🛠 Prentah Dasar

| MultiLang-ASM | NASM (x86_64) | Katrangan |
| :--- | :--- | :--- |
| `pindah` | `mov` | Pindah data |
| `tambah` | `add` | Tambah angka |
| `suda` | `sub` | Suda angka |
| `banding` | `cmp` | Banding angka |
| `mlumpat` | `jmp` | Mlumpat menyang alamat |
| `timbal` | `call` | Timbal fungsi |
| `bali` | `ret` | Bali saka fungsi |
| `selo` | `int` | Selo software |
| `timbal_sistem` | `syscall` | Timbal sistem |

## 📝 Contoh Kode

```asm
; Halo Donya ing basa Jawa
bagean .data
    pesen: db "Halo Donya!", 10

bagean .text
    global _start

_start:
    pindah rax, 1          ; syscall: write
    pindah rdi, 1          ; fd: stdout
    pindah rsi, pesen      ; buffer
    pindah rdx, 12         ; length
    timbal_sistem

    pindah rax, 60         ; syscall: exit
    pindah rdi, 0          ; exit code
    timbal_sistem
```

## 🚀 Panganggo

```bash
python mlasm.py jv program.masm
```
