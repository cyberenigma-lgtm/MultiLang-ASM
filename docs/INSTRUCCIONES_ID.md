# MultiLang-ASM: Manual de Instrucciones [ID]

**Idioma:** Indonesian / Bahasa Indonesia (`id`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 44  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `bagi` | `div` |
| `bagi_tanda` | `idiv` |
| `bandingkan` | `cmp` |
| `byte_ke_word` | `cbw` |
| `double_ke_quad` | `cdq` |
| `henti` | `hlt` |
| `interupsi` | `int` |
| `jika_beda` | `jne` |
| `jika_lebih_besar` | `jg` |
| `jika_lebih_kecil` | `jl` |
| `jika_nol` | `jz` |
| `jika_sama` | `je` |
| `jumlah` | `add` |
| `kali` | `mul` |
| `kali_tanda` | `imul` |
| `keluarkan` | `pop` |
| `keluarkan_flag` | `popf` |
| `kembali` | `ret` |
| `kembali_sistem` | `sysret` |
| `kosong` | `nop` |
| `kurang` | `sub` |
| `kurang_satu` | `dec` |
| `lompat` | `jmp` |
| `masukkan` | `push` |
| `masukkan_flag` | `pushf` |
| `muat_byte` | `lodsb` |
| `muat_efektif` | `lea` |
| `negatif` | `neg` |
| `panggil` | `call` |
| `panggilan_sistem` | `syscall` |
| `perpanjang_nol` | `movzx` |
| `perpanjang_tanda` | `movsx` |
| `pindah` | `mov` |
| `pindah_byte` | `movsb` |
| `putaran` | `loop` |
| `putaran_jika_nol` | `loopz` |
| `salin` | `mov` |
| `simpan_byte` | `stosb` |
| `tambah` | `add` |
| `tambah_satu` | `inc` |
| `tukar` | `xchg` |
| `uji` | `test` |
| `ulang` | `rep` |
| `word_ke_double` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Indonesian / Bahasa Indonesia (id)
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
mlasm id programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build id programa.masm
```
