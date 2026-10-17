# MultiLang-ASM: Manual de Instrucciones [FI]

**Idioma:** Finnish / Suomi (`fi`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `hyppää` | `jmp` |
| `jaa` | `div` |
| `jos_eri` | `jne` |
| `jos_nolla` | `jz` |
| `jos_pienempi` | `jl` |
| `jos_sama` | `je` |
| `jos_suurempi` | `jg` |
| `järjestelmäkutsu` | `syscall` |
| `järjestelmäpaluu` | `sysret` |
| `kaksoissana_nelois` | `cdq` |
| `kasvata` | `inc` |
| `kerro` | `mul` |
| `keskeytys` | `int` |
| `kutsu` | `call` |
| `käännä` | `neg` |
| `laajenna_merkki` | `movsx` |
| `laajenna_nolla` | `movzx` |
| `lataa_osoite` | `lea` |
| `lataa_tavu` | `lodsb` |
| `lisää` | `add` |
| `palaa` | `ret` |
| `pienennä` | `dec` |
| `pysäytä` | `hlt` |
| `sana_kaksoissanaksi` | `cwd` |
| `siirrä` | `mov` |
| `siirrä_tavu` | `movsb` |
| `silmukka` | `loop` |
| `silmukka_jos_nolla` | `loopz` |
| `tallenna_tavu` | `stosb` |
| `tavu_sanaksi` | `cbw` |
| `testaa` | `test` |
| `toista` | `rep` |
| `tyhjä` | `nop` |
| `työnnä` | `push` |
| `työnnä_liput` | `pushf` |
| `vaihda` | `xchg` |
| `vedä` | `pop` |
| `vedä_liput` | `popf` |
| `vertaa` | `cmp` |
| `vähennä` | `sub` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Finnish / Suomi (fi)
section .text
global _start

_start:
    siirrä rax, 1
    siirrä rdi, 1
    siirrä rsi, msg
    siirrä rdx, 13
    järjestelmäkutsu

    siirrä rax, 60
    siirrä rdi, 0
    järjestelmäkutsu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm fi programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fi programa.masm
```
