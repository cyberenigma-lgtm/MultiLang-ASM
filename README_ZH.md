# MultiLang-ASM v1.0.0 (UPL+ C99 原生引擎版)

**全球首個專為主權低階開發打造的 x86_64 多語言組譯器引擎。**  
屬於 **UPL (Universal Polyglot Layer)** 生態系統與 Neuro-OS 核心技術。

使用母語編寫組合語言代碼 · 支援全球 150 種語言與方言 · 200+ 條標準 x86_64 指令 · 100% 純 ANSI C99 打造 · 零 Python 依賴 · 極速轉譯 (<2 ms) · 完全相容 NASM。

## 快速使用
```bash
# 編譯原生執行檔：
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# 轉譯組譯碼：
mlasm zh 範例.masm -o 範例.asm

# 智慧自動語言識別：
mlasm auto 範例.masm -o 範例.asm
```
