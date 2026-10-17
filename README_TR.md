# MultiLang-ASM v1.0.0 (UPL+ C99 Sürümü)

**Dünyanın ilk x86_64 çok dilli ve egemen çevirici (assembler) motoru.**  
**UPL (Universal Polyglot Layer)** ekosisteminin ve Neuro-OS çekirdeğinin parçası.

Kendi ana dilinizde assembly yazın · 150 Dünya Dili · 200+ x86_64 Komutu · %100 Yerel ANSI C99 Motoru · Sıfır Python Bağımlılığı · Anında Çalışma (<2 ms) · NASM Uyumlu.

## Hızlı Başlangıç
```bash
# Yerel motoru derleyin:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Dönüştürme:
mlasm tr ornek.masm -o ornek.asm

# Otomatik Dil Algılama:
mlasm auto ornek.masm -o ornek.asm
```
