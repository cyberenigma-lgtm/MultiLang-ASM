# MultiLang-ASM v1.0.0 (UPL+ C99 Editie)

**'s Werelds eerste soevereine meertalige x86_64-assemblermotor.**  
Onderdeel van het **UPL (Universal Polyglot Layer)** ecosysteem en Neuro-OS.

Schrijf assembleercode in uw moedertaal · 150 Wereldtalen · 200+ x86_64-instructies · 100% Native ANSI C99 Motor · Geen Python-afhankelijkheid · Ultrasnel (<2 ms) · Volledig NASM-compatibel.

## Snel Aan de Slag
```bash
# Compileer de native motor:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpileren:
mlasm nl voorbeeld.masm -o voorbeeld.asm

# Automatische taaldetectie:
mlasm auto voorbeeld.masm -o voorbeeld.asm
```
