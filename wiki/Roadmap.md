# Roadmap

Future plans and version timeline for MultiLang-ASM.

---

## 🚀 Version History

| Version | Release Date | Status | Highlights |
|---------|--------------|--------|------------|
| v0.1 | 2024-12 | ✅ Released | Initial prototype, 3 languages |
| v0.2 | 2025-12 | ✅ Released | 10 languages, 80+ instructions |
| v0.3 | 2025-12 | ✅ Released | PRETTY expansion for all languages |
| v0.6 | Feb 2026 | ✅ Released | Modular Architecture (Babel Edition) |
| v0.7 | Feb 2026 | ✅ Released | Global Expansion (25+ Languages) |
| v1.0 | Q3 2026 | 📋 Planned | Stable release, production-ready |

---

## ✅ v0.3 (Current) - Released 2025-12-25

**Focus:** Complete PRETTY Mode

### Features Delivered
- ✅ PRETTY reverse mapping for all 10 languages
- ✅ 540+ new reverse translations
- ✅ Full bidirectional translation support
- ✅ Improved international collaboration

---

## 🔄 v0.4 - Planned Q1 2026

**Focus:** Intelligence & Quality

### Planned Features

#### 1. Automatic Language Detection ⭐
```bash
# Old way
python mlasm.py es programa.masm programa.asm

# New way
python mlasm.py auto programa.masm programa.asm
```
Analyzes code to detect language automatically.

#### 2. Comprehensive Test Suite ⭐
- 20+ pytest tests
- Coverage for all languages
- CI/CD with GitHub Actions
- Regression testing

#### 3. Multilingual Error Messages
Error messages in the user's language:
```
❌ Error: No se encontró el archivo 'programa.masm'  (Spanish)
❌ Erreur: Fichier 'programme.masm' introuvable      (French)
❌ Fehler: Datei 'programm.masm' nicht gefunden      (German)
```

#### 4. Basic Macro Support
Simple macros that expand inline:
```asm
%macro guardar_contexto
    meter rbp
    mover rbp, rsp
%endmacro
```

### Timeline
- **Planning:** December 2025
- **Development:** January-February 2026
- **Release:** March 2026

---

## 🌟 v0.5 - Planned Q2 2026

**Focus:** Developer Experience

### Planned Features

#### 1. VSCode Extension
- Syntax highlighting for `.masm` files
- IntelliSense for native mnemonics
- One-click translation
- Integrated error checking

#### 2. Web Playground
Interactive online translator:
- Live translation preview
- All languages supported
- Share code snippets
- No installation required

####  3. More Languages
Target: +5 languages
- 🇵🇹 Portuguese
- 🇹🇷 Turkish
- 🇵🇱 Polish
- 🇻🇳 Vietnamese
- 🇹🇭 Thai

#### 4. Enhanced Error Detection
- Syntax validation
- Register usage warnings
- Best practices hints

### Timeline
- **Development:** April-May 2026
- **Beta:** May 2026
- **Release:** June 2026

---

## 🎯 v1.0 - Planned Q3 2026

**Focus:** Stability & Maturity

### Goals for 1.0

- ✅ 100% test coverage
- ✅ Zero known critical bugs
- ✅ Complete documentation
- ✅ 15+ languages supported
- ✅ VSCode extension mature
- ✅ Active community
- ✅ Production deployments proven

### Features

#### 1. Advanced Macro System
- Parameters support
- Conditional macros
- Include files
- Macro libraries

#### 2. Multi-File Projects
```bash
mlasm project build --lang es --output kernel.bin
```

#### 3. ARM Support (Experimental)
Initial ARM64 translation support.

#### 4. Lint/Validation
- Full ASM syntax checking
- Optimization suggestions
- Security warnings

### Timeline
- **Development:** July-August 2026
- **RC:** August 2026
- **Release:** September 2026

---

## 🔮 Beyond v1.0

### Long-Term Vision (2027+)

#### More Architectures
- RISC-V support
- MIPS support
- PowerPC support

#### AI-Powered Features
- Automatic comment translation
- Code explanation in native language
- Intelligent autocomplete

#### Ecosystem Growth
- Package manager for macro libraries
- Community code repository
- Educational platform integration

#### Mobile Support
- Android app
- iOS app
- Tablet-optimized UI

---

## 📊 Community-Driven Features

Features will be prioritized based on:
1. User requests (GitHub Issues/Discussions)
2. Contribution offers
3. Impact on accessibility
4. Technical feasibility

**Want to influence the roadmap?**
- Vote on [feature requests](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
- Propose new features
- Contribute code

---

## ⏱️ Release Cadence

**Target Schedule:**
- Major version: Every 6 months
- Minor updates: Every 2-3 months
- Patches: As needed

**Quality Gates:**
- All  tests passing
- No regression in existing features
- Documentation up to date
- Community feedback incorporated

---

## 🤝 How to Contribute to Roadmap

### Propose a Feature
1. Check existing [issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)
2. Open new issue with `enhancement` label
3. Describe use case and expected behavior
4. Community discussion

### Vote on Features
- 👍 reactions on issues indicate support
- High-voted features are prioritized

### Implement Features
See [Contributing](Contributing) to start coding.

---

## 📢 Stay Updated

- **GitHub Releases:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/releases
- **Discussions:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions
- **Email:** neuro.so.ia.sim@gmail.com

---

**Last Updated:** 2025-12-25  
**Current Version:** v0.3
