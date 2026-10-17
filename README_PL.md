# MultiLang-ASM v1.0.0 (Wydanie UPL+ C99)

**Pierwszy na świecie suwerenny wielojęzyczny silnik asemblera x86_64.**  
Część ekosystemu **UPL (Universal Polyglot Layer)** i jądra Neuro-OS.

Pisz kod asemblera w swoim języku ojczystym · 150 Języków Świata · 200+ Instrukcji x86_64 · Natywny Silnik 100% ANSI C99 · Zero Zależności od Pythona · Błyskawiczne Działanie (<2 ms) · Kompatybilność z NASM.

## Szybki Start
```bash
# Kompilacja silnika natywnego:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilacja:
mlasm pl przyklad.masm -o przyklad.asm

# Automatyczne wykrywanie języka:
mlasm auto przyklad.masm -o przyklad.asm
```
