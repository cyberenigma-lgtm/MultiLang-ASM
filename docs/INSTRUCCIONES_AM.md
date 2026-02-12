# MultiLang-ASM: መመሪያዎች (አማርኛ - am)

ወደ MultiLang-ASM የአማርኛ ድጋፍ እንኳን በደህና መጡ።

## 🛠 መሰረታዊ ትዕዛዞች

| MultiLang-ASM | NASM (x86_64) | መግለጫ |
| :--- | :--- | :--- |
| `አንቀሳቅስ` | `mov` | መረጃ ማንቀሳቀስ |
| `ጨምር` | `add` | እሴት መጨመር |
| `ቀንስ` | `sub` | እሴት መቀነስ |
| `አወዳድር` | `cmp` | እሴቶችን ማወዳደር |
| `ዝለል` | `jmp` | ወደ አድራሻ መዝለል |
| `ጥራ` | `call` | ተግባርን መጥራት |
| `ተመለስ` | `ret` | ከተግባር መመለስ |
| `አቋርጥ` | `int` | የሶፍትዌር ማቋረጥ |
| `ሲስተም_ጥራ` | `syscall` | የስርዓት ጥሪ |

## 📝 የኮድ ምሳሌ

```asm
; ሰላም ለዓለም በአማርኛ
ክፍል .data
    መልዕክት: db "Selam le Alem!", 10

ክፍል .text
    global _start

_start:
    አንቀሳቅስ rax, 1          ; syscall: write
    አንቀሳቅስ rdi, 1          ; fd: stdout
    አንቀሳቅስ rsi, መልዕክት     ; buffer
    አንቀሳቅስ rdx, 15         ; length
    ሲስተም_ጥራ

    አንቀሳቅስ rax, 60         ; syscall: exit
    አንቀሳቅስ rdi, 0          ; exit code
    ሲስተም_ጥራ
```

## 🚀 አጠቃቀም

```bash
python mlasm.py am ፕሮግራም.masm
```
