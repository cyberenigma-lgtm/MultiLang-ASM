# 🛡️ MultiLang-ASM v0.4

> *"İlk çok dilli x86_64 çevirici (assembler)."*

**Kendi ana dilinizde assembly yazın.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Türkçe** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Bu nedir?

MultiLang-ASM, **Türkçe** anahtar kelimeler kullanarak x86_64 assembly yazmanıza olanak tanır.
Kodunuzu otomatik olarak standart NASM assembly diline çevirir.

## ✨ Özellikler

- 🌍 **Türkçe yazın** (tr)
- 🤖 **Otomatik Algılama:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Türkçe <-> ASM`

## 📖 Türkçe Örnek

### Source Code (`hello.masm`)
```asm
taşı rax, 1
taşı rdi, 1
taşı rsi, msg
taşı rdx, 13
syscall

taşı rax, 60
taşı rdi, 0
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

## 🛠️ Kullanım

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
