# MultiLang-ASM: Manual de Instrucciones [TR]

**Idioma:** Turkish / Türkçe (`tr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 44  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `adresi_yukle` | `lea` |
| `arttir` | `inc` |
| `atla` | `jmp` |
| `azalt` | `dec` |
| `bayraklari_cek` | `popf` |
| `bayraklari_it` | `pushf` |
| `bayt_sakla` | `stosb` |
| `bayt_tasi` | `movsb` |
| `bayt_to_word` | `cbw` |
| `bayt_yukle` | `lodsb` |
| `bol` | `div` |
| `bos` | `nop` |
| `buyukse` | `jg` |
| `cagir` | `call` |
| `carp` | `mul` |
| `cek` | `pop` |
| `cikar` | `sub` |
| `degil` | `not` |
| `degille` | `neg` |
| `degistir` | `xchg` |
| `don` | `ret` |
| `dongu` | `loop` |
| `dur` | `hlt` |
| `ekle` | `add` |
| `esit_degilse` | `jne` |
| `esitse` | `je` |
| `it` | `push` |
| `karsilastir` | `cmp` |
| `kesme` | `int` |
| `kucukse` | `jl` |
| `ozel_veya` | `xor` |
| `sifirsa` | `jz` |
| `sifirsa_dongu` | `loopz` |
| `sistem_cagrisi` | `syscall` |
| `sistem_donusu` | `sysret` |
| `tasi` | `mov` |
| `taşı` | `mov` |
| `tekrarla` | `rep` |
| `test_et` | `test` |
| `topla` | `add` |
| `ve` | `and` |
| `veya` | `or` |
| `word_to_double` | `cwd` |
| `özel_veya` | `xor` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Turkish / Türkçe (tr)
section .text
global _start

_start:
    tasi rax, 1
    tasi rdi, 1
    tasi rsi, msg
    tasi rdx, 13
    sistem_cagrisi

    tasi rax, 60
    tasi rdi, 0
    sistem_cagrisi

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm tr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build tr programa.masm
```
