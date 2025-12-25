# Contributing to MultiLang-ASM

Thank you for your interest in contributing! This page guides you through the process.

---

## 🌟 Ways to Contribute

1. 🌍 **Add a new language**
2. 📝 **Improve existing translations**
3. 📚 **Enhance documentation**
4. 🐛 **Report bugs**
5. ✨ **Propose features**
6. 🧪 **Write tests**
7. ⭐ **Give us a star**

---

## 🌍 Adding a New Language

### Prerequisites
- Native speaker proficiency
- Basic Python knowledge
- 30-60 minutes

### Steps

#### 1. Fork & Clone
```bash
git fork https://github.com/cyberenigma-lgtm/MultiLang-ASM.git
git clone https://github.com/YOUR_USERNAME/MultiLang-ASM.git
cd MultiLang-ASM
```

#### 2. Edit `mlasm.py`

Add your language to the `TABLE` dictionary:

```python
TABLE["pt"] = {  # Portuguese example
    # Movement
    "mover": "mov",
    "mov": "mov",
    "trocar": "xchg",
    
    # Arithmetic
    "somar": "add",
    "subtrair": "sub",
    "multiplicar": "mul",
    
    # ... continue with 80+ instructions
}
```

#### 3. Add PRETTY Mapping

Add reverse translation to `PRETTY`:

```python
PRETTY["pt"] = {
    "mov": "mover",
    "add": "somar",
    "sub": "subtrair",
    # ... 60+ mappings
}
```

#### 4. Create Documentation

Create `docs/INSTRUCCIONES_PT.md` following the format of [existing references](https://github.com/cyberenigma-lgtm/MultiLang-ASM/tree/main/docs).

#### 5. Update Index

Add your language to `docs/README.md`:
```markdown
- 🇵🇹 [Português](INSTRUCCIONES_PT.md)
```

#### 6. Create Example

Create `demo_pt.masm` with basic example code.

#### 7. Test

```bash
python mlasm.py pt demo_pt.masm test.asm
python mlasm.py pt test.asm test_reverse.masm --reverse
```

#### 8. Submit Pull Request

```bash
git checkout -b add-portuguese
git add .
git commit -m "feat: add Portuguese language support"
git push origin add-portuguese
```

Open PR on GitHub with description of changes.

---

## 📝 Improving Translations

Found a better term? Great!

### Process

1. Open an [issue](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues/new) explaining why the new term is better
2. Get community feedback
3. Update `TABLE` in `mlasm.py`
4. Update documentation
5. Submit PR

### Principles

- **Naturalness > Literality** - Use terms that sound natural
- **Consistency** - Keep similar patterns across instructions
- **Clarity** - Avoid ambiguous terms

---

## 📚 Documentation Contributions

### What We Need

- Tutorials in different languages
- Real-world examples
- Integration guides
- Video tutorials
- Translation of existing docs

### Where to Add

- `docs/` - Language-specific docs
- Wiki pages - General guides
- `README.md` - Project overview
- `QUICKSTART.md` - Getting started

---

## 🐛 Reporting Bugs

### Before Reporting

1. Check [existing issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)
2. Verify you're using the latest version
3. Test with minimal example

### Bug Report Template

Use the [bug report template](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues/new?template=bug_report.md):

- Describe the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Error messages

---

## ✨ Proposing Features

### Feature Requests

Open an [issue](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues/new?template=feature_request.md) with:

- **Use case** - Why is this needed?
- **Proposed solution** - How should it work?
- **Examples** - Show expected usage
- **Alternatives** - Other approaches considered?

---

## 🧪 Writing Tests

### Test Structure

```
tests/
├── test_translation.py    # Forward translation tests
├── test_reverse.py        # Reverse mode tests
└── fixtures/
    └── es/
        ├── simple.masm
        └── expected.asm
```

### Writing a Test

```python
def test_spanish_basic():
    """Test basic Spanish translation"""
    input_code = "mover rax, 1\nsumar rbx, 10"
    expected = "mov rax, 1\nadd rbx, 10"
    
    result = translate(input_code, "es", to_standard=True)
    assert result == expected
```

### Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No unrelated changes

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] New language

## Testing
How was this tested?

## Checklist
- [ ] Tests pass
- [ ] Docs updated
- [ ] Self-reviewed
```

---

## 🎨 Code Style

### Python Style

- Follow PEP 8 (mostly)
- Descriptive variable names
- Comment complex logic
- Keep functions focused

### Documentation Style

- Clear, concise language
- Code examples for features
- Emoji for visual hierarchy
- Link to related pages

---

## 🏆 Recognition

Contributors are recognized in:

- `README.md` Contributors section
- Release notes
- Documentation of features they added

---

## 📞 Getting Help

Stuck? Need guidance?

- **Discussions:** [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions)
- **Email:** neuro.so.ia.sim@gmail.com
- **Issues:** Tag with `question`

---

## 🤝 Code of Conduct

**Golden Rule:** Treat others as you want to be treated.

- ✅ Be respectful
- ✅ Accept feedback gracefully
- ✅ Focus on what's best for the project
- ❌ No discrimination
- ❌ No harassment

---

## 🚀 Your First Contribution

Not sure where to start?

1. Browse [good first issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
2. Fix a typo in documentation
3. Add a code example
4. Improve error messages
5. Translate a tutorial

Every contribution matters! 🙏

---

**See Also:**
- [How to Use](How-to-Use) - Usage guide
- [Roadmap](Roadmap) - Future plans
- [FAQ](FAQ) - Common questions
