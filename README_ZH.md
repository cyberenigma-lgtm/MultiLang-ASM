# 🛡️ MultiLang-ASM v0.4

> *"第一个多语言 x86_64 汇编器。"*

**用您的母语编写汇编代码。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **中文** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 这是什么？

MultiLang-ASM 允许您使用**中文**关键字编写 x86_64 汇编。
它会自动将您的代码翻译成标准的 NASM 汇编。

## ✨ 特性

- 🌍 **用中文编写** (zh)
- 🤖 **自动检测:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `中文 <-> ASM`

## 📖 中文示例

### Source Code (`hello.masm`)
```asm
移動 rax, 1
移動 rdi, 1
移動 rsi, msg
移動 rdx, 13
系統呼叫

移動 rax, 60
移動 rdi, 0
系統呼叫
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

## 🛠️ 用法

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
