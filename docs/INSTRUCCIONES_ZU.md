# MultiLang-ASM: Manual de Instrucciones [ZU]

**Idioma:** Zulu / isiZulu (`zu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `andisa_iqanda` | `movzx` |
| `andisa_uphawu` | `movsx` |
| `biza` | `call` |
| `buya` | `ret` |
| `eqa` | `jmp` |
| `faka` | `push` |
| `faka_amaflag` | `pushf` |
| `gcina_ibyte` | `stosb` |
| `hambisa` | `mov` |
| `hambisa_ibyte` | `movsb` |
| `hlanganisa` | `add` |
| `hlola` | `test` |
| `hlukanisa` | `div` |
| `ibyte_iya_egameni` | `cbw` |
| `igama_iya_kabili` | `cwd` |
| `ikabili_iya_quad` | `cdq` |
| `iluphu` | `loop` |
| `iluphu_uma_iqanda` | `loopz` |
| `khipha` | `pop` |
| `khipha_amaflag` | `popf` |
| `khulisa` | `inc` |
| `layisha_ibyte` | `lodsb` |
| `layisha_ikheli` | `lea` |
| `lutho` | `nop` |
| `misa` | `hlt` |
| `nciphisa` | `dec` |
| `phika` | `neg` |
| `phinda` | `rep` |
| `phindaphinda` | `mul` |
| `qhathanisa` | `cmp` |
| `shintshisana` | `xchg` |
| `susa` | `sub` |
| `ukubizwa_kwesistimu` | `syscall` |
| `ukubuya_kwesistimu` | `sysret` |
| `uma_iqanda` | `jz` |
| `uma_kukhulu` | `jg` |
| `uma_kulingana` | `je` |
| `uma_kuncane` | `jl` |
| `uma_kungalingani` | `jne` |
| `uphazamiso` | `int` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Zulu / isiZulu (zu)
section .text
global _start

_start:
    hambisa rax, 1
    hambisa rdi, 1
    hambisa rsi, msg
    hambisa rdx, 13
    ukubizwa_kwesistimu

    hambisa rax, 60
    hambisa rdi, 0
    ukubizwa_kwesistimu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm zu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build zu programa.masm
```
