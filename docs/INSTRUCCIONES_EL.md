# MultiLang-ASM: Manual de Instrucciones [EL]

**Idioma:** Greek / Ελληνικά (`el`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 33  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `byte_σε_word` | `cbw` |
| `word_σε_double` | `cwd` |
| `άλμα` | `jmp` |
| `έλεγχος` | `test` |
| `ανταλλαγή` | `xchg` |
| `αποθήκευση_byte` | `stosb` |
| `αφαίρεση` | `sub` |
| `βρόχος` | `loop` |
| `βρόχος_εάν_μηδέν` | `loopz` |
| `διακοπή` | `int` |
| `εάν_ίσο` | `je` |
| `εάν_μεγαλύτερο` | `jg` |
| `εάν_μηδέν` | `jz` |
| `εάν_μικρότερο` | `jl` |
| `εάν_όχι_ίσο` | `jne` |
| `εξαγωγή` | `pop` |
| `εξαγωγή_σημαιών` | `popf` |
| `επανάληψη` | `rep` |
| `επιστροφή` | `ret` |
| `επιστροφή_συστήματος` | `sysret` |
| `κλήση` | `call` |
| `κλήση_συστήματος` | `syscall` |
| `μετακίνηση` | `mov` |
| `μετακίνηση_byte` | `movsb` |
| `παύση` | `hlt` |
| `πολλαπλασιασμός` | `mul` |
| `πρόσθεση` | `add` |
| `σύγκριση` | `cmp` |
| `τίποτα` | `nop` |
| `φόρτωση` | `lea` |
| `φόρτωση_byte` | `lodsb` |
| `ώθηση` | `push` |
| `ώθηση_σημαιών` | `pushf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Greek / Ελληνικά (el)
section .text
global _start

_start:
    μετακίνηση rax, 1
    μετακίνηση rdi, 1
    μετακίνηση rsi, msg
    μετακίνηση rdx, 13
    κλήση_συστήματος

    μετακίνηση rax, 60
    μετακίνηση rdi, 0
    κλήση_συστήματος

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm el programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build el programa.masm
```
