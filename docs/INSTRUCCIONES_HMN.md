# MultiLang-ASM: Manual de Instrucciones [HMN]

**Idioma:** Hmong / Hmoob (`hmn`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `dhia` | `jmp` |
| `faib` | `div` |
| `hu` | `call` |
| `hu_kab_ke` | `syscall` |
| `kuaj` | `test` |
| `lossis` | `or` |
| `muab_ntau` | `mul` |
| `nres` | `hlt` |
| `ntxiv` | `add` |
| `pab_phev` | `cmp` |
| `rho` | `sub` |
| `rov_qab` | `ret` |
| `rub_tawm` | `pop` |
| `thawb` | `push` |
| `thiab` | `and` |
| `tshwj_xeeb` | `xor` |
| `tsis` | `not` |
| `tsis_muaj_dabtsi` | `nop` |
| `tsiv` | `mov` |
| `tขwv_tshav` | `int` |
| `voj_kuj` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Hmong / Hmoob (hmn)
section .text
global _start

_start:
    tsiv rax, 1
    tsiv rdi, 1
    tsiv rsi, msg
    tsiv rdx, 13
    hu_kab_ke

    tsiv rax, 60
    tsiv rdi, 0
    hu_kab_ke

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm hmn programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build hmn programa.masm
```
