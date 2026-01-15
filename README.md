# MultiLang-ASM
**The first multilingual x86_64 assembler.**  

Write assembly in your native language · 16 languages · 80+ instructions · reversible translation · NASM-compatible.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/INSTRUCCIONES_ES.md)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

📖 **[English](README.md)** | **[Español](README_ES.md)** | **[Français](README_FR.md)** | **[Deutsch](README_DE.md)** | **[Italiano](README_IT.md)** | **[Português](README_PT.md)** | **[Русский](README_RU.md)** | **[日本語](README_JA.md)** | **[中文](README_ZH.md)** | **[한국어](README_KO.md)** | **[العربية](README_AR.md)** | **[Bahasa](README_ID.md)** | **[Hindi](README_HI.md)** | **[Türkçe](README_TR.md)** | **[Polski](README_PL.md)** | **[Svenska](README_SV.md)** | **[Nederlands](README_NL.md)**

---

## 🚀 What is MultiLang-ASM?

MultiLang-ASM is the world's first multilingual assembler layer for x86_64.  
It allows developers to write assembly code using natural language keywords in their own language, and automatically translates it into standard NASM-compatible assembly.

It also supports **reverse translation**, allowing developers to view standard ASM in any supported language.

**Example:**
```asm
; Spanish
mover rax, 1
llamada_sistema

; Translates to →
mov rax, 1
syscall
```

---

## ✨ Features

- 🧠 **Write assembly in your native language**
- 🌍 **16 languages supported** (Includes: Hindi, Turkish, Polish, Swedish, Dutch)
- 🤖 **Auto-Detection** of source language
- ⚡ **Macros** (%define) support
- 🔁 **Reversible translation** (ASM → Language → ASM)
- 🧩 **80+ instructions mapped** (Full support for 11 core languages, Essentials for 5 new)
- 🛠️ **NASM/FASM/GAS compatible output**  
- 📚 **Full documentation per language**  
- 🧪 **Examples and tests included**  
- 🔌 **Easy integration with Make, CMake, CI/CD**

## 🔥 What's New in v0.5 (Released)

