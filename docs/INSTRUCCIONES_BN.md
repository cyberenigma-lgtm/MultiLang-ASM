# MultiLang-ASM: Manual de Instrucciones [BN]

**Idioma:** Bengali / বাংলা (`bn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `если_больше` | `jg` |
| `অস্বীকার` | `neg` |
| `অ্যাড্রেস_লোড` | `lea` |
| `ইন্টারাপ্ট` | `int` |
| `ওয়ার্ড_থেকে_ডাবল` | `cwd` |
| `কল` | `call` |
| `কিছু_না` | `nop` |
| `গুণ` | `mul` |
| `চিহ্ন_প্রসারণ` | `movsx` |
| `ডাবল_থেকে_কোয়াড` | `cdq` |
| `তুলনা` | `cmp` |
| `থামানো` | `hlt` |
| `পপ` | `pop` |
| `পরীক্ষা` | `test` |
| `পুনরাবৃত্তি` | `rep` |
| `পুশ` | `push` |
| `ফেরা` | `ret` |
| `ফ্ল্যাগ_পপ` | `popf` |
| `ফ্ল্যাগ_পুশ` | `pushf` |
| `বাইট_থেকে_ওয়ার্ড` | `cbw` |
| `বাইট_লোড` | `lodsb` |
| `বাইট_সংরক্ষণ` | `stosb` |
| `বাইট_সরানো` | `movsb` |
| `বিনিময়` | `xchg` |
| `বিয়োগ` | `sub` |
| `বৃদ্ধি` | `inc` |
| `ভাগ` | `div` |
| `যদি_অসমান` | `jne` |
| `যদি_ছোট` | `jl` |
| `যদি_শূন্য` | `jz` |
| `যদি_সমান` | `je` |
| `যোগ` | `add` |
| `লাফানো` | `jmp` |
| `লুপ` | `loop` |
| `শূন্য_প্রসারণ` | `movzx` |
| `শূন্য_লুপ` | `loopz` |
| `সরানো` | `mov` |
| `সিস্টেম_কল` | `syscall` |
| `সিস্টেম_রিটার্ন` | `sysret` |
| `হ্রাস` | `dec` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Bengali / বাংলা (bn)
section .text
global _start

_start:
    সরানো rax, 1
    সরানো rdi, 1
    সরানো rsi, msg
    সরানো rdx, 13
    সিস্টেম_কল

    সরানো rax, 60
    সরানো rdi, 0
    সিস্টেম_কল

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm bn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build bn programa.masm
```
