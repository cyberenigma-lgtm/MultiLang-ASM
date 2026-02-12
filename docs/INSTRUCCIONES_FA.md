# MultiLang-ASM: دستورالعمل‌ها (فارسی - fa)

به بخش پشتیبانی فارسی MultiLang-ASM خوش آمدید.

## 🛠 دستورات پایه

| MultiLang-ASM | NASM (x86_64) | توضیحات |
| :--- | :--- | :--- |
| `انتقال` | `mov` | انتقال داده |
| `جمع` | `add` | جمع کردن |
| `تفریق` | `sub` | تفریق کردن |
| `مقایسه` | `cmp` | مقایسه مقادیر |
| `پرش` | `jmp` | پرش به آدرس |
| `فراخوانی` | `call` | فراخوانی تابع |
| `بازگشت` | `ret` | بازگشت از تابع |
| `وقفه` | `int` | وقفه نرم‌افزاری |
| `فراخوانی_سیستم`| `syscall` | فراخوانی سیستم |

## 📝 نمونه کد

```asm
; سلام دنیا به زبان فارسی
بخش .data
    پیام: db "Salam Donya!", 10

بخش .text
    global _start

_start:
    انتقال rax, 1          ; syscall: write
    انتقال rdi, 1          ; fd: stdout
    انتقال rsi, پیام       ; buffer
    انتقال rdx, 13         ; length
    فراخوانی_سیستم

    انتقال rax, 60         ; syscall: exit
    انتقال rdi, 0          ; exit code
    فراخوانی_سیستم
```

## 🚀 استفاده

```bash
python mlasm.py fa program.masm
```
