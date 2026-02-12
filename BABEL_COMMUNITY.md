# 🌍 Babel Community: The Future of Assembly for Everyone

Welcome to the **Babel Community**, the official initiative to make low-level programming accessible in every human language. MultiLang-ASM v0.6 "Babel Community Edition" is designed to be powered by *you*.

## Why Babel?
Traditional assembly languages are locked behind an English-centric barrier. We believe the logic of the machine is universal, and the words we use to describe it should be too.

## How to Contribute a Language Pack

With the new modular system, adding a language is easier than ever:

1. **Initialize your pack**:
   Run `python mlasm.py --new-lang <your_iso_code>` (e.g., `pt` for Portuguese, `hi` for Hindi).
2. **Edit the file**:
   Found in `langs/<your_iso_code>.py`. Add the mappings for instructions.
3. **Add "Kids Mode"**: 
   Help the next generation by adding simple verbs like "put", "take", and "look".
4. **Submit a Pull Request**: 
   Share your work with the world!

## Community Guidelines
- **Respect Local Nuances**: Use terms that feel natural to native speakers (e.g., "apanca" in Madrid, "stash" in Cockney).
- **Technical Accuracy**: Ensure the mappings align correctly with NASM mnemonics.
- **Inclusivity**: Low-level coding is for everyone, regardless of their native tongue.

## Roadmap to v1.0
- [ ] Web Browser Translator (WASM)
- [ ] VS Code Extension Integration for all Community Packs
- [ ] Real-time Collaborative Translation Platform

Join us in rebuilding the Tower of Babel, but this time, where everyone understands each other. 🛡️
