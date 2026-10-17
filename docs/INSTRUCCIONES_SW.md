# MultiLang-ASM: Manual de Instrucciones [SW]

**Idioma:** Swahili / Kiswahili (`sw`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `au` | `or` |
| `badilishana` | `xchg` |
| `baiti_kwa_neno` | `cbw` |
| `gawa` | `div` |
| `hakuna` | `nop` |
| `hamisha` | `mov` |
| `hifadhi_baiti` | `stosb` |
| `ita` | `call` |
| `ito_mfumo` | `syscall` |
| `jaribu` | `test` |
| `jumlisha` | `add` |
| `kama_kubwa` | `jg` |
| `kama_ndogo` | `jl` |
| `kama_sawa` | `je` |
| `kama_sio_sawa` | `jne` |
| `kama_sufuri` | `jz` |
| `katiza` | `int` |
| `linganisha` | `cmp` |
| `mzunguko` | `loop` |
| `mzunguko_kama_sufuri` | `loopz` |
| `na` | `and` |
| `neno_kwa_duara` | `cwd` |
| `ongeza` | `inc` |
| `pakia_anwani` | `lea` |
| `pata_baiti` | `lodsb` |
| `pekee` | `xor` |
| `punguza` | `dec` |
| `rudi` | `ret` |
| `rudi_mfumo` | `sysret` |
| `rudia` | `rep` |
| `ruka` | `jmp` |
| `simama` | `hlt` |
| `sio` | `not` |
| `sogeza_baiti` | `movsb` |
| `sukuma` | `push` |
| `sukuma_bendera` | `pushf` |
| `toa` | `sub` |
| `vuta` | `pop` |
| `vuta_bendera` | `popf` |
| `zidisha` | `mul` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Swahili / Kiswahili (sw)
section .text
global _start

_start:
    hamisha rax, 1
    hamisha rdi, 1
    hamisha rsi, msg
    hamisha rdx, 13
    ito_mfumo

    hamisha rax, 60
    hamisha rdi, 0
    ito_mfumo

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sw programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sw programa.masm
```
