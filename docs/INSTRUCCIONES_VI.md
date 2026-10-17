# MultiLang-ASM: Manual de Instrucciones [VI]

**Idioma:** Vietnamese / Tiếng Việt (`vi`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 33  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `byte_sang_word` | `cbw` |
| `chuyen` | `mov` |
| `cong` | `add` |
| `day_co` | `pushf` |
| `day_vao` | `push` |
| `di_chuyen_byte` | `movsb` |
| `dung` | `hlt` |
| `goi` | `call` |
| `goi_he_thong` | `syscall` |
| `khong_lam_gi` | `nop` |
| `kiem_tra` | `test` |
| `lap_lai` | `rep` |
| `lay_co` | `popf` |
| `lay_ra` | `pop` |
| `luu_byte` | `stosb` |
| `nap_dia_chi` | `lea` |
| `neu_bang` | `je` |
| `neu_khac` | `jne` |
| `neu_khong` | `jz` |
| `neu_lon_hon` | `jg` |
| `neu_nho_hon` | `jl` |
| `ngat` | `int` |
| `nhan` | `mul` |
| `nhay` | `jmp` |
| `so_sanh` | `cmp` |
| `tai_byte` | `lodsb` |
| `tra_ve` | `ret` |
| `tra_ve_he_thong` | `sysret` |
| `trao_doi` | `xchg` |
| `tru` | `sub` |
| `vong_lap` | `loop` |
| `vong_lap_neu_khong` | `loopz` |
| `word_sang_double` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Vietnamese / Tiếng Việt (vi)
section .text
global _start

_start:
    chuyen rax, 1
    chuyen rdi, 1
    chuyen rsi, msg
    chuyen rdx, 13
    goi_he_thong

    chuyen rax, 60
    chuyen rdi, 0
    goi_he_thong

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm vi programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build vi programa.masm
```
