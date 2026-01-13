# 🛡️ MultiLang-ASM v0.4

> *"Assembler x86_64 multibahasa pertama."*

**Tulis assembly dalam bahasa ibu Anda.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Bahasa Indonesia** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Apa ini?

MultiLang-ASM memungkinkan Anda menulis assembly x86_64 menggunakan kata kunci dalam **Bahasa Indonesia**.
Ini secara otomatis menerjemahkan kode Anda ke assembly NASM standar.

## ✨ Fitur

- 🌍 **Tulis dalam Bahasa Indonesia** (id)
- 🤖 **Deteksi Otomatis:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Bahasa Indonesia <-> ASM`

## 📖 Contoh Bahasa Indonesia

### Source Code (`hello.masm`)
```asm
pindah rax, 1
pindah rdi, 1
pindah rsi, msg
pindah rdx, 13
panggilan_sistem

pindah rax, 60
pindah rdi, 0
panggilan_sistem
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

## 🛠️ Penggunaan

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
