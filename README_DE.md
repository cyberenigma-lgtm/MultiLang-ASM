# 🛡️ MultiLang-ASM v0.4

> *"Der erste mehrsprachige x86_64-Assembler."*

**Schreiben Sie Assembler in Ihrer Muttersprache.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Deutsch** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Was ist das?

Mit MultiLang-ASM können Sie x86_64-Assembly mit Schlüsselwörtern auf **Deutsch** schreiben.
Es übersetzt Ihren Code automatisch in Standard-NASM-Assembly.

## ✨ Funktionen

- 🌍 **Auf Deutsch schreiben** (de)
- 🤖 **Auto-Erkennung:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Deutsch <-> ASM`

## 📖 Beispiel auf Deutsch

### Source Code (`hello.masm`)
```asm
bewegen rax, 1
bewegen rdi, 1
bewegen rsi, msg
bewegen rdx, 13
syscall

bewegen rax, 60
bewegen rdi, 0
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

## 🛠️ Verwendung

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
