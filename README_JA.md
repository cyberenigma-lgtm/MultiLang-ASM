# 🛡️ MultiLang-ASM v0.4

> *"世界初の多言語 x86_64 アセンブラ。"*

**母国語でアセンブリを書きましょう。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **日本語** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 これは何ですか？

MultiLang-ASM は、**日本語**のキーワードを使用して x86_64 アセンブリを書くことを可能にします。
コードは自動的に標準的な NASM アセンブリに翻訳されます。

## ✨ 特徴

- 🌍 **日本語で書く** (ja)
- 🤖 **自動検出:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `日本語 <-> ASM`

## 📖 日本語の例

### Source Code (`hello.masm`)
```asm
移動 rax, 1
移動 rdi, 1
移動 rsi, msg
移動 rdx, 13
システムコール

移動 rax, 60
移動 rdi, 0
システムコール
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

## 🛠️ 使い方

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
