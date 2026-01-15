# 🛡️ MultiLang-ASM v0.4

> *"Первый многоязычный ассемблер x86_64."*

**Пишите на ассемблере на своем родном языке.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Русский** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Что это?

MultiLang-ASM позволяет писать ассемблерный код x86_64, используя ключевые слова на **Русском**.
Он автоматически переводит ваш код в стандартный ассемблер NASM.

## ✨ Особенности

- 🌍 **Писать на Русском** (ru)
- 🤖 **Автоопределение:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Русский <-> ASM`

## 📖 Пример на Русском

### Source Code (`hello.masm`)
```asm
перенести rax, 1
перенести rdi, 1
перенести rsi, msg
перенести rdx, 13
системный_вызов

перенести rax, 60
перенести rdi, 0
системный_вызов
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

## 🛠️ Использование

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
