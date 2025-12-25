# Kernel Tutorial - Step by Step

Complete tutorial for creating a kernel from scratch using MultiLang-ASM in Spanish.

---

## 🎯 What You'll Learn

By the end of this tutorial, you'll understand:
- How a computer boots (BIOS → Bootloader → Kernel)
- Memory segmentation in Real Mode
- BIOS interrupts (video, keyboard, disk)
- Stack operations and calling conventions
- String manipulation in assembly
- Event loops in operating systems

---

## 📚 Prerequisites

### Knowledge Needed
- Basic programming concepts (loops, functions)
- Understanding of hexadecimal numbers
- Patience and curiosity!

### Tools Required
- Python 3.6+
- NASM assembler
- QEMU (for testing)
- MultiLang-ASM

---

## 🧱 Part 1: Understanding the Boot Process

### What Happens When You Turn On a Computer?

1. **BIOS/UEFI Starts**
   - ROM chip has firmware (BIOS)
   - Checks hardware (POST - Power-On Self Test)
   - Looks for bootable devices

2. **BIOS Loads Bootloader**
   - Reads first 512 bytes from disk
   - Checks bytes 510-511 for signature `0xAA55`
   - If valid, loads to address `0x7C00`
   - Jumps to `0x7C00` (your code starts!)

3. **Bootloader Loads Kernel**
   - Your bootloader reads kernel from disk
   - Loads kernel to memory (e.g., `0x1000`)
   - Jumps to kernel entry point

4. **Kernel Takes Control**
   - Initializes hardware
   - Sets up interrupts
   - Starts main loop

---

## 🔢 Part 2: Memory in Real Mode

### Memory Addressing Formula

In 16-bit Real Mode:
```
Physical Address = (Segment × 16) + Offset
```

### Example

```
CS:IP = 0x7C0:0x0000
Real address = (0x7C0 × 16) + 0x0000 = 0x7C00
```

### Why Segments?

- 16-bit registers can only address 64 KB (2^16)
- Segments allow accessing up to 1 MB
- 1 MB = 2^20 = 1,048,576 bytes

### Memory Map (Rough)

```
0x00000 - 0x003FF: Interrupt Vector Table (IVT)
0x00400 - 0x004FF: BIOS Data Area (BDA)
0x00500 - 0x07BFF: Free for use
0x07C00 - 0x07DFF: Bootloader (512 bytes)
0x07E00 - 0x9FFFF: Free for use (638 KB)
0xA0000 - 0xFFFFF: Video memory, ROM, etc.
```

---

## 💾 Part 3: The Bootloader - Line by Line

### Full Annotated Code

```asm
[bits 16]                   ; Generate 16-bit code
[org 0x7C00]                ; Code starts at 0x7C00

inicio:
    ; Step 1: Initialize Segments
    mover ax, 0             ; AX = 0
    mover ds, ax            ; Data Segment = 0
    mover es, ax            ; Extra Segment = 0
    mover ss, ax            ; Stack Segment = 0
    mover sp, 0x7C00        ; Stack Pointer = 0x7C00
    
    ; Step 2: Load Kernel from Disk
    mover ah, 0x02          ; Function: Read Sectors
    mover al, 10            ; Read 10 sectors
    mover ch, 0             ; Cylinder 0
    mover cl, 2             ; Sector 2 (sector 1 is bootloader)
    mover dh, 0             ; Head 0
    mover bx, 0x1000        ; Destination: ES:BX = 0x0000:0x1000
    interrupcion 0x13       ; BIOS Disk Service
    
    ; Step 3: Print Message
    mover si, msg_boot
    llamar imprimir
    
    ; Step 4: Jump to Kernel
    saltar 0x1000           ; Transfer control
```

### Breaking Down Each Step

#### Why Initialize Segments to 0?

**Question:** Why `mover ds, ax` where `ax = 0`?

**Answer:** 
- Segments × 16 + Offset = Address
- If segment = 0, then offset = real address
- Simplifies addressing: `[0x1234]` really means address `0x1234`

#### Why Can't We Move 0 Directly to DS?

**Question:** Why not `mover ds, 0`?

**Answer:**
- x86 doesn't allow immediate values to segment registers
- Must go through a general-purpose register (AX, BX, etc.)
- It's a hardware limitation

#### Why Stack Pointer at 0x7C00?

**Question:** Doesn't the stack overwrite our code?

**Answer:**
- Stack grows **downward** (toward lower addresses)
- Code is at `0x7C00+` (grows upward)
- Stack is at `0x7C00-` (grows downward)
- They grow away from each other = safe!

```
Memory layout:
0x7B00 ← Stack grows this way
0x7C00 → Code is here
0x7E00 → Code grows this way
```

---

## 🖥️ Part 4: BIOS Interrupts

### What is an Interrupt?

An interrupt is like calling a predefined function in the BIOS.

**Syntax:**
```asm
mover ah, function_number
interrupcion interrupt_number
```

### INT 13h - Disk Services

```asm
mover ah, 0x02          ; Function 02h = Read Sectors
mover al, 10            ; Number of sectors
mover ch, 0             ; Cylinder number
mover cl, 2             ; Starting sector
mover dh, 0             ; Head number
mover dl, 0             ; Drive number (0 = floppy, 0x80 = HDD)
mover bx, 0x1000        ; Buffer address (ES:BX)
interrupcion 0x13       ; Call BIOS
```

