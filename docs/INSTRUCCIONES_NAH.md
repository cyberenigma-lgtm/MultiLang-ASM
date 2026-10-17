# MultiLang-ASM: Manual de Instrucciones [NAH]

**Idioma:** Nahuatl / Mexicano (`nah`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ahcic` | `dec` |
| `amo` | `neg` |
| `amo_itla` | `nop` |
| `amo_neneuh` | `jne` |
| `ay_tic_tlapalo` | `movzx` |
| `ayac_malacatl` | `loopz` |
| `ayac_neneuh` | `jz` |
| `byte_huica` | `movsb` |
| `byte_wordtech` | `cbw` |
| `chicahua` | `inc` |
| `choloa` | `jmp` |
| `cuepa` | `ret` |
| `double_quadtech` | `cdq` |
| `flag_huica` | `pushf` |
| `flag_quixtia` | `popf` |
| `hueyi` | `jg` |
| `huica` | `mov` |
| `kargay_byte` | `lodsb` |
| `malacatl` | `loop` |
| `miquilia` | `mul` |
| `neneuhqui` | `je` |
| `notza` | `call` |
| `patla` | `xchg` |
| `quixtia` | `pop` |
| `tepitzin` | `jl` |
| `tequitl_cuepa` | `sysret` |
| `tequitl_notza` | `syscall` |
| `tlanonotza` | `cmp` |
| `tlapohua` | `add` |
| `tlatzacuia` | `sub` |
| `tlatzacuia_byte` | `stosb` |
| `tlatzacuia_maca` | `lea` |
| `tlatzacuilli_huica` | `push` |
| `tzacuia` | `int` |
| `uactia` | `hlt` |
| `unancha_tlapalo` | `movsx` |
| `word_doubletech` | `cwd` |
| `xelua` | `div` |
| `yancuic` | `rep` |
| `yehuatl` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Nahuatl / Mexicano (nah)
section .text
global _start

_start:
    huica rax, 1
    huica rdi, 1
    huica rsi, msg
    huica rdx, 13
    tequitl_notza

    huica rax, 60
    huica rdi, 0
    tequitl_notza

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm nah programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build nah programa.masm
```
