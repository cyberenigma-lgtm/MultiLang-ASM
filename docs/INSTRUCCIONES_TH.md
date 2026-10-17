# MultiLang-ASM: Manual de Instrucciones [TH]

**Idioma:** Thai / ไทย (`th`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 33  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `กระโดด` | `jmp` |
| `กลับ` | `ret` |
| `ขัดจังหวะ` | `int` |
| `คืนค่าระบบ` | `sysret` |
| `คูณ` | `mul` |
| `ดึง` | `pop` |
| `ดึงแฟล็ก` | `popf` |
| `ถ้าน้อยกว่า` | `jl` |
| `ถ้ามากกว่า` | `jg` |
| `ถ้าเท่ากับ` | `je` |
| `ถ้าเป็นศูนย์` | `jz` |
| `ถ้าไม่เท่ากับ` | `jne` |
| `ทดสอบ` | `test` |
| `ทำซ้ำ` | `rep` |
| `บวก` | `add` |
| `ผลัก` | `push` |
| `ผลักแฟล็ก` | `pushf` |
| `ย้าย` | `mov` |
| `ย้ายไบต์` | `movsb` |
| `ลบ` | `sub` |
| `วนรอบ` | `loop` |
| `วนรอบถ้าเป็นศูนย์` | `loopz` |
| `สลับ` | `xchg` |
| `หยุด` | `hlt` |
| `เก็บบายต์` | `stosb` |
| `เปรียบเทียบ` | `cmp` |
| `เรียก` | `call` |
| `เรียกใช้ระบบ` | `syscall` |
| `เวิร์ดเป็นดับเบิล` | `cwd` |
| `โหลด` | `lea` |
| `โหลดไบต์` | `lodsb` |
| `ไบต์เป็นเวิร์ด` | `cbw` |
| `ไม่มีการทำงาน` | `nop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Thai / ไทย (th)
section .text
global _start

_start:
    ย้าย rax, 1
    ย้าย rdi, 1
    ย้าย rsi, msg
    ย้าย rdx, 13
    เรียกใช้ระบบ

    ย้าย rax, 60
    ย้าย rdi, 0
    เรียกใช้ระบบ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm th programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build th programa.masm
```
