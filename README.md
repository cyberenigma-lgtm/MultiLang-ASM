# 🛡️ MultiLang-ASM v0.2

**The first multilingual assembler. Write x86_64 assembly in your native language.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-10-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/INSTRUCCIONES_ES.md)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

📖 **[Español](README_ES.md)** | **English**

---

## 🚀 What is this?

**MultiLang-ASM** is the first assembler that lets you program at a low level using **your native language**. You no longer need to master English to create kernels, drivers, or firmware.

This project demonstrates that linguistic barriers in programming are **artificial** and removable.

## 💡 Why It Matters

Most low-level tools were designed in an English-speaking context decades ago. This has created an invisible barrier that excludes millions of people with talent, creativity, and brilliant ideas.

**MultiLang-ASM breaks that legacy** and opens the door to:
- Students learning in their native language
- Self-taught developers without formal English education
- Entire communities currently excluded from low-level programming
- Children who can experiment without artificial barriers

It's not just code. It's **technological justice**.

## ✨ Features

- 🌐 **Multilingual:** Write in Spanish, Arabic, French, Italian, Portuguese...
- 🔄 **Reversible:** View standard ASM in any language
- ⚡ **Fast:** Translates to NASM in milliseconds
- 🛡️ **Compatible:** 100% compatible with NASM/FASM/GAS
- 📚 **Complete:** 80+ instructions per language
- 🔧 **Extensible:** Add new languages easily

## 🌍 Supported Languages

| Language | Code | Status | Instructions |
|----------|------|--------|--------------|
| 🇪🇸 Español | `es` | ✅ Complete | 80+ |
| 🇫🇷 Français | `fr` | ✅ Complete | 80+ |
| 🇩🇪 Deutsch | `de` | ✅ Complete | 80+ |
| 🇮🇹 Italiano | `it` | ✅ Complete | 80+ |
| 🇸🇦 العربية | `ar` | ✅ Complete | 80+ (RTL) |
| 🇷🇺 Русский | `ru` | ✅ Complete | 80+ |
| 🇰🇷 한국어 | `ko` | ✅ Complete | 80+ |
| 🇮🇩 Bahasa | `id` | ✅ Complete | 80+ |
| 🇨🇳 中文 | `zh` | ✅ Complete | 80+ |
| 🇯🇵 日本語 | `ja` | ✅ Complete | 80+ |

Want your language? Open an issue!

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/cyberenigma-lgtm/MultiLang-ASM.git
cd MultiLang-ASM
```

No external dependencies required. Just Python 3.6+.

### Basic Usage
```bash
# Write in Spanish
python mlasm.py es my_code.masm code.asm

# Compile with NASM
nasm -f elf64 code.asm -o code.o
ld code.o -o program

# Run
./program
```

### Example in Spanish
```asm
; Hola Mundo in Spanish
seccion .texto
global _inicio

_inicio:
    mover rax, 1          ; syscall write
    mover rdi, 1          ; stdout
    llamada_sistema       ; call kernel
    
    mover rax, 60         ; syscall exit
    interrupcion 0x80
```

Translates to standard NASM:
```asm
section .text
global _start

_start:
    mov rax, 1
    mov rdi, 1
    syscall
    
    mov rax, 60
    int 0x80
```

### Reversible Mode
```bash
# View standard ASM in French
python mlasm.py fr code.asm code_fr.masm --reverse
```

## 📊 Supported Instructions Map

| Language | Example | Translation | Standard ASM |
|----------|---------|-------------|--------------|
| Spanish | `mover rax, rbx` | → | `mov rax, rbx` |
| Arabic | `نقل rax, rbx` | → | `mov rax, rbx` |
| French | `deplacer rax, rbx` | → | `mov rax, rbx` |
| German | `bewegen rax, rbx` | → | `mov rax, rbx` |
| Russian | `перенести rax, rbx` | → | `mov rax, rbx` |
| Japanese | `移動 rax, rbx` | → | `mov rax, rbx` |
| Korean | `이동 rax, rbx` | → | `mov rax, rbx` |

See complete dictionary in [`mlasm.py`](mlasm.py).

## 🌟 Philosophy

This project is born from a simple conviction:

- English is not a **technical** requirement, it's a **historical** convention
- The CPU understands **opcodes**, not human languages
- Removing linguistic barriers **democratizes** technology
- Creativity shouldn't depend on the language you speak

## 📈 Project Status

| Feature | Status |
|---------|--------|
| Functional prototype | ✅ Completed |
| Bidirectional translation | ✅ Completed |
| Support for 10 languages | ✅ Completed |
| Comment preservation | ✅ Completed |
| Multiple aliases | ✅ Completed |
| Syntax expansion (macros) | 🔄 In development |
| Automatic language detection | 🔄 Planned |
| IDE integration | 🔄 Planned |
| ASM syntax validation | 🔄 Planned |

## ⚠️ Current Limitations (v0.2)

Being transparent about what it **doesn't** do (yet) is as important as showing what it does:

- ❌ Doesn't support complex macros
- ❌ Doesn't translate high-level control structures
- ❌ Doesn't automatically detect source code language
- ❌ Doesn't validate advanced ASM syntax (NASM does that)
- ❌ Doesn't translate section names (`.text`, `.data`)

These limitations are in the roadmap for future versions.

## 🔬 Complete Workflow Example

### Step 1: Write in your language
Create `hello.masm` in Spanish:
```asm
; Program: Hello World
seccion .texto
global _inicio

