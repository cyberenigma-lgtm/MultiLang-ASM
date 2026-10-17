# MultiLang-ASM: Manual de Instrucciones [LO]

**Idioma:** Lao / ພາສາລາວ (`lo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ກັບຄືນ` | `ret` |
| `ການເອີ້ນລະບົບ` | `syscall` |
| `ຂັດຂວາງ` | `int` |
| `ຄູນ` | `mul` |
| `ຍ້າຍ` | `mov` |
| `ດຶງອອກ` | `pop` |
| `ທົດສອບ` | `test` |
| `ບວກ` | `add` |
| `ບໍ່` | `not` |
| `ບໍ່ມີຫຍັງ` | `nop` |
| `ປຽບທຽບ` | `cmp` |
| `ພິເສດ` | `xor` |
| `ຢຸດ` | `hlt` |
| `ລົບ` | `sub` |
| `ຫານ` | `div` |
| `ຫຼື` | `or` |
| `ຮອບວຽນ` | `loop` |
| `ເຕັ້ນ` | `jmp` |
| `ເອີ້ນ` | `call` |
| `ແລະ` | `and` |
| `ໃສ່` | `push` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Lao / ພາສາລາວ (lo)
section .text
global _start

_start:
    ຍ້າຍ rax, 1
    ຍ້າຍ rdi, 1
    ຍ້າຍ rsi, msg
    ຍ້າຍ rdx, 13
    ການເອີ້ນລະບົບ

    ຍ້າຍ rax, 60
    ຍ້າຍ rdi, 0
    ການເອີ້ນລະບົບ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm lo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build lo programa.masm
```
