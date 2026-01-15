# 🛡️ MultiLang-ASM v0.4

> *"पहला बहुभाषी x86_64 असेंबलर।"*

**अपनी मातृभाषा में असेंबली लिखें।**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Hindi** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 यह क्या है?

MultiLang-ASM आपको **हिंदी** कीवर्ड का उपयोग करके x86_64 असेंबली लिखने की अनुमति देता है।
यह स्वचालित रूप से आपके कोड को मानक NASM असेंबली में अनुवादित करता है।

## ✨ विशेषताएं

- 🌍 **हिंदी में लिखें** (hi)
- 🤖 **स्वतः पहचान:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Hindi <-> ASM`

## 📖 हिंदी उदाहरण

### Source Code (`hello.masm`)
```asm
bhejo rax, 1
bhejo rdi, 1
bhejo rsi, msg
bhejo rdx, 13
syscall

bhejo rax, 60
bhejo rdi, 0
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

## 🛠️ उपयोग

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
