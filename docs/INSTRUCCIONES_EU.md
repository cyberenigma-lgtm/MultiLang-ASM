# MultiLang-ASM: Manual de Instrucciones [EU]

**Idioma:** Basque / Euskara (`eu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `atera` | `pop` |
| `banderak_atera` | `popf` |
| `banderak_sartu` | `pushf` |
| `begizta` | `loop` |
| `berdina_bada` | `je` |
| `biderkatu` | `mul` |
| `bikoitza_quadrera` | `cdq` |
| `byte_gorde` | `stosb` |
| `byte_hitzera` | `cbw` |
| `byte_kargatu` | `lodsb` |
| `byte_mugitu` | `movsb` |
| `deitu` | `call` |
| `dekrementatu` | `dec` |
| `errepikatu` | `rep` |
| `etena` | `int` |
| `ez_berdina_bada` | `jne` |
| `ezer_ez` | `nop` |
| `gehitu` | `add` |
| `gelditu` | `hlt` |
| `handiagoa_bada` | `jg` |
| `helbidea_kargatu` | `lea` |
| `hitza_bikoitzera` | `cwd` |
| `inkrementatu` | `inc` |
| `itzuli` | `ret` |
| `jauzi` | `jmp` |
| `kendu` | `sub` |
| `konparatu` | `cmp` |
| `mugitu` | `mov` |
| `probatu` | `test` |
| `sartu` | `push` |
| `sistema_deia` | `syscall` |
| `sistema_itzulera` | `sysret` |
| `trukatu` | `xchg` |
| `txikiagoa_bada` | `jl` |
| `ukatu` | `neg` |
| `zatitu` | `div` |
| `zeinu_hedatu` | `movsx` |
| `zero_bada` | `jz` |
| `zero_bada_begizta` | `loopz` |
| `zero_hedatu` | `movzx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Basque / Euskara (eu)
section .text
global _start

_start:
    mugitu rax, 1
    mugitu rdi, 1
    mugitu rsi, msg
    mugitu rdx, 13
    sistema_deia

    mugitu rax, 60
    mugitu rdi, 0
    sistema_deia

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm eu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build eu programa.masm
```
