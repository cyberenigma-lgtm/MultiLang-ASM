# 🛡️ MultiLang-ASM v0.4

> *"Den första flerspråkiga x86_64-assemblern."*

**Skriv assembler på ditt modersmål.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Svenska** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Vad är detta?

MultiLang-ASM låter dig skriva x86_64-assembler med nyckelord på **Svenska**.
Den översätter automatiskt din kod till standard NASM-assembler.

## ✨ Funktioner

- 🌍 **Skriv på Svenska** (sv)
- 🤖 **Automatisk Detektering:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Svenska <-> ASM`

## 📖 Svenskt Exempel

### Source Code (`hello.masm`)
```asm
flytta rax, 1
flytta rdi, 1
flytta rsi, msg
flytta rdx, 13
syscall

flytta rax, 60
flytta rdi, 0
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

## 🛠️ Användning

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
