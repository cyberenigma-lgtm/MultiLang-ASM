# 🛡️ MultiLang-ASM v0.4

> *"최초의 다국어 x86_64 어셈블러."*

**모국어로 어셈블리를 작성하세요.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **한국어** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 이것은 무엇입니까?

MultiLang-ASM을 사용하면 **한국어** 키워드를 사용하여 x86_64 어셈블리를 작성할 수 있습니다.
코드는 자동으로 표준 NASM 어셈블리로 번역됩니다.

## ✨ 특징

- 🌍 **한국어로 작성** (ko)
- 🤖 **자동 감지:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `한국어 <-> ASM`

## 📖 한국어 예제

### Source Code (`hello.masm`)
```asm
이동 rax, 1
이동 rdi, 1
이동 rsi, msg
이동 rdx, 13
시스템호출

이동 rax, 60
이동 rdi, 0
시스템호출
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

## 🛠️ 사용법

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
