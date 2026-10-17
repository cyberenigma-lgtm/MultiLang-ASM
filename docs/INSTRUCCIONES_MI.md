# MultiLang-ASM: Manual de Instrucciones [MI]

**Idioma:** Maori / Te Reo Māori (`mi`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aukati` | `int` |
| `byte_ki_focal` | `cbw` |
| `double_ki_quad` | `cdq` |
| `fari` | `xchg` |
| `focal_ki_double` | `cwd` |
| `hoki` | `ret` |
| `hoki_pūnaha` | `sysret` |
| `kahore` | `nop` |
| `karanga` | `call` |
| `karanga_pūnaha` | `syscall` |
| `koropiko` | `loop` |
| `koropiko_mehemea_kore` | `loopz` |
| `mehemea_iti` | `jl` |
| `mehemea_kore` | `jz` |
| `mehemea_kore_rite` | `jne` |
| `mehemea_nui` | `jg` |
| `mehemea_rite` | `je` |
| `neke` | `mov` |
| `neke_byte` | `movsb` |
| `peke` | `jmp` |
| `pūmau_byte` | `stosb` |
| `tango` | `sub` |
| `tene` | `push` |
| `tene_tohu` | `pushf` |
| `tukurua` | `rep` |
| `tāpiri` | `add` |
| `unu` | `pop` |
| `unu_tohu` | `popf` |
| `uta_byte` | `lodsb` |
| `uta_nohoanga` | `lea` |
| `wehe` | `div` |
| `whakakore` | `neg` |
| `whakamutu` | `hlt` |
| `whakamātau` | `test` |
| `whakapalo` | `dec` |
| `whakapiki` | `inc` |
| `whakarea` | `mul` |
| `whakataurite` | `cmp` |
| `whakawhanui_kore` | `movzx` |
| `whakawhanui_tohu` | `movsx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Maori / Te Reo Māori (mi)
section .text
global _start

_start:
    neke rax, 1
    neke rdi, 1
    neke rsi, msg
    neke rdx, 13
    karanga_pūnaha

    neke rax, 60
    neke rdi, 0
    karanga_pūnaha

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm mi programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build mi programa.masm
```
