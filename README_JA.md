# MultiLang-ASM v1.0.0 (UPL+ C99 ネイティブ版)

**世界初のx86_64向け多言語アセンブラエンジン。**  
**UPL (Universal Polyglot Layer)** エコシステムおよび Neuro-OS コアの一部。

母国語でアセンブリコードを記述 · 世界150言語に対応 · 200以上のx86_64命令セット · 100% ANSI C99ネイティブ実装 · Python依存ゼロ · 超高速変換（2ミリ秒未満） · NASM完全互換。

## クイックスタート
```bash
# ネイティブエンジンのコンパイル:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# アセンブリのトランスパイル:
mlasm ja sample.masm -o sample.asm

# 言語の自動検出:
mlasm auto sample.masm -o sample.asm
```
