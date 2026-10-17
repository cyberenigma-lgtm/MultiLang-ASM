# MultiLang-ASM v1.0.0 (Édition UPL+ C99)

**Le premier moteur d'assembleur multilingue et souverain pour x86_64.**  
Partie intégrante de l'écosystème **UPL (Universal Polyglot Layer)** et du noyau Neuro-OS.

Écrivez du code assembleur dans votre langue maternelle · 150 Langues du Monde · 200+ Instructions x86_64 · Moteur Natif 100% ANSI C99 · Zéro Dépendance Python · Exécution Instantanée (<2 ms) · Compatible NASM.

## Utilisation Rapide
```bash
# Compilation du moteur natif :
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilation :
mlasm fr exemple.masm -o exemple.asm

# Détection automatique de la langue :
mlasm auto exemple.masm -o exemple.asm
```
