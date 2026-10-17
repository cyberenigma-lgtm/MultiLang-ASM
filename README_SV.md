# MultiLang-ASM v1.0.0 (UPL+ C99 Utgåva)

**Världens första suveräna flerspråkiga x86_64-assemblermotor.**  
En integrerad del av **UPL (Universal Polyglot Layer)** och Neuro-OS.

Skriv assemblerkod på ditt modersmål · 150 Världsspråk · 200+ x86_64-instruktioner · 100% Inbyggd ANSI C99-motor · Noll Python-beroenden · Blixtsnabb (<2 ms) · NASM-kompatibel.

## Snabbstart
```bash
# Kompilera den inbyggda motorn:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilera:
mlasm sv exempel.masm -o exempel.asm

# Automatisk språkdetektering:
mlasm auto exempel.masm -o exempel.asm
```
