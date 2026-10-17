# MultiLang-ASM: Manual de Instrucciones [TE]

**Idioma:** Telugu / తెలుగు (`te`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `అంతరాయం` | `int` |
| `ఆపు` | `hlt` |
| `ఎక్కువైతే` | `jg` |
| `ఏమీ_లేదు` | `nop` |
| `కలుపు` | `add` |
| `గుణించు` | `mul` |
| `గుర్తు_విస్తరణ` | `movsx` |
| `చిరునామా_లోడ్` | `lea` |
| `డবল_క్వాడ్` | `cdq` |
| `తక్కువైతే` | `jl` |
| `తగ్గించు` | `dec` |
| `తిరస్కరించు` | `neg` |
| `తిరిగి_రా` | `ret` |
| `తీయు` | `pop` |
| `తీసివేయి` | `sub` |
| `దూకు` | `jmp` |
| `నెట్టు` | `push` |
| `పరీక్షించు` | `test` |
| `పిలువు` | `call` |
| `పెంచు` | `inc` |
| `పోల్చు` | `cmp` |
| `ఫ్లాగ్_తీయు` | `popf` |
| `ఫ్లాగ్_నెట్టు` | `pushf` |
| `బైట్_మార్చు` | `movsb` |
| `బైట్_లోడ్` | `lodsb` |
| `బైట్_వర్డ్` | `cbw` |
| `బైట్_సేవ్` | `stosb` |
| `భాగించు` | `div` |
| `మళ్ళీ_చేయి` | `rep` |
| `మార్చు` | `mov` |
| `మార్పిడి` | `xchg` |
| `లూప్` | `loop` |
| `వర్డ్_డబుల్` | `cwd` |
| `సమానం_కాకపోతే` | `jne` |
| `సమానమైతే` | `je` |
| `సిస్టమ్_కాల్` | `syscall` |
| `సిస్టమ్_తిరిగి_రా` | `sysret` |
| `సున్నా_అయితే` | `jz` |
| `సున్నా_లూప్` | `loopz` |
| `సున్నా_విస్తరణ` | `movzx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Telugu / తెలుగు (te)
section .text
global _start

_start:
    మార్చు rax, 1
    మార్చు rdi, 1
    మార్చు rsi, msg
    మార్చు rdx, 13
    సిస్టమ్_కాల్

    మార్చు rax, 60
    మార్చు rdi, 0
    సిస్టమ్_కాల్

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm te programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build te programa.masm
```
