# 🛡️ MultiLang-ASM v0.4

> *"O primeiro assembler x86_64 multilíngue."*

**Escreva assembly em sua língua nativa.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **Português** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 O que é isso?

MultiLang-ASM permite escrever assembly x86_64 usando palavras-chave em **Português**.
Ele traduz automaticamente seu código para assembly NASM padrão.

## ✨ Recursos

- 🌍 **Escrever em Português** (pt)
- 🤖 **Detecção Automática:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `Português <-> ASM`

## 📖 Exemplo em Português

### Source Code (`hello.masm`)
```asm
mover rax, 1
mover rdi, 1
mover rsi, msg
mover rdx, 13
chamada_sistema

mover rax, 60
mover rdi, 0
chamada_sistema
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

## 🛠️ Uso

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
