# MultiLang-ASM v1.0.0
<p align="center">
  <img src="assets/logo.png" alt="MultiLang-ASM Logo" width="800">
</p>

**The world's first sovereign multilingual x86_64 assembler engine.**  
Part of the **UPL (Universal Polyglot Layer)** Ecosystem & Neuro-OS Core.

Write assembly in your native language · 150 World Languages & Dialects · 200+ x86_64 Instructions · 100% ANSI C99 Native Engine · Zero Python Runtime Dependencies · Instant Execution (<2 ms) · NASM-compatible.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Standard: ANSI C99](https://img.shields.io/badge/Standard-ANSI%20C99-blue.svg)](src/)
[![Languages](https://img.shields.io/badge/languages-150%20Global-success.svg)](LISTA_PAISES_LENGUAS.md)
[![Instructions](https://img.shields.io/badge/instructions-200%2B%20x86__64-brightgreen.svg)](docs/INSTRUCCIONES_ES.md)
[![Ecosystem: UPL+](https://img.shields.io/badge/Ecosystem-UPL%2B%20Sovereign-purple.svg)](https://github.com/cyberenigma-lgtm/UNIVERSAL-POLYGLOT-LAYER-UPL)

📖 **[English](README.md)** | **[Español](README_ES.md)** | **[Français](README_FR.md)** | **[Deutsch](README_DE.md)** | **[Italiano](README_IT.md)** | **[Português](README_PT.md)** | **[Русский](README_RU.md)** | **[日本語](README_JA.md)** | **[中文](README_ZH.md)** | **[한국어](README_KO.md)** | **[العربية](README_AR.md)** | **[Bahasa](README_ID.md)** | **[Hindi](README_HI.md)** | **[Türkçe](README_TR.md)** | **[Polski](README_PL.md)** | **[Svenska](README_SV.md)** | **[Nederlands](README_NL.md)**

---

## 🚀 What is MultiLang-ASM?

MultiLang-ASM is an ultra-fast, zero-dependency multilingual assembler and preprocessor for **x86_64**.  
It enables systems engineers, students, kernel developers, and makers worldwide to write low-level code in their mother tongue, instantly transpiling to standard NASM syntax.

Originally prototyped in Python, **version 1.0.0 is rewritten from the ground up as a pure ANSI C99 native engine**, eliminating all Python runtime requirements and achieving sub-millisecond translation speeds.

### Bidirectional Example (Spanish ↔ Standard NASM)

```asm
; Spanish Input (hello_es.masm)
mover rax, 1
mover rdi, 1
mover rsi, msg
mover rdx, 13
llamada_sistema

; Native mlasm compilation → Standard NASM
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 13
syscall
```

---

## ✨ Features (v1.0.0 UPL Edition)

- ⚡ **100% Standalone ANSI C99 Engine**: Zero dependencies. Compiles to an ultra-compact binary (<80 KB) with any C99 compiler (`gcc`, `clang`, `tcc`, `msvc`).
- 🌍 **150 World Languages**: Full coverage of all 5 continents (Europe, Americas, Africa, Asia, Oceania), including indigenous and regional tongues.
- ⚙️ **200+ Instructions**: Complete x86_64 coverage (Data movement, Arithmetic, Logic, Bit manipulation, Flags, Strings, Loops, System calls, Descriptor tables, and FPU/x87).
- 🤖 **Instant Auto-Detection**: Automatically identifies source language from keyword frequency (`mlasm auto file.masm`).
- 🔁 **Reversible (PRETTY) Mode**: View standard NASM assembly in any of the 150 supported languages (`--reverse`).
- 🧠 **Native Macro Preprocessor**: First-class `%define` constant substitution handled in C.
- 🛡️ **Pass-Through Architecture**: Any instruction not in the dictionary (e.g. `cpuid`, `rdtsc`) passes through to NASM untouched.
- 📦 **Direct Build Pipeline**: One-command compilation from multilingual ASM directly to executable binary (`mlasm --build <lang> <file.masm>`).

---

## 🛠️ Quick Start

### 1. Build the Native Engine

**On Windows:**
```cmd
gcc -std=c99 -O2 src/mlasm_core.c -I src -o bin/mlasm.exe
```
*(Or simply run `mlasm.bat`, which auto-compiles the binary on first run).*

**On Linux / macOS:**
```bash
make
# or: gcc -std=c99 -O2 src/mlasm_core.c -I src -o bin/mlasm
```

### 2. Usage

```bash
# Basic Transpilation:
mlasm es examples/hello_es.masm -o hello_es.asm

# Automatic Language Detection:
mlasm auto examples/hello_zh.masm -o hello_zh.asm

# Reverse Translation (NASM -> Native Language):
mlasm --reverse ru program.asm -o program_ru.masm

# Build Directly to Executable (Transpiles + NASM + GCC):
mlasm --build es examples/hello_es.masm

# Run Internal Native Test Suite:
mlasm --test

# List All 150 Supported Languages:
mlasm --list-langs
```

---

## 🗺️ Supported Languages (150 Global Coverage)

See the comprehensive [Country & Language Directory (LISTA_PAISES_LENGUAS.md)](LISTA_PAISES_LENGUAS.md) for detailed regional classifications across:
- **Europe (46 languages)**: Spanish, Catalan, Galician, Basque, Asturian, Aragonese, Occitan, French, German, Italian, Portuguese, English, Irish, Scottish Gaelic, Welsh, Dutch, Danish, Swedish, Norwegian, Finnish, Polish, Czech, Slovak, Hungarian, Romanian, Bulgarian, Greek, Latin, Esperanto, Russian, Ukrainian, etc.
- **Americas (16 languages)**: Latin American Spanish dialects, Quechua, Aymara, Nahuatl, Maya, Guarani, Cherokee, Navajo, Inuktitut, Greenlandic, Hawaiian, etc.
- **Africa (36 languages)**: Swahili, Amharic, Oromo, Tigrinya, Somali, Hausa, Yoruba, Igbo, Fula, Wolof, Akan, Lingala, Kongo, Kinyarwanda, Kirundi, Shona, Chichewa, Zulu, Xhosa, Afrikaans, etc.
- **Asia & Oceania (52 languages)**: Mandarin, Cantonese, Japanese, Korean, Vietnamese, Thai, Khmer, Burmese, Indonesian, Javanese, Tagalog, Cebuano, Hindi, Urdu, Bengali, Punjabi, Marathi, Gujarati, Tamil, Telugu, Kannada, Malayalam, Persian, Pashto, Kurdish, Hebrew, Arabic, Turkish, Kazakh, Uzbek, Mongolian, Maori, Samoan, Fijian, Tok Pisin, etc.

---

## 🧪 Testing and Validation

MultiLang-ASM includes a native validation suite:
```bash
# Windows
test.bat

# Linux / macOS
./test.sh
```
All 9 core validation tests and 150 language mappings execute in under 5 ms with 0 failures.

---

## 📜 Sovereign Philosophy

> *"Not knowing English should never be a barrier to systems programming. The machine speaks binary; how humans express intent is a sovereign right."*

MultiLang-ASM is free and open-source software under the **MIT License**.  
Part of the **UPL (Universal Polyglot Layer)** and **Neuro-OS** ecosystems.
