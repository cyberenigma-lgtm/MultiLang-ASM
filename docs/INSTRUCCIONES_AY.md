# MultiLang-ASM: Manual de Instrucciones [AY]

**Idioma:** Aymara (`ay`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `apaqaña` | `sub` |
| `apsuña` | `pop` |
| `aswan_jach'a` | `jg` |
| `aswan_jisk'a` | `jl` |
| `byte_imayaña` | `stosb` |
| `byte_katuña` | `lodsb` |
| `byte_kuna` | `movsb` |
| `byte_wordtech` | `cbw` |
| `ch'usa_hina` | `jz` |
| `ch'usa_mast'aña` | `movzx` |
| `ch'usa_muyuta` | `loopz` |
| `double_quadtech` | `cdq` |
| `jaljaña` | `div` |
| `jani_arunayaña` | `neg` |
| `jani_kipka` | `jne` |
| `jani_kunnasa` | `nop` |
| `jawsaña` | `call` |
| `jilayaña` | `inc` |
| `katuña` | `lea` |
| `kipka_hina` | `je` |
| `kipkaña` | `cmp` |
| `kuna` | `mov` |
| `kutiyaña` | `rep` |
| `kutiña` | `ret` |
| `mirayaña` | `mul` |
| `muyuta` | `loop` |
| `pisiyaña` | `dec` |
| `samaña` | `int` |
| `sayayaña` | `hlt` |
| `sistema_jawsaña` | `syscall` |
| `sistema_kutiña` | `sysret` |
| `t'it'iña` | `jmp` |
| `turkaña` | `xchg` |
| `uchuqaña` | `push` |
| `unancha_apsu` | `popf` |
| `unancha_mast'aña` | `movsx` |
| `unancha_uchuqa` | `pushf` |
| `word_doubletech` | `cwd` |
| `yant'aña` | `test` |
| `yapaña` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Aymara (ay)
section .text
global _start

_start:
    kuna rax, 1
    kuna rdi, 1
    kuna rsi, msg
    kuna rdx, 13
    sistema_jawsaña

    kuna rax, 60
    kuna rdi, 0
    sistema_jawsaña

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ay programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ay programa.masm
```
