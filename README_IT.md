# MultiLang-ASM v1.0.0 (Edizione UPL+ C99)

**Il primo motore assemblatore multilingue sovrano al mondo per x86_64.**  
Parte fondamentale dell'ecosistema **UPL (Universal Polyglot Layer)** e del kernel Neuro-OS.

Scrivi codice assembly nella tua lingua madre · 150 Lingue del Mondo · 200+ Istruzioni x86_64 · Motore Nativo 100% ANSI C99 · Zero Dipendenze Python · Esecuzione Istantanea (<2 ms) · Compatibile con NASM.

## Uso Rapido
```bash
# Compilazione del motore nativo:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilazione:
mlasm it esempio.masm -o esempio.asm

# Rilevamento automatico della lingua:
mlasm auto esempio.masm -o esempio.asm
```
