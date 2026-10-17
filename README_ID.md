# MultiLang-ASM v1.0.0 (Edisi UPL+ C99)

**Mesin assembler multibahasa x86_64 berdaulat pertama di dunia.**  
Bagian penting dari ekosistem **UPL (Universal Polyglot Layer)** dan inti Neuro-OS.

Tulis kode bahasa rakitan (assembly) dalam bahasa ibu Anda · 150 Bahasa Dunia · 200+ Instruksi x86_64 · Mesin Asli 100% ANSI C99 · Bebas Ketergantungan Python · Kecepatan Kilat (<2 ms) · Kompatibel dengan NASM.

## Panduan Cepat
```bash
# Kompilasi mesin asli:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# Transpilasi:
mlasm id contoh.masm -o contoh.asm

# Deteksi Bahasa Otomatis:
mlasm auto contoh.masm -o contoh.asm
```
