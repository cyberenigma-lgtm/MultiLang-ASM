# 🛡️# MultiLang-ASM
**The first multilingual x86_64 assembler.**  
Write assembly in your native language · 10 languages · 80+ instructions · reversible translation · NASM-compatible.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-10-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/INSTRUCCIONES_ES.md)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)

📖 **English** | **[Español](README_ES.md)**

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
- 🌍 **10 languages supported** (Spanish, French, German, Italian, Russian, Arabic, Korean, Indonesian, Chinese, Japanese)
- 🔁 **Reversible translation** (ASM → Language → ASM)  
- 🧩 **80+ instructions mapped**  
- 🛠️ **NASM/FASM/GAS compatible output**  
- 📚 **Full documentation per language**  
- 🧪 **Examples and tests included**  
- 🔌 **Easy integration with Make, CMake, CI/CD**  

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
| v0.3 | More languages, PRETTY expansion | 🔄 In progress |
| v0.4 | Macro support, VSCode plugin | 📋 Planned |
| v0.5 | Web playground, ARM support | 📋 Planned |
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

**Version:** v0.2  
**Author:** J / Neuro-OS Project  
**Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

🛡️ **Part of the [Neuro-OS](https://neuro-os.es) ecosystem**
