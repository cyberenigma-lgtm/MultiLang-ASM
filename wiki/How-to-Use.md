# How to Use MultiLang-ASM

Complete guide to installing and using MultiLang-ASM.

---

## 📦 Installation

### Requirements
- Python 3.6 or higher
- NASM (for final compilation)

### Quick Install

```bash
git clone https://github.com/cyberenigma-lgtm/MultiLang-ASM.git
cd MultiLang-ASM
```

That's it! No dependencies required.

---

## 🚀 Basic Usage

### 1. Write Assembly in Your Language

Create a file `hello.masm` in Spanish:

```asm
; hello.masm
seccion .texto
global _inicio

_inicio:
    mover rax, 1          ; syscall write
    mover rdi, 1          ; stdout
    llamada_sistema
    
    mover rax, 60         ; syscall exit
    mover rdi, 0
    interrupcion 0x80
```

### 2. Translate to Standard ASM

```bash
python mlasm.py es hello.masm hello.asm
```

Output:
```
🛡️ MultiLang-ASM v0.3
   Language: ES
   Mode: Standard (NASM)
   Input: hello.masm
   Output: hello.asm
   Status: ✅ OK
```

### 3. Compile with NASM

```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
```

### 4. Run

```bash
./hello
```

---

## 🔄 Reverse Mode (PRETTY)

View standard ASM code in any language:

```bash
# View in French
python mlasm.py fr standard.asm french_view.masm --reverse

# View in Japanese
python mlasm.py ja standard.asm japanese_view.masm --reverse

# View in Arabic
python mlasm.py ar standard.asm arabic_view.masm --reverse
```

This is useful for:
- Learning assembly in your language
- International collaboration
- Code review in native language

---

## 🛠️ Command Line Reference

### Basic Syntax

```bash
python mlasm.py <language> <input> <output> [--reverse]
```

### Parameters

- `<language>` - Language code: `es`, `fr`, `de`, `it`, `ar`, `ru`, `ko`, `id`, `zh`, `ja`
- `<input>` - Input file path
- `<output>` - Output file path
- `--reverse` - (Optional) Reverse mode: standard ASM → native language

### Examples

```bash
# Spanish to NASM
python mlasm.py es programa.masm programa.asm

# French to NASM
python mlasm.py fr programme.masm programme.asm

# NASM to German (reverse)
python mlasm.py de program.asm programm_de.masm --reverse
```

---

## 📁 Project Structure Recommendations

### Small Project

```
my-program/
├── mlasm.py           # Copy of translator
├── src/
│   └── main.masm     # Your code in native language
├── build/
│   ├── main.asm      # Generated NASM
│   └── main.o        # Compiled object
└── programa           # Final binary
```

### Larger Project

```
my-os/
├── mlasm.py
├── Makefile
├── src/
│   ├── boot.masm
│   ├── kernel.masm
│   └── drivers.masm
└── build/
```

**Makefile example:**
```makefile
all:
	python mlasm.py es src/boot.masm build/boot.asm
	python mlasm.py es src/kernel.masm build/kernel.asm
	nasm -f elf64 build/boot.asm -o build/boot.o
	nasm -f elf64 build/kernel.asm -o build/kernel.o
	ld -T linker.ld build/*.o -o kernel.bin
```

---

## 🧪 Testing Your Code

### Verify Translation

```bash
# Translate
python mlasm.py es test.masm test.asm

# View generated ASM
cat test.asm

# Reverse to check
python mlasm.py es test.asm test_check.masm --reverse
diff test.masm test_check.masm
```

### Common Workflow

1. Write code in native language
2. Translate to NASM
3. Compile with NASM
4. Link with ld
5. Test binary

---

## 🔧 Integration with Build Systems

### Make

See `Makefile.example` in the repository.

### CMake

```cmake
function(add_mlasm_executable target lang source)
    set(ASM_FILE "${CMAKE_BINARY_DIR}/${target}.asm")
    
    add_custom_command(
        OUTPUT ${ASM_FILE}
        COMMAND python ${CMAKE_SOURCE_DIR}/mlasm.py ${lang} ${source} ${ASM_FILE}
        DEPENDS ${source}
    )
    
    # ... continue with NASM compilation
endfunction()
```

### VSCode Tasks

See [Quick Start Guide](https://github.com/cyberenigma-lgtm/MultiLang-ASM/blob/main/QUICKSTART.md#-configuraci%C3%B3n-del-editor-vscode) for VSCode integration.

---

## ❓ Troubleshooting

### "File not found" error
- Verify file paths are correct
- Use absolute paths if needed

### "Language not supported" error
- Check language code (must be one of: es, fr, de, it, ar, ru, ko, id, zh, ja)
- Ensure correct spelling

### Comments not preserved
- Comments with `;` are preserved automatically
- Multi-line comments may need adjustment

### Unicode issues on Windows
- Ensure console supports UTF-8
- Use `chcp 65001` before running

---

## 📚 Next Steps

- Read [Examples](Examples) for code samples
- Check [PRETTY Mode](PRETTY-Mode) for reverse translation details
- See [Contributing](Contributing) to add features or languages

---

**Need help?** Open an [issue](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues) or start a [discussion](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions).
