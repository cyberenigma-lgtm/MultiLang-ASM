# 🛡️ MultiLang-ASM v0.4

> *"De eerste meertalige x86_64 assembler."*

**Schrijf assembler in je moedertaal.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Nederlands** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Wat is dit?

Met MultiLang-ASM kun je x86_64 assembler schrijven met trefwoorden in het **Nederlands**.
Het vertaalt je code automatisch naar standaard NASM assembler.

## ✨ Functies

- 🌍 **Schrijf in het Nederlands** (nl)
- 🤖 **Automatische Detectie:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Nederlands <-> ASM`

## 📖 Nederlands Voorbeeld

### Source Code (`hello.masm`)
```asm
verplaats rax, 1
verplaats rdi, 1
verplaats rsi, msg
verplaats rdx, 13
syscall

verplaats rax, 60
verplaats rdi, 0
syscall
```

### Generates Standard ASM
```asm
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 13
syscall

mov rax, 60
mov rdi, 0
syscall
```

## 🛠️ Gebruik

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
