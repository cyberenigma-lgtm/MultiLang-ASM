# MultiLang-ASM: Manual de Instrucciones [TPI]

**Idioma:** Tok Pisin (`tpi`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `autim` | `pop` |
| `autim_flek` | `popf` |
| `bek_sistem` | `sysret` |
| `bikim_mak` | `movsx` |
| `bikim_zero` | `movzx` |
| `byte_go_word` | `cbw` |
| `divim` | `div` |
| `double_go_quad` | `cdq` |
| `go_ap` | `inc` |
| `go_bek` | `ret` |
| `go_daun` | `dec` |
| `holim_byte` | `stosb` |
| `kalap` | `jmp` |
| `lodim_adres` | `lea` |
| `lodim_byte` | `lodsb` |
| `lup` | `loop` |
| `lup_sapos_nating` | `loopz` |
| `mekim_gen` | `rep` |
| `minusim` | `sub` |
| `mulpim` | `mul` |
| `muvim` | `mov` |
| `muvim_byte` | `movsb` |
| `nating` | `nop` |
| `no_makim` | `neg` |
| `pinis` | `hlt` |
| `plusim` | `add` |
| `putim_flek` | `pushf` |
| `putim_insait` | `push` |
| `sapos_bik` | `jg` |
| `sapos_liklik` | `jl` |
| `sapos_nating` | `jz` |
| `sapos_no_sem` | `jne` |
| `sapos_sem` | `je` |
| `sekim` | `cmp` |
| `senisim` | `xchg` |
| `singaut` | `call` |
| `singaut_sistem` | `syscall` |
| `stopim` | `int` |
| `testim` | `test` |
| `word_go_double` | `cwd` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Tok Pisin (tpi)
section .text
global _start

_start:
    muvim rax, 1
    muvim rdi, 1
    muvim rsi, msg
    muvim rdx, 13
    singaut_sistem

    muvim rax, 60
    muvim rdi, 0
    singaut_sistem

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tpi programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tpi programa.masm
```
