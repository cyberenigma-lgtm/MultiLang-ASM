# How to Use MultiLang-ASM (v1.0.0 Native C99 / UPL+)

MultiLang-ASM runs as a standalone native binary with **zero external dependencies**.

---

## 🛠️ 1. Compiling the Engine

The engine is written in standard ANSI C99 and compiles with any C compiler:

```bash
# Windows (MinGW GCC):
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm.exe

# Linux / macOS:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm
```

Alternatively, running `mlasm.bat` (Windows) or `make` (Linux/macOS) will automatically build the executable.

---

## 💻 2. Basic CLI Commands

### Direct Transpilation
Specify the language code and the target output file:
```bash
mlasm es examples/hello_es.masm -o hello_es.asm
mlasm fr examples/hello_fr.masm -o hello_fr.asm
mlasm zh examples/hello_zh.masm -o hello_zh.asm
```

### Auto-Detection Mode
MultiLang-ASM can automatically determine the source language by scanning keyword frequencies:
```bash
mlasm auto examples/hello_ru.masm -o hello_ru.asm
mlasm auto examples/hello_la.masm -o hello_la.asm
```

### Reversible / PRETTY Mode
Convert standard NASM assembly into any of the 150 supported languages:
```bash
mlasm --reverse es standard_code.asm -o code_in_spanish.masm
mlasm --reverse ja standard_code.asm -o code_in_japanese.masm
```

### Direct Build Pipeline (`--build`)
Transpiles, assembles via NASM, and links via GCC in one command:
```bash
mlasm --build es examples/hello_es.masm
```

### List Languages & Run Tests
```bash
mlasm --list-langs    # Displays all 150 compiled language packages
mlasm --test          # Executes the internal 9-step C99 verification suite
```
