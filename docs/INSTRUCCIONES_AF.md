# MultiLang-ASM: Manual de Instrucciones [AF]

**Idioma:** Afrikaans (`af`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `as_gelyk` | `je` |
| `as_groter` | `jg` |
| `as_kleiner` | `jl` |
| `as_nie_gelyk` | `jne` |
| `as_nul` | `jz` |
| `brei_nul_uit` | `movzx` |
| `brei_teken_uit` | `movsx` |
| `deel` | `div` |
| `dubbel_na_quad` | `cdq` |
| `greep_na_woord` | `cbw` |
| `haal` | `pop` |
| `haal_vlae` | `popf` |
| `herhaal` | `rep` |
| `keer_terug` | `ret` |
| `laai_effektief` | `lea` |
| `laai_greep` | `lodsb` |
| `lus` | `loop` |
| `lus_as_nul` | `loopz` |
| `niks` | `nop` |
| `onderbreking` | `int` |
| `ontken` | `neg` |
| `roep` | `call` |
| `ruil` | `xchg` |
| `skuif` | `mov` |
| `skuif_greep` | `movsb` |
| `spring` | `jmp` |
| `stelselroep` | `syscall` |
| `stelselterugkeer` | `sysret` |
| `stoor_greep` | `stosb` |
| `stoot` | `push` |
| `stoot_vlae` | `pushf` |
| `stop` | `hlt` |
| `tel_by` | `add` |
| `toets` | `test` |
| `trek_af` | `sub` |
| `vergelyk` | `cmp` |
| `vermeerder` | `inc` |
| `vermenigvuldig` | `mul` |
| `verminder` | `dec` |
| `woord_na_dubbel` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Afrikaans (af)
section .text
global _start

_start:
    skuif rax, 1
    skuif rdi, 1
    skuif rsi, msg
    skuif rdx, 13
    stelselroep

    skuif rax, 60
    skuif rdi, 0
    stelselroep

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm af programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build af programa.masm
```
