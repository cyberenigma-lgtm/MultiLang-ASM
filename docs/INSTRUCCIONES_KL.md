# MultiLang-ASM: Manual de Instrucciones [KL]

**Idioma:** Greenlandic / Kalaallisut (`kl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aamma` | `and` |
| `akornusersorpaa` | `int` |
| `amerlisarpaa` | `mul` |
| `atortup_qaaqqussutaa` | `syscall` |
| `aveqqippaa` | `div` |
| `ilannguppaa` | `add` |
| `imaluunniit` | `or` |
| `immikkut` | `xor` |
| `kaaviiaartoq` | `loop` |
| `manguppaa` | `push` |
| `misilippaa` | `test` |
| `naagga` | `not` |
| `nalilersorpaa` | `cmp` |
| `nussorpaa` | `mov` |
| `nussorpaa_ane` | `pop` |
| `peerpaa` | `sub` |
| `pissippoq` | `jmp` |
| `soqanngilaq` | `nop` |
| `torluppaa` | `call` |
| `unitsiguk` | `hlt` |
| `uteqqippoq` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Greenlandic / Kalaallisut (kl)
section .text
global _start

_start:
    nussorpaa rax, 1
    nussorpaa rdi, 1
    nussorpaa rsi, msg
    nussorpaa rdx, 13
    atortup_qaaqqussutaa

    nussorpaa rax, 60
    nussorpaa rdi, 0
    atortup_qaaqqussutaa

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm kl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build kl programa.masm
```
