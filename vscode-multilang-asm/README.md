# MultiLang-ASM VSCode Extension

**The first multilingual assembly extension for VSCode**

## Features

- ✅ **Syntax highlighting** for 16 languages
- ✅ **Autocomplete** with language-specific suggestions
- ✅ **Snippets** for common patterns
- ✅ **Kids Mode** with simplified syntax
- ✅ **Hover help** for instructions and registers
- ✅ **Auto-detection** of language from code

## Supported Languages

- 🇪🇸 Español
- 🇫🇷 Français
- 🇩🇪 Deutsch
- 🇮🇹 Italiano
- 🇸🇦 العربية
- 🇷🇺 Русский
- 🇰🇷 한국어
- 🇮🇩 Bahasa
- 🇨🇳 中文
- 🇯🇵 日本語
- 🇧🇷 Português
- 🇮🇳 Hindi
- 🇹🇷 Turkish
- 🇵🇱 Polish
- 🇸🇪 Swedish
- 🇳🇱 Dutch
- 🇬🇷 Greek (New!)
- 🇮🇱 Hebrew (New!)
- 🇹🇭 Thai (New!)
- 🇻🇳 Vietnamese (New!)
- 🇰🇪 Swahili (New!)
- 🇵🇭 Tagalog (New!)
- 🇲🇾 Malay (New!)
- 🇮🇷 Persian (New!)
- 🇺🇦 Ukrainian (New!)
- 🇷🇴 Romanian (New!)

### 🎭 Global Dialects (New in v0.5)
- **English:** Cockney, Aussie, Texan, Scots, Irish.
- **Spanish:** Andalusian (Standard), Madrileño.
- **German:** Bavarian, Swiss, Austrian.
- **Italian:** Sicilian, Roman.
- **French:** Quebecois.
- **Chinese:** Cantonese.
- **Portuguese:** Brazilian.

## 🚀 New Features in v0.5

### 🛡️ Professional Mode
Full x86-64 instruction set support mapped to native languages. Now supports:
- **Stack:** `push`, `pop` (e.g., `empujar`, `sacar`)
- **Logic:** `and`, `or`, `xor`, `not` (e.g., `y`, `o`, `xor`, `no`)
- **Control Flow:** `je`, `jne`, `loop` (e.g., `si_igual`, `bucle`)
- **Arithmetics:** `inc`, `dec`, `mul`, `div`

### 🎓 Educational Hub
Interactive Walkthroughs included directly in VSCode:
1.  **Get Started**: Interactive intro.
2.  **Kids Zone**: Learn to code with simplified syntax.
3.  **Teacher's Guide**: Methodology for educators.

## Installation

1. Open VSCode
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "MultiLang-ASM"
4. Click Install

## Usage

1. Create a file with `.masm` extension
2. Start writing assembly in your language
3. Enjoy syntax highlighting and autocomplete!

### Example (Spanish):
```asm
mover rax, 5
sumar rax, 3
enseñar rax
```

### Example (Kids Mode - Spanish):
```asm
pon rax a 5
suma rax con 3
enseña rax
```

## Configuration

Open VSCode settings and search for "MultiLang-ASM":

- `multilangasm.defaultLanguage`: Set your preferred language (default: "es")
- `multilangasm.autoDetect`: Auto-detect language from code (default: true)
- `multilangasm.enableKidsMode`: Enable simplified syntax for children (default: false)

## Snippets

Type the instruction name and press Tab:

- `mover` → Move instruction (Spanish)
- `pon` → Put instruction (Kids mode)
- `funcion` → Function template
- `repite` → Loop template
- `si` → If conditional template

## Development

### Building

```bash
npm install
npm run compile
```

### Testing

```bash
npm test
```

### Publishing

```bash
vsce package
vsce publish
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](https://github.com/cyberenigma-lgtm/MultiLang-ASM/blob/main/CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE)

## Author

José Manuel  
Email: neuro.so.ia.sim@gmail.com  
GitHub: https://github.com/cyberenigma-lgtm/MultiLang-ASM

## Part of Neuro-OS Ecosystem

🛡️ [Neuro-OS](https://neuro-os.es)
