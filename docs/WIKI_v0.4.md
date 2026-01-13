# 📚 MultiLang-ASM v0.4 Wiki

Welcome to the official documentation for **MultiLang-ASM v0.4**.
This project allows you to write x86_64 assembly code in your native language.

## 🚀 Quick Links
- [GitHub Repository](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
- [Bug Reports](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)
- [Latest Release](https://github.com/cyberenigma-lgtm/MultiLang-ASM/releases)

---

## 🛠️ Installation & Setup

MultiLang-ASM is a Python-based tool. No compilation is required.

### Requirements
- **Python 3.6+**
- **NASM** (The Netwide Assembler) - To compile the output.
- **LD** (Linker) - To create the final executable.

### Installation
```bash
git clone https://github.com/cyberenigma-lgtm/MultiLang-ASM.git
cd MultiLang-ASM
```

---

## 📖 Usage Guide

MultiLang-ASM v0.4 introduces powerful new ways to interact with the tool.

### 1. Auto-Detection (Recommended)
You can let the tool detect the language automatically.

```bash
python mlasm.py auto source_file.masm
```
*Creates `source_file.asm`*

### 2. Manual Specification
If auto-detection fails or you want to force a language:

```bash
# Force Spanish (es)
python mlasm.py es source_file.masm

# Force Japanese (ja)
python mlasm.py ja source_file.masm
```

### 3. One-Step Build (Windows)
We provide a helper script for Windows users:
```bat
mlasm build es source_file.masm
```

### 4. Reverse Translation (Decompilation)
Turn standard ASM back into your native language!
```bash
# ASM -> French
python mlasm.py fr source.asm output_fr.masm --reverse
```

---

## ⚡ New Features in v0.4

### Macros (`%define`)
You can now define constants and aliases using the `%define` directive.
This runs **before** translation, so you can use it to create native-language constants.

**Example (Spanish):**
```asm
%define SALUDO "Hola"
%define SALIDA 60

mover rax, SALIDA
```

**Example (Hindi):**
```asm
%define MITRA 10
bhejo rax, MITRA
```

---

## 🌍 Supported Languages (v0.4)

| Language | Code | Support Level | Notes |
|----------|------|---------------|-------|
| 🇪🇸 Español | `es` | ⭐ Full | 80+ Instructions |
| 🇫🇷 Français | `fr` | ⭐ Full | 80+ Instructions |
| 🇩🇪 Deutsch | `de` | ⭐ Full | 80+ Instructions |
| 🇮🇹 Italiano | `it` | ⭐ Full | 80+ Instructions |
| 🇧🇷 Português | `pt` | ⭐ Full | 80+ Instructions |
| 🇷🇺 Русский | `ru` | ⭐ Full | 80+ Instructions |
| 🇯🇵 日本語 | `ja` | ⭐ Full | 80+ Instructions |
| 🇨🇳 中文 | `zh` | ⭐ Full | 80+ Instructions |
| 🇰🇷 한국어 | `ko` | ⭐ Full | 80+ Instructions |
| 🇸🇦 العربية | `ar` | ⭐ Full | RTL Support |
| 🇮🇩 Bahasa | `id` | ⭐ Full | 80+ Instructions |
| 🇮🇳 Hindi | `hi` | 🔷 Core+ | Logic + Flow + Arith |
| 🇹🇷 Türkçe | `tr` | 🔷 Core+ | Logic + Flow + Arith |
| 🇵🇱 Polski | `pl` | 🔷 Core+ | Logic + Flow + Arith |
| 🇸🇪 Svenska | `sv` | 🔷 Core+ | Logic + Flow + Arith |
| 🇳🇱 Nederlands | `nl` | 🔷 Core+ | Logic + Flow + Arith |

*(Full = All standard x86 user-mode instructions including MMX/SSE placeholders)*
*(Core+ = Essential instructions for OS/Kernel development: mov, logic, math, stack, flow)*

---

## 🧩 Examples

We have generated "Hello World" examples for **every supported language** in the `examples/` directory.

### Running an example
```bash
python mlasm.py auto examples/hello_es.masm
nasm -f elf64 examples/hello_es.asm -o hello.o
ld hello.o -o hello
./hello
```

---

## ⚠️ Troubleshooting & Common Problems

### 1. "Unknown Instruction" Error
**Problem:** The tool crashes or reports an error translating a line.
**Solution:**
- Check for typos in your native keyword.
- Ensure the instruction is supported (check `docs/INSTRUCCIONES_XX.md`).
- If usage appears correct, open an Issue; the dictionary might miss a synonym.

### 2. Encoding Issues (UnicodeDecodeError)
**Problem:** Python crashes when reading Asian, Cyrillic, or Arabic characters.
**Solution:**
- Always confirm your file is saved as **UTF-8**.
- On Windows PowerShell, you may need `chcp 65001`.

### 3. NASM Errors after Translation
**Problem:** `mlasm.py` succeeds, but `nasm` fails to compile the output.
**Solution:**
- `mlasm` does not validate ASM syntax, it only translates keywords.
- Check argument order (`mov dest, src`).
- Ensure labels are valid (no spaces, special chars allowed by NASM).

### 4. Macro Recursion
**Problem:** Using `%define A B` and `%define B A` freezes the tool.
**Solution:**
- Do not create circular definitions.
- The macro engine is simple and does not support arguments (like C macros) yet.

---

## 🤝 Contributing

We welcome contributions!
- **Add a Language:** Edit `mlasm.py` and add to the `TABLE`.
- **Fix a Translation:** Submit a Pull Request.

**Full Change Log:** [CHANGELOG.md](../CHANGELOG.md)
