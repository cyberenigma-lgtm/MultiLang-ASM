# MultiLang-ASM: Manual de Instrucciones [RO]

**Idioma:** Romanian / Română (`ro`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aduna` | `add` |
| `apel_sistem` | `syscall` |
| `apeleaza` | `call` |
| `bucla` | `loop` |
| `bucla_daca_zero` | `loopz` |
| `byte_la_word` | `cbw` |
| `compara` | `cmp` |
| `daca_egal` | `je` |
| `daca_mai_mare` | `jg` |
| `daca_mai_mic` | `jl` |
| `daca_nu_egal` | `jne` |
| `daca_zero` | `jz` |
| `decrementeaza` | `dec` |
| `double_la_quad` | `cdq` |
| `extinde_semn` | `movsx` |
| `extinde_zero` | `movzx` |
| `imparte` | `div` |
| `incarca_byte` | `lodsb` |
| `incarca_efectiv` | `lea` |
| `incrementeaza` | `inc` |
| `inmulteste` | `mul` |
| `intrerupere` | `int` |
| `muta` | `mov` |
| `muta_byte` | `movsb` |
| `neaga` | `neg` |
| `nimic` | `nop` |
| `opreste` | `hlt` |
| `pune` | `push` |
| `pune_steguri` | `pushf` |
| `repeta` | `rep` |
| `retur_sistem` | `sysret` |
| `returneaza` | `ret` |
| `sari` | `jmp` |
| `scade` | `sub` |
| `schimba` | `xchg` |
| `scoate` | `pop` |
| `scoate_steguri` | `popf` |
| `stocheaza_byte` | `stosb` |
| `testeaza` | `test` |
| `word_la_double` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Romanian / Română (ro)
section .text
global _start

_start:
    muta rax, 1
    muta rdi, 1
    muta rsi, msg
    muta rdx, 13
    apel_sistem

    muta rax, 60
    muta rdi, 0
    apel_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ro programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ro programa.masm
```
