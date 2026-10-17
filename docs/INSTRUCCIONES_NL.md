# MultiLang-ASM: Manual de Instrucciones [NL]

**Idioma:** Dutch / Nederlands (`nl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 39  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aftrekken` | `sub` |
| `als_gelijk` | `je` |
| `als_groter` | `jg` |
| `als_kleiner` | `jl` |
| `als_niet_gelijk` | `jne` |
| `als_nul` | `jz` |
| `delen` | `div` |
| `duw` | `push` |
| `duw_vlaggen` | `pushf` |
| `en` | `and` |
| `herhaal` | `rep` |
| `keer_terug` | `ret` |
| `laad_adres` | `lea` |
| `laad_byte` | `lodsb` |
| `lus` | `loop` |
| `lus_als_nul` | `loopz` |
| `niet` | `not` |
| `niets` | `nop` |
| `of` | `or` |
| `onderbreking` | `int` |
| `ontkennen` | `neg` |
| `optellen` | `add` |
| `roep` | `call` |
| `sla_byte_op` | `stosb` |
| `spring` | `jmp` |
| `stop` | `hlt` |
| `systeem_terug` | `sysret` |
| `systeemaanroep` | `syscall` |
| `test` | `test` |
| `trek` | `pop` |
| `trek_vlaggen` | `popf` |
| `vergelijk` | `cmp` |
| `verhogen` | `inc` |
| `verlagen` | `dec` |
| `vermenigvuldigen` | `mul` |
| `verplaats` | `mov` |
| `verplaats_byte` | `movsb` |
| `wissel` | `xchg` |
| `xor` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Dutch / Nederlands (nl)
section .text
global _start

_start:
    verplaats rax, 1
    verplaats rdi, 1
    verplaats rsi, msg
    verplaats rdx, 13
    systeemaanroep

    verplaats rax, 60
    verplaats rdi, 0
    systeemaanroep

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm nl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build nl programa.masm
```
