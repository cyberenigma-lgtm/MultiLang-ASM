# MultiLang-ASM v1.0.0 (UPL+ C99 Edition)

**Die weltweit erste souveräne mehrsprachige x86_64-Assembler-Engine.**  
Bestandteil des **UPL (Universal Polyglot Layer)** Ökosystems und des Neuro-OS-Kerns.

Schreiben Sie Assembler-Code in Ihrer Muttersprache · 150 Weltsprachen · 200+ x86_64-Befehle · 100% native ANSI C99-Engine · Keine Python-Laufzeitabhängigkeit · Blitzschnell (<2 ms) · NASM-kompatibel.

## Schnellanleitung
```bash
# Kompilieren der nativen Engine:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Übersetzung:
mlasm de beispiel.masm -o beispiel.asm

# Automatische Spracherkennung:
mlasm auto beispiel.masm -o beispiel.asm
```
