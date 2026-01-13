# 🛡️ MultiLang-ASM v0.4

> *"Pierwszy wielojęzyczny asembler x86_64."*

**Pisz w asemblerze w swoim ojczystym języku.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Polski** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Co to jest?

MultiLang-ASM umożliwia pisanie w asemblerze x86_64 przy użyciu słów kluczowych w języku **Polskim**.
Automatycznie tłumaczy Twój kod na standardowy asembler NASM.

## ✨ Funkcje

- 🌍 **Pisz po Polsku** (pl)
- 🤖 **Wykrywanie Auto:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Polski <-> ASM`

## 📖 Przykład po Polsku

### Source Code (`hello.masm`)
```asm
przesun rax, 1
przesun rdi, 1
przesun rsi, msg
przesun rdx, 13
syscall

przesun rax, 60
przesun rdi, 0
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

## 🛠️ Użycie

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
