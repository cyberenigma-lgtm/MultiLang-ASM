# 🛡️ MultiLang-ASM v0.4

> *"Il primo assemblatore x86_64 multilingue."*

**Scrivi assembler nella tua lingua madre.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Italiano** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Che cos'è?

MultiLang-ASM ti permette di scrivere assembly x86_64 usando parole chiave in **Italiano**.
Traduce automaticamente il tuo codice in assembly NASM standard.

## ✨ Caratteristiche

- 🌍 **Scrivi in Italiano** (it)
- 🤖 **Rilevamento Auto:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Italiano <-> ASM`

## 📖 Esempio in Italiano

### Source Code (`hello.masm`)
```asm
spostare rax, 1
spostare rdi, 1
spostare rsi, msg
spostare rdx, 13
chiamata_sistema

spostare rax, 60
spostare rdi, 0
chiamata_sistema
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

## 🛠️ Utilizzo

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
