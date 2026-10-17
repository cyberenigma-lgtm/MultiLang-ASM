# MultiLang-ASM: Manual de Instrucciones [YO]

**Idioma:** Yoruba (`yo`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `asán` | `nop` |
| `bi_o_ba_dogba` | `je` |
| `bi_o_ba_kere` | `jl` |
| `bi_o_ba_odo` | `jz` |
| `bi_o_ba_tobi` | `jg` |
| `bi_o_ba_yatọ` | `jne` |
| `byte_si_ọrọ` | `cbw` |
| `da_duro` | `int` |
| `danwo` | `test` |
| `duro` | `hlt` |
| `faagun_ami` | `movsx` |
| `faagun_odo` | `movzx` |
| `fikun` | `add` |
| `fikun_ẹyọ` | `inc` |
| `fipamọ_byte` | `stosb` |
| `fiwe` | `cmp` |
| `gbe` | `mov` |
| `gbe_byte` | `movsb` |
| `kojọpọ_adirẹsi` | `lea` |
| `kojọpọ_byte` | `lodsb` |
| `meji_si_mẹrin` | `cdq` |
| `mẹfọ` | `jmp` |
| `paarọ` | `xchg` |
| `padà` | `ret` |
| `padà_eto` | `sysret` |
| `pe_eto` | `syscall` |
| `pin` | `div` |
| `pè` | `call` |
| `pọsi` | `mul` |
| `sẹ` | `neg` |
| `tunṣe` | `rep` |
| `tì` | `push` |
| `tì_asia` | `pushf` |
| `yipo` | `loop` |
| `yipo_bi_o_ba_odo` | `loopz` |
| `yọ` | `pop` |
| `yọ_asia` | `popf` |
| `yọkuro` | `sub` |
| `yọkuro_ẹyọ` | `dec` |
| `ọrọ_si_meji` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Yoruba (yo)
section .text
global _start

_start:
    gbe rax, 1
    gbe rdi, 1
    gbe rsi, msg
    gbe rdx, 13
    pe_eto

    gbe rax, 60
    gbe rdi, 0
    pe_eto

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm yo programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build yo programa.masm
```
