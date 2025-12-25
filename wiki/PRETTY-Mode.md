# PRETTY Mode - Reverse Translation

PRETTY mode allows you to view standard NASM assembly in any of the 10 supported languages.

---

## 🔄 What is PRETTY Mode?

**PRETTY** (Pretty Reverse Translation) converts standard ASM back to native language mnemonics.

### Use Cases

1. **Learning** - Study existing ASM code in your language
2. **Code Review** - Review code in your preferred language
3. **Collaboration** - International teams viewing same code differently
4. **Documentation** - Generate language-specific documentation

---

## 🚀 How to Use

### Basic Syntax

```bash
python mlasm.py <language> <input.asm> <output.masm> --reverse
```

### Example: View NASM in Spanish

**Input (standard.asm):**
```asm
mov rax, 1
add rbx, 10
jmp loop_start
call function
ret
```

**Command:**
```bash
python mlasm.py es standard.asm espanol.masm --reverse
```

**Output (espanol.masm):**
```asm
mover rax, 1
sumar rbx, 10
saltar loop_start
llamar function
retornar
```

---

## 🌍 Language Examples

### French
```bash
python mlasm.py fr program.asm program_fr.masm --reverse
```
Result: `mov` → `deplacer`, `add` → `ajouter`

### German
```bash
python mlasm.py de program.asm programm_de.masm --reverse
```
Result: `mov` → `bewegen`, `add` → `addieren`

### Japanese
```bash
python mlasm.py ja program.asm program_ja.masm --reverse
```
Result: `mov` → `移動`, `add` → `加算`

### Arabic
```bash
python mlasm.py ar program.asm program_ar.masm --reverse
```
Result: `mov` → `نقل`, `add` → `جمع`

---

## 📊 Coverage

### v0.3 - Full Coverage

All 10 languages now have complete PRETTY mapping:

| Language | Mappings | Status |
|----------|----------|--------|
| Spanish | 100+ | ✅ Complete |
| French | 60+ | ✅ Complete |
| German | 50+ | ✅ Complete |
| Italian | 60+ | ✅ Complete |
| Arabic | 50+ | ✅ Complete |
| Russian | 60+ | ✅ Complete |
| Korean | 50+ | ✅ Complete |
| Indonesian | 50+ | ✅ Complete |
| Chinese | 50+ | ✅ Complete |
| Japanese | 60+ | ✅ Complete |

---

## 🔍 How It Works

### Reverse Mapping Table

MultiLang-ASM maintains a `PRETTY` dictionary that maps standard mnemonics to native equivalents:

```python
PRETTY = {
    "es": {
        "mov": "mover",
        "add": "sumar",
        "jmp": "saltar",
        # ... 100+ more
    },
    "fr": {
        "mov": "deplacer",
        "add": "ajouter",
        "jmp": "sauter",
        # ... 60+ more
    },
    # ... all 10 languages
}
```

### Translation Process

1. Parse input ASM line by line
2. Identify mnemonics
3. Look up in PRETTY table for target language
4. Replace with native equivalent
5. Preserve comments and formatting

---

## ⚙️ Advanced Usage

### Batch Conversion

Convert multiple files:

```bash
for file in *.asm; do
    python mlasm.py es "$file" "${file%.asm}_es.masm" --reverse
done
```

### Round-Trip Verification

Verify translation accuracy:

```bash
# Original Spanish
python mlasm.py es original.masm temp.asm

# Round-trip to Spanish
python mlasm.py es temp.asm roundtrip.masm --reverse

# Compare
diff original.masm roundtrip.masm
```

---

## ⚠️ Limitations

### What PRETTY Does

- ✅ Translates instruction mnemonics
- ✅ Preserves comments
- ✅ Maintains formatting
- ✅ Keeps labels unchanged

### What PRETTY Doesn't Do

- ❌ Doesn't translate directives (`.text`, `.data`)
- ❌ Doesn't translate register names
- ❌ Doesn't translate section names
- ❌ Doesn't handle complex macros

### Example

**Input:**
```asm
section .text
global _start
_start:
    mov rax, 1
```

**Spanish Reverse:**
```asm
section .text
global _start
_start:
    mover rax, 1
```

Notice: `section`, `global`, `_start`, `rax` remain unchanged.

---

## 🎯 Best Practices

### 1. Use for Learning

```bash
# Download NASM tutorial code
wget https://example.com/tutorial.asm

# View in your language
python mlasm.py es tutorial.asm tutorial_es.masm --reverse

# Study in native language!
```

### 2. Code Review Workflow

```bash
# Developer writes in Spanish
python mlasm.py es feature.masm feature.asm

# Reviewer views in French
python mlasm.py fr feature.asm feature_fr.masm --reverse
```

### 3. Documentation Generation

Generate docs in multiple languages:

```bash
python mlasm.py es kernel.asm kernel_docs_es.masm --reverse
python mlasm.py fr kernel.asm kernel_docs_fr.masm --reverse
python mlasm.py de kernel.asm kernel_docs_de.masm --reverse
```

---

## 🔮 Future Enhancements

Planned for future versions:

- 🔄 More comprehensive mappings (currently 60-100 per language)
- 🔄 Directive translation (`.text` → `.texto`)
- 🔄 Comment translation (experimental)
- 🔄 Variable name suggestions

---

## 📚 Related Pages

- [How to Use](How-to-Use) - Basic usage guide
- [Examples](Examples) - Code examples
- [Supported Languages](Supported-Languages) - Language list
- [Roadmap](Roadmap) - Future plans
