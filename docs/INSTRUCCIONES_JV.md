# MultiLang-ASM: Manual de Instrucciones [JV]

**Idioma:** Javanese / Basa Jawa (`jv`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `baleni` | `rep` |
| `bali` | `ret` |
| `bali_sistem` | `sysret` |
| `banding` | `cmp` |
| `byte_neng_word` | `cbw` |
| `double_neng_quad` | `cdq` |
| `gelung` | `loop` |
| `gelung_yen_nol` | `loopz` |
| `ijol` | `xchg` |
| `jembar_nol` | `movzx` |
| `jembar_tanda` | `movsx` |
| `lebokne` | `push` |
| `lebokne_gendero` | `pushf` |
| `mandeg` | `hlt` |
| `mlumpat` | `jmp` |
| `muat_alamat` | `lea` |
| `muat_byte` | `lodsb` |
| `mungkur` | `neg` |
| `ora_ono` | `nop` |
| `para` | `div` |
| `pindah` | `mov` |
| `pindah_byte` | `movsb` |
| `ping` | `mul` |
| `selo` | `int` |
| `simpen_byte` | `stosb` |
| `suda` | `sub` |
| `suda_siji` | `dec` |
| `tambah` | `add` |
| `tambah_siji` | `inc` |
| `timbal` | `call` |
| `timbal_sistem` | `syscall` |
| `uji` | `test` |
| `wetokne` | `pop` |
| `wetokne_gendero` | `popf` |
| `word_neng_double` | `cwd` |
| `yen_bedo` | `jne` |
| `yen_kurang` | `jl` |
| `yen_luwih` | `jg` |
| `yen_nol` | `jz` |
| `yen_podo` | `je` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Javanese / Basa Jawa (jv)
section .text
global _start

_start:
    pindah rax, 1
    pindah rdi, 1
    pindah rsi, msg
    pindah rdx, 13
    timbal_sistem

    pindah rax, 60
    pindah rdi, 0
    timbal_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm jv programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build jv programa.masm
```