### 🧸 Kids Mode (Modo Niños)
**New!** We have moved the educational suite to its own dedicated home.
👉 **[Visit MultiLang-ASM Kids Repository](https://github.com/cyberenigma-lgtm/MultiLang-ASM-Kids)**

- 📚 **[Kids Wiki & Guide](https://github.com/cyberenigma-lgtm/MultiLang-ASM-Kids/wiki)**
- 🎮 **[Exercises & Examples](https://github.com/cyberenigma-lgtm/MultiLang-ASM-Kids/tree/main/examples)**
- 🏫 **Teacher Resources**

Simplified syntax for 27 languages:
```asm
; Kids Mode (Spanish)
pon rax a 5
suma rax con 3
enseña rax
```

### 🛡️ Professional Mode
Full x86-64 support mapped to native keywords. Now supports stack (`push`/`pop`), logic (`and`/`or`/`xo`/`not`), and control flow (`loop`/`je`/`jne`).

### 🎭 Global Dialects
Preserve cultural identity with dialect support:
- **English**: Cockney, Aussie, Texan...
- **Spanish**: Andaluz, Madrileño...
- **German**: Bavarian, Swiss...
- **Japanese**: Kansai-ben...

### 🌍 11 New Languages
Added 10 new languages + dialects: Greek, Hebrew, Thai, Vietnamese, Swahili, Tagalog, Malay, Persian, Ukrainian, Romanian...

## 🔥 What's New in v0.4 (Released)

### 🤖 Smart Language Auto-Detection
You no longer need to specify the language manually. MultiLang-ASM analyzes your code and detects the source language with high accuracy.

```bash
# Before (v0.3)
python mlasm.py es program.masm

# Now (v0.4)
python mlasm.py auto program.masm
```

### ⚡ Macros (`%define`)
Basic preprocessor support. Define constants or aliases in your own language.

```asm
; Spanish
%define HELLO 0x1
mover eax, HELLO

; Hindi
%define RAKHO 0x1
bhejo eax, RAKHO
```

### 🌍 5 New Languages (Beta)
Added 5 new languages with "Core+" support (Essential logic, arithmetic, and flow control):

- 🇮🇳 **Hindi (`hi`)**: `bhejo` (mov), `joro` (add), `kudo` (jmp)...
- 🇹🇷 **Turkish (`tr`)**: `taşı` (mov), `ekle` (add), `atla` (jmp)...
- 🇵🇱 **Polish (`pl`)**: `przesun` (mov), `dodaj` (add), `skocz` (jmp)...
- 🇸🇪 **Swedish (`sv`)**: `flytta` (mov), `addera` (add), `hoppa` (jmp)...
- 🇳🇱 **Dutch (`nl`)**: `verplaats` (mov), `optellen` (add), `spring` (jmp)...

These languages include full support for logic (`AND`/`OR`/`XOR`/`NOT`) and comparison (`CMP`/`TEST`).  

---

## 📦 Quick Start

### Translate and compile:

```bash
python mlasm.py es programa.masm programa.asm
nasm -f elf64 programa.asm -o programa.o
ld programa.o -o programa
./programa
```

### One-step build (with helper script):
```bash
mlasm build es programa.masm
```

---

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
| 🇧🇷 Português | `pt` | ✅ Complete | 80+ |
| 🇮🇳 Hindi | `hi` | ✅ beta | Core+ |
| 🇹🇷 Turkish | `tr` | ✅ beta | Core+ |
| 🇵🇱 Polish | `pl` | ✅ beta | Core+ |
| 🇸🇪 Swedish | `sv` | ✅ beta | Core+ |
| 🇳🇱 Dutch | `nl` | ✅ beta | Core+ |
| 🇬🇷 Greek | `el` | ✅ beta | Core+ |
| 🇮🇱 Hebrew | `he` | ✅ beta | Core+ |
| 🇹🇭 Thai | `th` | ✅ beta | Core+ |
| 🇻🇳 Vietnamese | `vi` | ✅ beta | Core+ |
| 🇰🇪 Swahili | `sw` | ✅ beta | Core+ |
| 🇵🇭 Tagalog | `tl` | ✅ beta | Core+ |
| 🇲🇾 Malay | `ms` | ✅ beta | Core+ |
| 🇮🇷 Persian | `fa` | ✅ beta | Core+ |
| 🇺🇦 Ukrainian | `uk` | ✅ beta | Core+ |
| 🇷🇴 Romanian | `ro` | ✅ beta | Core+ |

Want your language? Open an [issue](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)!

---

## 📁 Project Structure

```
MultiLang-ASM/
├── mlasm.py              # Core translation engine
├── docs/                 # Language-specific documentation
│   ├── INSTRUCCIONES_ES.md
│   ├── INSTRUCCIONES_FR.md
│   └── ...
├── mlasm.bat             # Windows helper script
├── Makefile.example      # Build system integration
├── demo_es.masm          # Spanish example
├── demo_fr.masm          # French example
└── README.md             # This file
```

---

## 🤝 Contribute

MultiLang-ASM is open to contributors from all over the world.

**You can help by:**
- 🌍 Adding new languages
- 📝 Improving keyword mappings
- 🔄 Expanding PRETTY reversible mode
- 📚 Writing examples in your language
- 🐛 Reporting bugs or suggesting improvements
- ⭐ Giving us a star

**See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.**

Issues labeled `good first issue` are perfect for first-time contributors.

---

## 🗺️ Roadmap

| Version | Features | Status |
|---------|----------|--------|
| v0.2 | 10 languages, 80+ instructions, reversible mode | ✅ Released |
| v0.3 | PRETTY expansion for all 10 languages, 80+ Instr | ✅ Released |
| v0.4 | Auto-detection, tests, macros, 16 languages | ✅ Released |
| v0.5 | VSCode plugin, Kids Mode, 27 Languages, Global Dialects | ✅ Released |
| v0.6 | Community platform, language packs, contributor system | 📋 Planned |
| v1.0 | Stable release, full test coverage | 📋 Planned |

---

## 📚 Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Vision & Architecture](VISION_Y_ARQUITECTURA.md) - Technical deep dive
- [Collaborators Guide](COLLABORATORS.md) - How to manage contributors
- [Changelog](CHANGELOG.md) - Version history
- [Release Notes](RELEASE.md) - v0.2 details

### Instruction References (by language)
- 🇪🇸 [Español](docs/INSTRUCCIONES_ES.md)
- 🇫🇷 [Français](docs/INSTRUCCIONES_FR.md)
- 🇩🇪 [Deutsch](docs/INSTRUCCIONES_DE.md)
- 🇮🇹 [Italiano](docs/INSTRUCCIONES_IT.md)
- 🇸🇦 [العربية](docs/INSTRUCCIONES_AR.md)
- 🇷🇺 [Русский](docs/INSTRUCCIONES_RU.md)
- 🇰🇷 [한국어](docs/INSTRUCCIONES_KO.md)
- 🇮🇩 [Bahasa](docs/INSTRUCCIONES_ID.md)
- 🇨🇳 [中文](docs/INSTRUCCIONES_ZH.md)
- 🇯🇵 [日本語](docs/INSTRUCCIONES_JA.md)
- 🇧🇷 [Português](docs/MULTILANG_ASM_PTBR.md)

---

## 💡 Why MultiLang-ASM?

Not knowing English shouldn't be a barrier to learning low-level programming.

MultiLang-ASM removes that artificial barrier and opens the door to:
- Students learning in their mother tongue
- Self-taught developers without formal English education
- Communities currently excluded from systems programming

**It's code. It's justice. It's the future.**

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Thanks to all contributors who help democratize low-level programming.

**Special thanks to the open-source community for making this possible.**

---

## 📧 Contact

**Email:** neuro.so.ia.sim@gmail.com  
**Issues:** [GitHub Issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)  
**Discussions:** [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions)

---

**Version:** v0.5 (Babel Release)  
**Author:** J / Neuro-OS Project  
**Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

🛡️ **Part of the [Neuro-OS](https://neuro-os.es) ecosystem**
