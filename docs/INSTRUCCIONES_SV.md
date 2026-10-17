# MultiLang-ASM: Manual de Instrucciones [SV]

**Idioma:** Swedish / Svenska (`sv`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 39  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `addera` | `add` |
| `anropa` | `call` |
| `avbrott` | `int` |
| `byt` | `xchg` |
| `dividera` | `div` |
| `eller` | `or` |
| `flytta` | `mov` |
| `flytta_byte` | `movsb` |
| `hoppa` | `jmp` |
| `inget` | `nop` |
| `inte` | `not` |
| `jamfor` | `cmp` |
| `ladda_adress` | `lea` |
| `ladda_byte` | `lodsb` |
| `lagg` | `push` |
| `lagg_flaggor` | `pushf` |
| `loop` | `loop` |
| `loop_om_noll` | `loopz` |
| `minska` | `dec` |
| `multiplicera` | `mul` |
| `negera` | `neg` |
| `och` | `and` |
| `oka` | `inc` |
| `om_lika` | `je` |
| `om_mindre` | `jl` |
| `om_noll` | `jz` |
| `om_olika` | `jne` |
| `om_storre` | `jg` |
| `repetera` | `rep` |
| `returnera` | `ret` |
| `spara_byte` | `stosb` |
| `stopp` | `hlt` |
| `subtrahera` | `sub` |
| `systemanrop` | `syscall` |
| `systemretur` | `sysret` |
| `ta` | `pop` |
| `ta_flaggor` | `popf` |
| `testa` | `test` |
| `xor` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Swedish / Svenska (sv)
section .text
global _start

_start:
    flytta rax, 1
    flytta rdi, 1
    flytta rsi, msg
    flytta rdx, 13
    systemanrop

    flytta rax, 60
    flytta rdi, 0
    systemanrop

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm sv programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build sv programa.masm
```
