# MultiLang-ASM v1.0.0 (Edição UPL+ C99)

**O primeiro motor de montador (assembler) soberano e multilíngue do mundo para x86_64.**  
Parte integrante do ecossistema **UPL (Universal Polyglot Layer)** e do núcleo do Neuro-OS.

Escreva código assembly na sua língua nativa · 150 Idiomas do Mundo · 200+ Instruções x86_64 · Motor Nativo 100% ANSI C99 · Zero Dependências de Python · Execução Instantânea (<2 ms) · Compatível com NASM.

## Uso Rápido
```bash
# Compilação do motor nativo:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilação:
mlasm pt exemplo.masm -o exemplo.asm

# Detecção automática de idioma:
mlasm auto exemplo.masm -o exemplo.asm
```
