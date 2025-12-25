# GitHub Wiki Setup Instructions

This folder contains all the wiki pages for MultiLang-ASM.

---

## 📋 Wiki Pages Created

1. **Home.md** - Main landing page
2. **Supported-Languages.md** - Complete language list and comparison
3. **How-to-Use.md** - Installation and usage guide
4. **PRETTY-Mode.md** - Reverse translation documentation
5. **Contributing.md** - Contributing guidelines
6. **FAQ.md** - Frequently asked questions
7. **Roadmap.md** - Version timeline and future plans

---

## 🚀 How to Upload to GitHub Wiki

### Method 1: Via GitHub Web Interface (Recommended)

1. Go to your repository's Wiki tab: https://github.com/cyberenigma-lgtm/MultiLang-ASM/wiki

2. Click "New Page" for each file

3. Copy the content from each `.md` file and paste it

4. **Important:** Use the exact filenames (without .md extension):
   - `Home`
   - `Supported-Languages`
   - `How-to-Use`
   - `PRETTY-Mode`
   - `Contributing`
   - `FAQ`
   - `Roadmap`

5. Click "Save Page"

### Method 2: Clone Wiki Repository

GitHub wikis are Git repositories. You can clone and push:

```bash
# Clone the wiki
git clone https://github.com/cyberenigma-lgtm/MultiLang-ASM.wiki.git
cd MultiLang-ASM.wiki

# Copy all wiki pages
cp ../wiki/*.md .

# Commit and push
git add .
git commit -m "docs: add complete wiki documentation"
git push origin master
```

---

## 🔗 Wiki Navigation

The wiki is already cross-linked. Internal links use this format:
```markdown
[Link Text](Page-Name)
```

For example:
- `[How to Use](How-to-Use)` links to the How-to-Use page
- `[FAQ](FAQ)` links to the FAQ page

---

## ✅ Checklist

After uploading, verify:

- [ ] Home page displays correctly
- [ ] All internal links work
- [ ] Code blocks are formatted
- [ ] Tables render properly
- [ ] Emojis display correctly

---

## 🎨 Customization

Feel free to customize:
- Add more examples
- Update version numbers
- Add screenshots
- Expand FAQ
- Update roadmap dates

---

## 📧 Questions?

Email: neuro.so.ia.sim@gmail.com

---

**Created:** 2025-12-25  
**Version:** v0.3  
**Status:** Ready to deploy
