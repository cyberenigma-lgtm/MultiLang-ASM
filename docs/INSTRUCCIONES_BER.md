# MultiLang-ASM: Manual de Instrucciones [BER]

**Idioma:** Berber / Tamazight (`ber`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ader_byte` | `lodsb` |
| `ader_tansa` | `lea` |
| `agi` | `neg` |
| `als` | `rep` |
| `arem` | `test` |
| `azmam` | `loop` |
| `azmam_ma_ilem` | `loopz` |
| `byte_ar_tguri` | `cbw` |
| `bḍu` | `div` |
| `ekkes` | `sub` |
| `fukk` | `int` |
| `ma_igda` | `je` |
| `ma_ilem` | `jz` |
| `ma_imeqqer` | `jg` |
| `ma_imeẓẓi` | `jl` |
| `ma_ur_igda` | `jne` |
| `neḍ` | `jmp` |
| `rnu` | `add` |
| `sekker` | `pop` |
| `sekker_tamatart` | `popf` |
| `semɣer_ilem` | `movzx` |
| `semɣer_tamatart` | `movsx` |
| `senfel` | `xchg` |
| `seres` | `push` |
| `seres_tamatart` | `pushf` |
| `sget` | `mul` |
| `sidrus` | `dec` |
| `sihel` | `mov` |
| `sihel_byte` | `movsb` |
| `simɣer` | `inc` |
| `siwel` | `call` |
| `siwel_unagraw` | `syscall` |
| `taguri_ar_tusna` | `cwd` |
| `tusna_ar_quad` | `cdq` |
| `uɣal` | `ret` |
| `uɣal_unagraw` | `sysret` |
| `walat` | `nop` |
| `zer` | `cmp` |
| `ḥbes` | `hlt` |
| `ḥerz_byte` | `stosb` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Berber / Tamazight (ber)
section .text
global _start

_start:
    sihel rax, 1
    sihel rdi, 1
    sihel rsi, msg
    sihel rdx, 13
    siwel_unagraw

    sihel rax, 60
    sihel rdi, 0
    siwel_unagraw

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ber programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ber programa.masm
```
