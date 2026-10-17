# MultiLang-ASM: Manual de Instrucciones [MS]

**Idioma:** Malay / Bahasa Melayu (`ms`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `bahagi` | `div` |
| `bait_ke_kata` | `cbw` |
| `banding` | `cmp` |
| `darab` | `mul` |
| `gelung` | `loop` |
| `gelung_jika_sifar` | `loopz` |
| `henti` | `hlt` |
| `jika_besar` | `jg` |
| `jika_beza` | `jne` |
| `jika_kecil` | `jl` |
| `jika_sama` | `je` |
| `jika_sifar` | `jz` |
| `kata_ke_kembar` | `cwd` |
| `kembali` | `ret` |
| `kembali_sistem` | `sysret` |
| `kembar_ke_quad` | `cdq` |
| `kosong` | `nop` |
| `lompat` | `jmp` |
| `luas_sifar` | `movzx` |
| `luas_tanda` | `movsx` |
| `muat_bait` | `lodsb` |
| `muat_efektif` | `lea` |
| `naik` | `inc` |
| `panggil` | `call` |
| `panggilan_sistem` | `syscall` |
| `pindah` | `mov` |
| `pindah_bait` | `movsb` |
| `sampuk` | `int` |
| `sangkal` | `neg` |
| `simpan_bait` | `stosb` |
| `tambah` | `add` |
| `tarik_bendera` | `popf` |
| `tarik_keluar` | `pop` |
| `tolak` | `sub` |
| `tolak_bendera` | `pushf` |
| `tolak_masuk` | `push` |
| `tukar` | `xchg` |
| `turun` | `dec` |
| `uji` | `test` |
| `ulang` | `rep` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Malay / Bahasa Melayu (ms)
section .text
global _start

_start:
    pindah rax, 1
    pindah rdi, 1
    pindah rsi, msg
    pindah rdx, 13
    panggilan_sistem

    pindah rax, 60
    pindah rdi, 0
    panggilan_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ms programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ms programa.masm
```
