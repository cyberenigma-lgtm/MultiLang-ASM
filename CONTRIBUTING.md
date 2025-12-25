# 🤝 Contributing to MultiLang-ASM

📖 **English** | **[Español](CONTRIBUTING_ES.md)**

---

Thank you for your interest in contributing to MultiLang-ASM! This project seeks to democratize low-level programming by removing linguistic barriers.

## 🌍 Ways to Contribute

### 1. Add a New Language

**What you need:**
- Be a native speaker or have advanced proficiency in the language
- Know natural programming terms in that language
- 30-60 minutes of time

**Steps:**

1. Fork the repository
2. Edit `mlasm.py` and add your language to the `TABLE`:

```python
TABLE["your_code"] = {
    # Movement
    "native_word": "mov",
    "another_word": "add",
    # ... continue with 80+ instructions
}
```

3. Create documentation in `docs/INSTRUCTIONS_XX.md` following the format of existing ones
4. Update `docs/README.md` to include your language
5. Create a pull request

**Languages we need:**
- 🇵🇹 Português
- 🇹🇷 Türkçe
- 🇵🇱 Polski
- 🇻🇳 Tiếng Việt
- 🇹🇭 ไทย
- 🇬🇷 Ελληνικά
- And more...

---

### 2. Improve Existing Translations

If you're a native speaker of a supported language and find that some terms could be more natural:

1. Open an issue describing the improvement
2. Propose the alternative term and why it sounds more natural
3. Make a pull request with the change

**Principle:** Naturalness > Literality

---

### 3. Expand Documentation

- Tutorials in your language
- Real project examples
- Specific use cases
- Explanatory videos

---

### 4. Report Bugs

**Issue format:**
```markdown
## Description
[Describe the problem]

## Steps to Reproduce
1. ...
2. ...

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: [Windows/Linux/macOS]
- Python: [version]
- MultiLang-ASM: [version]
```

---

### 5. Request Features

Open an issue with the `enhancement` label describing:
- What functionality you want
- Why it's useful
- Usage examples

---

## 📋 Style Guidelines

### Python Code

```python
# Use descriptive names
def translate_token(token, lang):  # ✅
def tt(t, l):  # ❌

# Document complex functions
def foo():
    """Explain what the function does"""
    pass

# Follow PEP 8 (but don't obsess)
```

### Markdown Documentation

- Use emojis for sections (improves scannability)
- Include functional code examples
- Link to other documents when relevant
- Keep lines to 80 columns when possible

### Translations

**Principles:**
1. **Naturalness over Literality** - Use terms that sound natural, not word-for-word translations
2. **Clarity over Brevity** - `compare` is better than `cmp`
3. **Consistency** - If you use verb infinitives, maintain it throughout the language
4. **Compatibility** - English instructions must always continue to work

---

## 🔄 Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your contribution:
   ```bash
   git checkout -b lang-xx
   ```
3. **Make your changes** following style guidelines
4. **Test** that everything works:
   ```bash
   python mlasm.py your_lang demo.masm demo.asm
   ```
5. **Commit** with descriptive message:
   ```bash
   git commit -m "feat: add support for Portuguese"
   ```
6. **Push** to your fork:
   ```bash
   git push origin lang-xx
   ```
7. **Open a Pull Request** on GitHub

---

## ✅ Checklist for New Languages

- [ ] Added to `TABLE` in `mlasm.py`
- [ ] Created `docs/INSTRUCTIONS_XX.md`
- [ ] Updated `docs/README.md`
- [ ] Updated main `README.md`
- [ ] Tested with at least 3 different examples
- [ ] Verified existing functionality still works

---

## 🎯 Current Priorities

**High priority:**
- Expansion of `PRETTY` for all languages (reversible mode)
- More languages in `TABLE`
- Real project examples

**Medium priority:**
- Automated tests
- VSCode plugin
- Automatic language detection

**Low priority:**
- ARM architecture support
- Interactive mode

---

## 💬 Communication

- **Issues:** For bugs, features, questions
- **Discussions:** For ideas, long debates
- **Pull Requests:** For code contributions

---

## 📜 Code of Conduct

**Golden rule:** Treat others as you want to be treated.

Specifically:
- ✅ Be respectful to all contributors
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the project
- ❌ We don't tolerate discrimination of any kind
- ❌ We don't tolerate hostile behavior

---

## 🙏 Acknowledgments

All contributors will be listed in:
- `README.md` (Contributors section)
- Each version's release notes
- Documentation of the language they add

---

## 📞 Questions?

Open an issue with the `question` label or start a Discussion.

---

**Thanks for helping democratize low-level programming.** 🛡️✨

---

**MultiLang-ASM** - Part of the Neuro-OS ecosystem  
https://github.com/cyberenigma-lgtm/MultiLang-ASM
