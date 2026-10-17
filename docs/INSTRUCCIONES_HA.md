# MultiLang-ASM: Manual de Instrucciones [HA]

**Idioma:** Hausa (`ha`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ajiye_byte` | `stosb` |
| `babu` | `nop` |
| `biyu_zuwa_hudu` | `cdq` |
| `byte_zuwa_kalma` | `cbw` |
| `cire` | `pop` |
| `cire_tuta` | `popf` |
| `dakatar` | `hlt` |
| `fadada_shara` | `movsx` |
| `fadada_sifiri` | `movzx` |
| `gwada` | `cmp` |
| `idan_ba_daidai_ba` | `jne` |
| `idan_daidai` | `je` |
| `idan_fi` | `jg` |
| `idan_kasa` | `jl` |
| `idan_sifiri` | `jz` |
| `jarraba` | `test` |
| `kalma_zuwa_biyu` | `cwd` |
| `kara` | `add` |
| `kara_daya` | `inc` |
| `karyata` | `neg` |
| `kira` | `call` |
| `kiran_tsarin` | `syscall` |
| `koma` | `ret` |
| `koma_tsarin` | `sysret` |
| `loda_adireshi` | `lea` |
| `loda_byte` | `lodsb` |
| `madauki` | `loop` |
| `madauki_idan_sifiri` | `loopz` |
| `maimaita` | `rep` |
| `motsa` | `mov` |
| `motsa_byte` | `movsb` |
| `musaya` | `xchg` |
| `raba` | `div` |
| `rage` | `sub` |
| `rage_daya` | `dec` |
| `rubanya` | `mul` |
| `tsallaka` | `jmp` |
| `tsayawa` | `int` |
| `tura` | `push` |
| `tura_tuta` | `pushf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hausa (ha)
section .text
global _start

_start:
    motsa rax, 1
    motsa rdi, 1
    motsa rsi, msg
    motsa rdx, 13
    kiran_tsarin

    motsa rax, 60
    motsa rdi, 0
    kiran_tsarin

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ha programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ha programa.masm
```