**After INT 13h:**
- CF (Carry Flag) = 0 if success, 1 if error
- AH = Status code
- AL = Number of sectors actually read

### INT 10h - Video Services

#### Function 0x00 - Set Video Mode

```asm
mover ah, 0x00
mover al, 0x03          ; 80x25 text mode
interrupcion 0x10
```

**Video modes:**
- `0x03` = 80x25 text, 16 colors
- `0x12` = 640x480 graphics, 16 colors
- `0x13` = 320x200 graphics, 256 colors

#### Function 0x0E - Teletype Output

```asm
mover ah, 0x0E
mover al, 'A'           ; Character to print
mover bh, 0             ; Page number
mover bl, 0x07          ; Color (white on black)
interrupcion 0x10
```

### INT 16h - Keyboard Services

#### Function 0x00 - Wait for Keystroke

```asm
mover ah, 0x00
interrupcion 0x16
; After: AL = ASCII code, AH = scan code
```

**Common ASCII codes:**
- Enter = 13
- ESC = 27
- Space = 32
- 'A' = 65
- '0' = 48

---

## 📝 Part 5: The Kernel - Dissected

### Main Loop Architecture

Every OS has a main loop:

```asm
bucle_principal:
    ; 1. Wait for event
    mover ah, 0x00
    interrupcion 0x16       ; Wait for key
    
    ; 2. Process event
    comparar al, 27         ; Is it ESC?
    si_igual shutdown
    
    ; 3. Update state
    mover ah, 0x0E
    interrupcion 0x10       ; Echo character
    
    ; 4. Repeat
    saltar bucle_principal
```

### Why HLT (detener)?

**Without HLT:**
```asm
bucle:
    saltar bucle            ; CPU at 100%, hot!
```

**With HLT:**
```asm
bucle:
    detener                 ; CPU sleeps, cool
    saltar bucle
```

**Benefits:**
- Saves power
- Reduces heat
- CPU wakes on interrupts

---

## 🔧 Part 6: Functions and Stack

### The Stack

The stack is a LIFO (Last In, First Out) structure.

```
Initial: SP → [empty]

PUSH AX:  SP → [AX]

PUSH BX:  SP → [BX]
              [AX]

POP CX:   SP → [AX]    (CX now = BX)

POP DX:   SP → [empty] (DX now = AX)
```

### Calling Convention

```asm
; Caller
mover si, cadena
llamar imprimir         ; PUSH return_address, JMP imprimir

; Callee
imprimir:
    meter ax            ; Save AX
    meter bx            ; Save BX
    ; ... do work ...
    sacar bx            ; Restore BX
    sacar ax            ; Restore AX
    retornar            ; POP return_address, JMP return_address
```

### Why Save Registers?

**Bad:**
```asm
function:
    mover ax, 123       ; Destroys caller's AX!
    retornar
```

**Good:**
```asm
function:
    meter ax            ; Save caller's AX
    mover ax, 123       ; Use AX
    sacar ax            ; Restore caller's AX
    retornar
```

---

## 🎓 Part 7: Exercises

### Exercise 1: Change Colors

Modify the kernel to print in different colors.

**Hint:** Change `mover bx, 0x07` to:
- `0x01` = Blue
- `0x02` = Green
- `0x04` = Red
- `0x0E` = Yellow

### Exercise 2: Count Keypresses

Add a counter that shows how many keys were pressed.

**Hint:** Use a variable in the data section:
```asm
contador dw 0
```

### Exercise 3: Command Interpreter

Make the kernel recognize commands like "help" or "clear".

**Hint:** Store typed characters in a buffer and compare when Enter is pressed.

---

## 🐛 Part 8: Common Bugs

### Bug: Triple Fault (Reboot Loop)

**Symptom:** Computer reboots continuously

**Causes:**
1. Stack pointer not initialized
2. Jumping to wrong address
3. Interrupt without proper handler

**Fix:** Always initialize SS:SP!

### Bug: Nothing Appears on Screen

**Causes:**
1. Video mode not set correctly
2. Wrong interrupt number
3. AL contains 0 (null character)

**Fix:** Print a visible character first (like 'A') to test.

### Bug: Disk Read Fails

**Symptom:** Kernel doesn't load

**Causes:**
1. Wrong sector numbers
2. Reading more sectors than exist
3. Buffer address incorrect

**Fix:** Start with reading 1 sector, then increase.

---

## 📚 Resources for Learning More

### Recommended Reading
- **OSDev Wiki** - https://wiki.osdev.org/
- **Ralf Brown's Interrupt List** - BIOS interrupt reference
- **Intel Manuals** - Official x86 documentation

### Next Steps
1. Switch to Protected Mode (32-bit)
2. Set up GDT (Global Descriptor Table)
3. Implement basic drivers (keyboard, timer)
4. Create a simple shell
5. Add file system support

---

## 🎯 Summary

You've learned:
- ✅ How computers boot
- ✅ Memory addressing in Real Mode
- ✅ BIOS interrupts for I/O
- ✅ Writing a bootloader
- ✅ Writing a minimal kernel
- ✅ Stack and calling conventions
- ✅ Event loops
- ✅ All in Spanish with MultiLang-ASM!

---

**Continue learning:** [Examples](Examples) | [How to Use](How-to-Use) | [FAQ](FAQ)

**Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM
