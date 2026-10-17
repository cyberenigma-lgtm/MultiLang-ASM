# MultiLang-ASM: Manual de Instrucciones [VE]

**Idioma:** Venda / Tshivenḓa (`ve`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `a_huna_tshithu` | `nop` |
| `andisa` | `mul` |
| `bvisa` | `pop` |
| `dhengedza` | `push` |
| `engedza` | `add` |
| `fhufha` | `jmp` |
| `hai` | `not` |
| `ima` | `hlt` |
| `kana` | `or` |
| `kovha` | `div` |
| `lingedza` | `test` |
| `mutingo` | `loop` |
| `na` | `and` |
| `sudzusa` | `mov` |
| `thithiso` | `int` |
| `tshiphiri` | `xor` |
| `tusa` | `sub` |
| `uvhidza_sisitemu` | `syscall` |
| `vhambedza` | `cmp` |
| `vhidza` | `call` |
| `vhuyelela` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Venda / Tshivenḓa (ve)
section .text
global _start

_start:
    sudzusa rax, 1
    sudzusa rdi, 1
    sudzusa rsi, msg
    sudzusa rdx, 13
    uvhidza_sisitemu

    sudzusa rax, 60
    sudzusa rdi, 0
    uvhidza_sisitemu

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ve programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ve programa.masm
```
