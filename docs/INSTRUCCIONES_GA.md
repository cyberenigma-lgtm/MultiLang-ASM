# MultiLang-ASM: Manual de Instrucciones [GA]

**Idioma:** Irish / Gaeilge (`ga`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `athdhéan` | `rep` |
| `beart_go_focal` | `cbw` |
| `bog` | `mov` |
| `bog_beart` | `movsb` |
| `brúigh` | `push` |
| `brúigh_bratacha` | `pushf` |
| `cuir_i_gcomparáid` | `cmp` |
| `dealú` | `sub` |
| `deicrimint` | `dec` |
| `diúltaigh` | `neg` |
| `dúbailte_go_ceathracha` | `cdq` |
| `filleadh` | `ret` |
| `filleadh_córais` | `sysret` |
| `focal_go_dúbailte` | `cwd` |
| `glaoch` | `call` |
| `glaoch_córais` | `syscall` |
| `idirbhriseadh` | `int` |
| `incrimint` | `inc` |
| `iolraigh` | `mul` |
| `leathnaigh_comhartha` | `movsx` |
| `leathnaigh_nialas` | `movzx` |
| `luchtaigh_beart` | `lodsb` |
| `luchtaigh_seolta` | `lea` |
| `léim` | `jmp` |
| `lúb` | `loop` |
| `lúb_más_nialas` | `loopz` |
| `mhalartaigh` | `xchg` |
| `mura_ionann` | `jne` |
| `más_ionann` | `je` |
| `más_lú` | `jl` |
| `más_mó` | `jg` |
| `más_nialas` | `jz` |
| `pop` | `pop` |
| `pop_bratacha` | `popf` |
| `roinn` | `div` |
| `stad` | `hlt` |
| `stóráil_beart` | `stosb` |
| `suimigh` | `add` |
| `tada` | `nop` |
| `tástáil` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Irish / Gaeilge (ga)
section .text
global _start

_start:
    bog rax, 1
    bog rdi, 1
    bog rsi, msg
    bog rdx, 13
    glaoch_córais

    bog rax, 60
    bog rdi, 0
    glaoch_córais

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ga programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ga programa.masm
```