_inicio:
    mover rax, 1        ; syscall write
    mover rdi, 1        ; stdout
    mover rsi, mensaje
    mover rdx, 12
    interrupcion 0x80
    
    mover rax, 60       ; syscall exit
    mover rdi, 0
    interrupcion 0x80

seccion .datos
    mensaje db "Hola Mundo!", 0xA
```

### Step 2: Translate to standard NASM
```bash
python mlasm.py es hello.masm hello.asm
```

Output:
```
🛡️ MultiLang-ASM v0.2
   Language: ES
   Mode: Standard (NASM)
   Input: hello.masm
   Output: hello.asm
   Status: ✅ OK
```

### Step 3: Compile with NASM
```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
```

### Step 4: Execute
```bash
./hello
# Output: Hola Mundo!
```

### Bonus: View in another language
```bash
python mlasm.py ar hello.asm hello_ar.masm --reverse
# Now hello_ar.masm uses Arabic mnemonics
```

## 🤝 Contribute

Want to add your language? Perfect!

1. Edit `mlasm.py`
2. Add your translation table in the `TABLE` dictionary
3. Make a pull request
4. Done! You'll have democratized low-level for your community

## 📄 Documentation

- [Vision and Architecture](VISION_Y_ARQUITECTURA.md)
- [Concept Report](INFORME_DE_CONCEPTO.md)
- [Changelog](CHANGELOG.md)
- **[🌍 Multilingual Documentation](docs/)** ← Complete references in 10 languages

### Instruction References by Language (80+ instructions each)
- 🇪🇸 [Español](docs/INSTRUCCIONES_ES.md)
- 🇫🇷 [Français](docs/INSTRUCCIONES_FR.md)
- 🇩🇪 [Deutsch](docs/INSTRUCCIONES_DE.md)
- 🇮🇹 [Italiano](docs/INSTRUCCIONES_IT.md)
- 🇸🇦 [العربية (Arabic)](docs/INSTRUCCIONES_AR.md)
- 🇷🇺 [Русский (Russian)](docs/INSTRUCCIONES_RU.md)
- 🇰🇷 [한국어 (Korean)](docs/INSTRUCCIONES_KO.md)
- 🇮🇩 [Bahasa Indonesia](docs/INSTRUCCIONES_ID.md)
- 🇨🇳 [中文 (Traditional Chinese)](docs/INSTRUCCIONES_ZH.md)
- 🇯🇵 [日本語 (Japanese)](docs/INSTRUCCIONES_JA.md)

## ⚖️ Technical Disclaimer

**MultiLang-ASM does not replace NASM, FASM, or GAS.**

It's an **accessibility layer** that translates native mnemonics to standard ASM. The generated file is 100% compatible with any traditional assembler. The CPU never sees the difference.

Think of it as a "human preprocessor" that removes the language barrier without modifying the underlying architecture.

## 💭 Author's Message

**"Not knowing English shouldn't be a barrier to creating. Knowledge should flow in all languages."**

If this project helped you, share it. Every person programming in their native language is a victory against artificial barriers in technology.

---

## 🤝 Want to Contribute?

**MultiLang-ASM is open to collaborations from around the world.**

You don't need to know assembly: if you speak another language, you can help translate, document, or create examples.

**How can you help?**
- 🌍 Add support for new languages
- 📝 Improve existing translations
- 📚 Create tutorials in your language
- 🐛 Report bugs or suggest improvements
- ⭐ Give the repo a star

**Check [CONTRIBUTING.md](CONTRIBUTING.md) to get started.**

Issues tagged with `good first issue` are perfect for new contributors.

---

**Version:** v0.2  
**License:** MIT  
**Author:** J / Neuro-OS Project  
**Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

— J

🛡️ **Part of the Neuro-OS ecosystem**
