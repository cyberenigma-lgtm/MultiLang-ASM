# Frequently Asked Questions (FAQ)

Common questions about MultiLang-ASM answered.

---

## 🤔 General Questions

### Q: What is MultiLang-ASM?

**A:** MultiLang-ASM is a translation layer for x86_64 assembly that allows you to write code using mnemonics in your native language instead of English. It translates to standard NASM-compatible assembly.

### Q: Is this a new assembler?

**A:** No. MultiLang-ASM is a **translator**, not an assembler. It converts native language mnemonics to standard ASM, which is then assembled by NASM/FASM/GAS.

### Q: Does the CPU understand my language?

**A:** No. The CPU still executes standard opcodes. MultiLang-ASM is a human-facing tool that removes the English language barrier.

---

## 🌍 Language Questions

### Q: How many languages are supported?

**A:** Currently **10 languages**: Spanish, French, German, Italian, Arabic, Russian, Korean, Indonesian, Chinese, and Japanese.

### Q: Can I add my language?

**A:** Yes! See [Contributing](Contributing) for instructions. We welcome contributions from native speakers.

### Q: Why isn't Portuguese/Hindi/Turkish supported?

**A:** We started with 10 languages and are actively accepting contributions for more. Open an [issue](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues) to propose your language.

### Q: Can I mix languages in the same file?

**A:** No. Each file is processed in a single language. However, you can use standard English mnemonics alongside native ones.

---

## ⚙️ Technical Questions

### Q: Is the generated ASM the same as if I wrote in English?

**A:** Yes. The output is identical to handwritten NASM code. There's zero performance difference.

### Q: Does it support all x86_64 instructions?

**A:** Currently 80+ most common instructions. Advanced/rare instructions fallback to English for now.

### Q: Can it handle macros?

**A:** Basic macros work. Advanced macro systems (NASM %macro with parameters) are planned for v0.4.

### Q: What about directives like `.text`, `.data`?

**A:** Directives currently remain in English. Translating them is on the roadmap.

---

## 🔧 Usage Questions

### Q: How do I install it?

**A:** Just `git clone` the repository. No dependencies required (only Python 3.6+).

### Q: Can I use it in production?

**A:** Yes! v0.3 is production-ready. The output is standard NASM-compatible ASM.

### Q: Does it work on Windows/Mac/Linux?

**A:** Yes, all platforms with Python 3.6+ are supported.

### Q: Can I integrate it with my build system?

**A:** Yes. See examples for [Make](How-to-Use#-integration-with-build-systems) and CMake integration.

---

## 🔄 PRETTY Mode Questions

### Q: What is PRETTY mode?

**A:** PRETTY mode converts standard ASM back to native language mnemonics. It's for viewing existing code in your language.

### Q: Does reverse translation always work?

**A:** It works for mapped instructions (80+ per language). Unmapped instructions remain in English.

### Q: Is round-trip translation lossless?

**A:** For supported instructions, yes. Comments and formatting are preserved.

---

## 🐛 Troubleshooting

### Q: My Unicode characters don't display correctly

**A:** On Windows, run `chcp 65001` before using MultiLang-ASM to enable UTF-8.

### Q: The tool says "Language not supported"

**A:** Verify you're using a valid language code: `es`, `fr`, `de`, `it`, `ar`, `ru`, `ko`, `id`, `zh`, `ja`.

### Q: Comments are being lost

**A:** This shouldn't happen. If it does, please [report a bug](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues/new?template=bug_report.md).

### Q: The generated ASM doesn't assemble

**A:** MultiLang-ASM only translates mnemonics. Syntax errors in your source will appear in the output. Check your source code.

---

## 📊 Project Questions

### Q: Who created this?

**A:** J / Neuro-OS Project. See [GitHub profile](https://github.com/cyberenigma-lgtm).

### Q: What's the license?

**A:** MIT License - completely free to use, modify, and distribute.

### Q: Can I use this for my company/school?

**A:** Absolutely! The MIT license allows commercial and educational use.

### Q: How can I contribute?

**A:** See [Contributing](Contributing) for details. We welcome code, translations, docs, and feedback.

---

## 🔮 Future Features

### Q: Will you add a VSCode plugin?

**A:** Yes, it's planned for v0.5.

### Q: Will you support ARM assembly?

**A:** It's on the long-term roadmap (v0.5+).

### Q: Will there be automatic language detection?

**A:** Yes! Planned for v0.4.

### Q: Can you add syntax validation?

**A:** Considered for v0.4 or v0.5.

---

## 🤝 Community

### Q: Is there a Discord/Slack?

**A:** Not yet, but we have [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions) for community interaction.

### Q: How do I report a bug?

**A:** Use the [bug report template](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues/new?template=bug_report.md).

### Q: Where can I see the roadmap?

**A:** See [Roadmap](Roadmap) wiki page or [README](https://github.com/cyberenigma-lgtm/MultiLang-ASM#roadmap).

---

## 📧 Still Have Questions?

- **Email:** neuro.so.ia.sim@gmail.com
- **Discussions:** [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions)
- **Issues:** [GitHub Issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)

---

**See Also:**
- [How to Use](How-to-Use) - Usage guide
- [Examples](Examples) - Code examples
- [Contributing](Contributing) - How to help
