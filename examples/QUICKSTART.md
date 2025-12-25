# Quick Start - Build a Kernel in 5 Minutes

**100% reproducible kernel example in your native language.**

---

## ⚡ Fastest Way (Automated)

```bash
cd examples
make run
```

**Done!** QEMU will open with your kernel running.

---

## 📋 Step by Step (Manual - Learn How It Works)

### Step 1: Translate Spanish → NASM

```bash
cd examples

# Translate bootloader
python ../mlasm.py es boot.masm boot.asm

# Translate kernel
python ../mlasm.py es kernel.masm kernel.asm
```

**What happened?**
- `boot.masm` (Spanish) → `boot.asm` (NASM)
- `kernel.masm` (Spanish) → `kernel.asm` (NASM)

### Step 2: Compile to Binary

```bash
# Compile bootloader
nasm -f bin boot.asm -o boot.bin

# Compile kernel
nasm -f bin kernel.asm -o kernel.bin
```

**What happened?**
- `boot.asm` → `boot.bin` (512 bytes, raw binary)
- `kernel.asm` → `kernel.bin` (5120 bytes, raw binary)

### Step 3: Create Disk Image

```bash
# Create empty disk image (1.44 MB floppy)
dd if=/dev/zero of=kernel.img bs=512 count=2880

# Write bootloader to sector 1
dd if=boot.bin of=kernel.img conv=notrunc

# Write kernel starting at sector 2
dd if=kernel.bin of=kernel.img seek=1 conv=notrunc
```

**What happened?**
- Created 1.44 MB disk image
- Bootloader at sector 1 (bytes 0-511)
- Kernel at sectors 2-11 (bytes 512-5631)

### Step 4: Run in QEMU

```bash
qemu-system-x86_64 -drive file=kernel.img,format=raw
```

**What you'll see:**

```
========================================
   MULTILINGUAL KERNEL v0.1
   Created with MultiLang-ASM
========================================

Kernel in Spanish running!
Press keys to see echo...
ESC to halt.

> █
```

---

## 🇨🇳 Try the Chinese Version

Want to prove it works with non-Latin scripts?

```bash
cd examples

# Build Chinese kernel
make -f Makefile.zh

# Run
make -f Makefile.zh run
```

**Output:**
```
========================================
   多語言核心 v0.1
   使用 MultiLang-ASM 建立
========================================

中文核心正在運作！
按鍵可見回顯...
ESC 停止系統。

> █
```

**Same functionality. Different language. Same binary code.**

---

## 🔍 Compare Generated Code

Want to see what MultiLang-ASM generated?

```bash
# View generated NASM from Spanish
head -20 boot.asm

# View generated NASM from Chinese
head -20 boot_zh.asm
```

Both compile to **identical** machine code.

---

## 🧪 Files Generated

After running, you'll have:

```
examples/
├── boot.masm          # Source (Spanish)
├── boot.asm           # Generated NASM
├── boot.bin           # Compiled binary
├── kernel.masm        # Source (Spanish)
├── kernel.asm         # Generated NASM
├── kernel.bin         # Compiled binary
└── kernel.img         # Bootable disk image
```

---

## 🐛 Troubleshooting

### "Python not found"
```bash
# Windows
py mlasm.py es boot.masm boot.asm

# Linux/Mac with python3
python3 mlasm.py es boot.masm boot.asm
```

### "NASM not found"
Install NASM:
- **Windows:** `choco install nasm` or download from nasm.us
- **Ubuntu:** `sudo apt install nasm`
- **macOS:** `brew install nasm`

### "QEMU not found"
Install QEMU:
- **Windows:** Download from qemu.org
- **Ubuntu:** `sudo apt install qemu-system-x86`
- **macOS:** `brew install qemu`

### "dd not found" (Windows)
Use Git Bash or WSL, or use the Makefile which handles this.

---

## 📊 What Each Command Does

| Command | Input | Output | Purpose |
|---------|-------|--------|---------|
| `mlasm.py` | `.masm` | `.asm` | Translate native → NASM |
| `nasm -f bin` | `.asm` | `.bin` | Compile ASM → binary |
| `dd` | `.bin` | `.img` | Create bootable image |
| `qemu` | `.img` | Running VM | Test kernel |

---

## 🎓 Next Steps

1. **Modify the message** - Edit `mensaje` in `kernel.masm`
2. **Change colors** - Modify `mover bx, 0x07` to other values
3. **Add functionality** - Implement command parsing
4. **Learn more** - Read `KERNEL-EXAMPLE.md` for detailed tutorial

---

## 📧 Need Help?

- **Issues:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues
- **Email:** neuro.so.ia.sim@gmail.com
- **Wiki:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/wiki

---

**Congratulations! You just built an OS kernel in your language!** 🛡️✨
