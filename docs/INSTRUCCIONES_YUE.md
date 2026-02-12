# MultiLang-ASM: 指令 (粵語 - yue)

歡迎使用 MultiLang-ASM 粵語支援。

## 🛠 基本指令

| MultiLang-ASM | NASM (x86_64) | 說明 |
| :--- | :--- | :--- |
| `搬` | `mov` | 移動數據 |
| `加` | `add` | 加數 |
| `減` | `sub` | 減數 |
| `比` | `cmp` | 比較數值 |
| `跳` | `jmp` | 跳去地址 |
| `叫` | `call` | 呼叫功能 |
| `返` | `ret` | 功能返回 |
| `中斷` | `int` | 軟件中斷 |
| `叫系統` | `syscall` | 系統呼叫 |

## 📝 程式範例

```asm
; 粵語版你好世界
部分 .data
    內容: db "你好世界!", 10

部分 .text
    global _start

_start:
    搬 rax, 1          ; syscall: write
    搬 rdi, 1          ; fd: stdout
    搬 rsi, 內容       ; buffer
    搬 rdx, 14         ; length
    叫系統

    搬 rax, 60         ; syscall: exit
    搬 rdi, 0          ; exit code
    叫系統
```

## 🚀 使用方法

```bash
python mlasm.py yue program.masm
```
