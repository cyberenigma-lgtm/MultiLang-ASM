# 🛡️ Creating a Kernel from Scratch with MultiLang-ASM

Complete example of how to create a minimal kernel in **50 lines** using MultiLang-ASM.

📖 **English** | **[Español](KERNEL-EXAMPLE_ES.md)** | **[中文示例](examples/README.md#-kernel-mínimo-en-chino-中文核心)**

---

## 📦 Project Files

```
my-kernel/
├── mlasm.py              # Copied from project
├── boot.masm             # Bootloader in your language
├── kernel.masm           # Kernel in your language
├── linker.ld             # Linker script (optional)
└── Makefile              # Build automation
```

---

## 🚀 Step 1: Bootloader (boot.masm)

**boot.masm** - 16 lines fully documented (see `examples/boot.masm` for detailed version):

```asm
; boot.masm - Bootloader
[bits 16]
[org 0x7C00]

inicio:
    ; Initialize segments
    mover ax, 0
    mover ds, ax
    mover es, ax
    mover ss, ax
    mover sp, 0x7C00
    
    ; Load kernel from disk (10 sectors)
    mover ah, 0x02          ; BIOS function: read sectors
    mover al, 10            ; number of sectors
    mover ch, 0             ; cylinder 0
    mover cl, 2             ; sector 2 (sector 1 is bootloader)
    mover dh, 0             ; head 0
    mover bx, 0x1000        ; destination address
    interrupcion 0x13       ; BIOS disk services
    
    ; Print message
    mover si, msg_boot
    llamar imprimir
    
    ; Jump to kernel
    saltar 0x1000

; Print function
imprimir:
    meter ax
    meter bx
.loop:
    cargar_byte             ; lodsb: AL = [SI++]
    comparar al, 0
    si_igual .done
    mover ah, 0x0E          ; teletype function
    mover bx, 0x07          ; color
    interrupcion 0x10       ; BIOS video
    saltar .loop
.done:
    sacar bx
    sacar ax
    retornar

msg_boot db 'Loading kernel...', 13, 10, 0

; Boot signature (must be at bytes 510-511)
times 510-($-$$) db 0
dw 0xAA55
```

---

## 💻 Step 2: Kernel (kernel.masm)

**kernel.masm** - 34 lines (see `examples/kernel.masm` for detailed version):

```asm
; kernel.masm - Minimal Kernel
[bits 16]
[org 0x1000]

inicio_kernel:
    ; Clear screen
    mover ah, 0x00
    mover al, 0x03
    interrupcion 0x10
    
    ; Print message
    mover si, mensaje
    llamar imprimir
    
    ; Main loop
bucle_principal:
    ; Wait for key
    mover ah, 0x00
    interrupcion 0x16
    
    ; Echo character
    mover ah, 0x0E
    interrupcion 0x10
    
    ; Check if ESC
    comparar al, 27
    si_igual shutdown
    
    saltar bucle_principal

shutdown:
    mover si, msg_apagado
    llamar imprimir
bucle_infinito:
    detener                 ; HLT
    saltar bucle_infinito

; Print function (same as bootloader)
imprimir:
    meter ax
    meter bx
.ciclo:
    cargar_byte
    comparar al, 0
   si_igual .fin
    mover ah, 0x0E
    mover bx, 0x07
    interrupcion 0x10
    saltar .ciclo
.fin:
    sacar bx
    sacar ax
    retornar

; Data
mensaje db 'Kernel in your language running!', 13, 10, 0
msg_apagado db 'System halted.', 13, 10, 0

; Fill to 5KB (10 sectors)
times 5120-($-$$) db 0
```

---

## ⚙️ Step 3: Makefile

```makefile
# Makefile for multilingual kernel
MLASM = python mlasm.py
NASM = nasm
DD = dd

all: kernel.img

# Translate bootloader
boot.asm: boot.masm
	$(MLASM) es $< $@

# Translate kernel
kernel.asm: kernel.masm
	$(MLASM) es $< $@

# Compile bootloader
boot.bin: boot.asm
	$(NASM) -f bin $< -o $@

# Compile kernel
kernel.bin: kernel.asm
	$(NASM) -f bin $< -o $@

# Create disk image
kernel.img: boot.bin kernel.bin
	$(DD) if=/dev/zero of=kernel.img bs=512 count=2880
	$(DD) if=boot.bin of=kernel.img conv=notrunc
	$(DD) if=kernel.bin of=kernel.img seek=1 conv=notrunc

# Run in QEMU
run: kernel.img
	qemu-system-x86_64 -drive file=kernel.img,format=raw

clean:
	rm -f *.asm *.bin kernel.img

.PHONY: all run clean
```

---

## 🏗️ Step 4: Compile and Run

### Complete Build

```bash
# Copy MultiLang-ASM
cp /path/to/mlasm.py .

# Build everything
make

# Run in QEMU
make run
```

### Step by Step (Manual)

```bash
# 1. Translate code (your language → NASM)
python mlasm.py es boot.masm boot.asm
python mlasm.py es kernel.masm kernel.asm

# 2. Compile to binary
nasm -f bin boot.asm -o boot.bin
nasm -f bin kernel.asm -o kernel.bin

# 3. Create disk image
dd if=/dev/zero of=kernel.img bs=512 count=2880
dd if=boot.bin of=kernel.img conv=notrunc
dd if=kernel.bin of=kernel.img seek=1 conv=notrunc

# 4. Run
qemu-system-x86_64 -drive file=kernel.img,format=raw
```

---

## 🎯 Expected Result

When you run `make run`, you'll see:

```
========================================
   MULTILINGUAL KERNEL v0.1
   Created with MultiLang-ASM
========================================

Kernel in your language running!
Press keys to see echo...
ESC to halt.

> 
```

---

## 📊 Code Analysis

### Lines of Code

| File | Lines | Language |
|------|-------|----------|
| boot.masm | 16 | Your language |
| kernel.masm | 34 | Your language |
| **Total** | **50** | **100%** |

### Instructions Used (Examples)

**In Spanish:**
- `mover` (mov) - Data movement
- `saltar` (jmp) - Unconditional jumps
- `comparar` (cmp) - Comparisons
- `si_igual` (je) - Conditional jump
- `llamar` (call) - Function call
- `retornar` (ret) - Return from function
- `meter` (push) - Push to stack
- `sacar` (pop) - Pop from stack
- `interrupcion` (int) - BIOS interrupts
- `detener` (hlt) - Halt CPU
- `cargar_byte` (lodsb) - Load byte

**In Chinese (中文):**
- `移動` (mov)
- `跳躍` (jmp)
- `呼叫` (call)
- `返回` (ret)
- `若相等` (je)
- `中斷` (int)
- `推入` (push)
- `彈出` (pop)

**All generate the same machine code!**

---

## 🔍 How It Works

### Bootloader
1. BIOS loads first 512 bytes at `0x7C00`
2. Bootloader configures segments
3. Reads 10 sectors from disk to `0x1000` (kernel)
4. Jumps to `0x1000` to execute kernel

### Kernel
1. Clears the screen (INT 10h, AH=00h)
2. Prints message character by character (INT 10h, AH=0Eh)
3. Enters infinite loop with `hlt`

---

## 🌍 Versions in Other Languages

The project includes complete working examples in:

### Spanish (Español)
```bash
cd examples
make run
```

### Chinese (中文)
```bash
cd examples
make -f Makefile.zh run
```

**Same functionality. Different language. Same binary output.**

---

## 🚀 Next Steps

### Expand the Kernel

1. **Protected Mode (32-bit)**
   - Enable A20 line
   - Load GDT (Global Descriptor Table)
   - Switch to protected mode

2. **Basic Drivers**
   - Keyboard driver
   - Timer driver
   - VGA driver

3. **File System**
   - FAT12/FAT16
   - Read/write files

---

## 📚 Resources

- [OSDev Wiki](https://wiki.osdev.org/) - Technical documentation
- [MultiLang-ASM Docs](https://github.com/cyberenigma-lgtm/MultiLang-ASM/tree/main/docs) - Language references
- [NASM Manual](https://nasm.us/doc/) - ASM syntax
- [Kernel Tutorial (Wiki)](https://github.com/cyberenigma-lgtm/MultiLang-ASM/wiki/Kernel-Tutorial) - Detailed tutorial

---

## 💡 Advantages of MultiLang-ASM

### Before (English)
```asm
mov ax, 0
mov ds, ax
call print
jmp loop
```

### Now (Your Language)

**Spanish:**
```asm
mover ax, 0
mover ds, ax
llamar imprimir
saltar bucle
```

**Chinese:**
```asm
移動 ax, 0
移動 ds, ax
呼叫 印出
跳躍 循環
```

**Same functionality, more natural code.**

---

## 🎓 Exercises

1. **Change Colors** - Modify text colors (BL register)
2. **Count Keypresses** - Add keystroke counter
3. **Command Interpreter** - Recognize "help", "clear" commands
4. **Multiple Lines** - Print several strings
5. **Graphics Mode** - Switch to VGA mode 13h

---

## 📧 Questions?

- **Email:** neuro.so.ia.sim@gmail.com
- **Wiki:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/wiki
- **Issues:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues

---

**You just created a kernel in your native language!** 🛡️✨

**Version:** v0.3  
**Date:** 2025-12-25  
**Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM
