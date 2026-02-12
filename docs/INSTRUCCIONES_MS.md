# MultiLang-ASM: Arahan (Bahasa Melayu - ms)

Selamat datang ke sokonagan Bahasa Melayu untuk MultiLang-ASM.

## 🛠 Arahan Asas

| MultiLang-ASM | NASM (x86_64) | Penerangan |
| :--- | :--- | :--- |
| `pindah` | `mov` | Pindah data |
| `tambah` | `add` | Tambah nilai |
| `tolak` | `sub` | Tolak nilai |
| `banding` | `cmp` | Banding nilai |
| `lompat` | `jmp` | Lompat ke alamat |
| `panggil` | `call` | Panggil fungsi |
| `kembali` | `ret` | Kembali dari fungsi |
| `sampuk` | `int` | Sampukan perisian |
| `panggilan_sistem`| `syscall` | Panggilan sistem |

## 📝 Contoh Kod

```asm
; Helo dunia dalam Bahasa Melayu
seksyen .data
    mesej: db "Helo dunia!", 10

seksyen .text
    global _start

_start:
    pindah rax, 1          ; syscall: write
    pindah rdi, 1          ; fd: stdout
    pindah rsi, mesej      ; buffer
    pindah rdx, 12         ; length
    panggilan_sistem

    pindah rax, 60         ; syscall: exit
    pindah rdi, 0          ; kod ralat
    panggilan_sistem
```

## 🚀 Penggunaan

```bash
python mlasm.py ms program.masm
```
