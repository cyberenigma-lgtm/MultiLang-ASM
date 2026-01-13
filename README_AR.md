# 🛡️ MultiLang-ASM v0.4

> *"أول مجمع x86_64 متعدد اللغات."*

**اكتب لغة التجميع بلغتك الأم.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **العربية** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 ما هذا؟

يسمح لك MultiLang-ASM بكتابة تجميع x86_64 باستخدام كلمات رئيسية باللغة **العربية**.
يترجم الكود الخاص بك تلقائيًا إلى تجميع NASM القياسي.

## ✨ الميزات

- 🌍 **اكتب باللغة العربية** (ar)
- 🤖 **الكشف التلقائي:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `العربية <-> ASM`

## 📖 مثال بالعربية

### Source Code (`hello.masm`)
```asm
نقل rax, 1
نقل rdi, 1
نقل rsi, msg
نقل rdx, 13
استدعاء_النظام

نقل rax, 60
نقل rdi, 0
استدعاء_النظام
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

## 🛠️ الاستخدام

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
