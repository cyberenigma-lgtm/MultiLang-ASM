# 🛡️ MultiLang-ASM v0.4

> *"Le premier assembleur x86_64 multilingue."*

**Écrivez de l'assembleur dans votre langue maternelle.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Français** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 Qu'est-ce que c'est ?

MultiLang-ASM vous permet d'écrire de l'assembleur x86_64 en utilisant des mots-clés en **Français**.
Il traduit automatiquement votre code en assembleur NASM standard.

## ✨ Fonctionnalités

- 🌍 **Écrire en Français** (fr)
- 🤖 **Détection Auto:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Français <-> ASM`

## 📖 Exemple en Français

### Source Code (`hello.masm`)
```asm
deplacer rax, 1
deplacer rdi, 1
deplacer rsi, msg
deplacer rdx, 13
appel_systeme

deplacer rax, 60
deplacer rdi, 0
appel_systeme
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

## 🛠️ Utilisation

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
