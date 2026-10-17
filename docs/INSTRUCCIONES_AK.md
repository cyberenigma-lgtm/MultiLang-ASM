# MultiLang-ASM: Manual de Instrucciones [AK]

**Idioma:** Akan (`ak`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `asɛmfua_kɔ_mmienu` | `cwd` |
| `ba_man` | `ret` |
| `ba_nhyehyɛe` | `sysret` |
| `byte_kɔ_asɛmfua` | `cbw` |
| `dɔɔso` | `mul` |
| `fa_atadi` | `lea` |
| `fa_byte` | `lodsb` |
| `frɛ` | `call` |
| `frɛ_nhyehyɛe` | `syscall` |
| `gyae` | `int` |
| `gyina` | `hlt` |
| `huri` | `jmp` |
| `hwee_nni_hɔ` | `nop` |
| `ka_ho` | `add` |
| `kyɛ` | `div` |
| `kɔ_to_ho` | `loop` |
| `kɔ_to_ho_sɛ_hwee` | `loopz` |
| `ma_ɛnyɛ_ketewa` | `dec` |
| `ma_ɛnyɛ_kɛse` | `inc` |
| `mmienu_kɔ_nan` | `cdq` |
| `pia_frankaa` | `pushf` |
| `pia_mu` | `push` |
| `po` | `neg` |
| `san_yɛ` | `rep` |
| `sesa` | `xchg` |
| `sie_byte` | `stosb` |
| `sɔ_hwɛ` | `test` |
| `sɛ_ɛnyɛ_pɛ` | `jne` |
| `sɛ_ɛsõ` | `jg` |
| `sɛ_ɛyɛ_hwee` | `jz` |
| `sɛ_ɛyɛ_ketewa` | `jl` |
| `sɛ_ɛyɛ_pɛ` | `je` |
| `toto` | `cmp` |
| `trɛw_hwee` | `movzx` |
| `trɛw_nsɛnkyerɛnne` | `movsx` |
| `tu` | `mov` |
| `tu_byte` | `movsb` |
| `yi_adi` | `pop` |
| `yi_fi_mu` | `sub` |
| `yi_frankaa` | `popf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Akan (ak)
section .text
global _start

_start:
    tu rax, 1
    tu rdi, 1
    tu rsi, msg
    tu rdx, 13
    frɛ_nhyehyɛe

    tu rax, 60
    tu rdi, 0
    frɛ_nhyehyɛe

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ak programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ak programa.masm
```
