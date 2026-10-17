# MultiLang-ASM: Manual de Instrucciones [EN_SC]

**Idioma:** Scottish English / Scots (`en_sc`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `again` | `rep` |
| `an` | `and` |
| `back` | `ret` |
| `big_to_mair` | `cwd` |
| `birl` | `loop` |
| `birling_nought` | `loopz` |
| `ca` | `call` |
| `canny` | `test` |
| `cry_system` | `syscall` |
| `divide` | `div` |
| `dock` | `sub` |
| `fetch` | `lea` |
| `gang_hame` | `sysret` |
| `gin_equal` | `je` |
| `gin_mair` | `jg` |
| `gin_no_equal` | `jne` |
| `gin_nought` | `jz` |
| `gin_wee` | `jl` |
| `grab_byte` | `lodsb` |
| `haud` | `int` |
| `heeze` | `inc` |
| `loup` | `jmp` |
| `lowp` | `dec` |
| `multiply` | `mul` |
| `neer` | `cmp` |
| `no` | `not` |
| `nowt` | `nop` |
| `or` | `or` |
| `pit` | `mov` |
| `pull` | `pop` |
| `pull_flags` | `popf` |
| `shift_byte` | `movsb` |
| `shove` | `push` |
| `shove_flags` | `pushf` |
| `stash_byte` | `stosb` |
| `swap` | `xchg` |
| `tot` | `add` |
| `wee_to_big` | `cbw` |
| `wheesht` | `hlt` |
| `xor` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Scottish English / Scots (en_sc)
section .text
global _start

_start:
    pit rax, 1
    pit rdi, 1
    pit rsi, msg
    pit rdx, 13
    cry_system

    pit rax, 60
    pit rdi, 0
    cry_system

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm en_sc programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build en_sc programa.masm
```
