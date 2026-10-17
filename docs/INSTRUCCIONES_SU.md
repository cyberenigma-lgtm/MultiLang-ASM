# MultiLang-ASM: Manual de Instrucciones [SU]

**Idioma:** Sundanese / Basa Sunda (`su`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aluar_bandera` | `popf` |
| `aluarkeun` | `pop` |
| `asup_bandera` | `pushf` |
| `asupkeun` | `push` |
| `bagi` | `div` |
| `balik` | `ret` |
| `balik_sistem` | `sysret` |
| `banding` | `cmp` |
| `byte_ka_kecap` | `cbw` |
| `dua_ka_opat` | `cdq` |
| `eureun` | `hlt` |
| `gelung` | `loop` |
| `gelung_lamun_nol` | `loopz` |
| `genti` | `xchg` |
| `gero_sistem` | `syscall` |
| `ingkar` | `neg` |
| `kali` | `mul` |
| `kecap_ka_dua` | `cwd` |
| `kosong` | `nop` |
| `kurang` | `sub` |
| `lamun_beda` | `jne` |
| `lamun_gede` | `jg` |
| `lamun_leutik` | `jl` |
| `lamun_nol` | `jz` |
| `lamun_sarua` | `je` |
| `lega_nol` | `movzx` |
| `lega_tanda` | `movsx` |
| `luncat` | `jmp` |
| `muat_alamat` | `lea` |
| `muat_byte` | `lodsb` |
| `naek` | `inc` |
| `ngagero` | `call` |
| `pindah` | `mov` |
| `pindah_byte` | `movsb` |
| `sela` | `int` |
| `simpen_byte` | `stosb` |
| `tambah` | `add` |
| `turun` | `dec` |
| `uji` | `test` |
| `ulang` | `rep` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Sundanese / Basa Sunda (su)
section .text
global _start

_start:
    pindah rax, 1
    pindah rdi, 1
    pindah rsi, msg
    pindah rdx, 13
    gero_sistem

    pindah rax, 60
    pindah rdi, 0
    gero_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm su programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build su programa.masm
```
