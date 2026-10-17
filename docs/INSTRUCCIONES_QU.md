# MultiLang-ASM: Manual de Instrucciones [QU]

**Idioma:** Quechua / Runa Simi (`qu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `astay` | `mov` |
| `aswan_hatun` | `jg` |
| `aswan_uchuy` | `jl` |
| `byte_astay` | `movsb` |
| `byte_kargay` | `lodsb` |
| `byte_waqaychay` | `stosb` |
| `byte_wordman` | `cbw` |
| `chusaq_hina` | `jz` |
| `chusaq_mastariy` | `movzx` |
| `chusaq_muyuy` | `loopz` |
| `dir_kargay` | `lea` |
| `double_quadman` | `cdq` |
| `imapas_mana` | `nop` |
| `kaqlla_hina` | `je` |
| `kutimuy` | `ret` |
| `llanchiy` | `test` |
| `llanu_kutimuy` | `sysret` |
| `llanu_waqyay` | `syscall` |
| `mana_kaqlla` | `jne` |
| `mirachiy` | `mul` |
| `muyuy` | `loop` |
| `pampachay` | `neg` |
| `paway` | `jmp` |
| `pisiyachiy` | `dec` |
| `qichuy` | `sub` |
| `qurpuy` | `pop` |
| `rakiniy` | `div` |
| `samachiy` | `int` |
| `sayachiy` | `hlt` |
| `tikray` | `rep` |
| `trukay` | `xchg` |
| `tupachiy` | `cmp` |
| `unancha_mastariy` | `movsx` |
| `unancha_qurpuy` | `popf` |
| `unancha_winay` | `pushf` |
| `waqyay` | `call` |
| `winay` | `push` |
| `wiñachiy` | `inc` |
| `word_doubleman` | `cwd` |
| `yapay` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Quechua / Runa Simi (qu)
section .text
global _start

_start:
    astay rax, 1
    astay rdi, 1
    astay rsi, msg
    astay rdx, 13
    llanu_waqyay

    astay rax, 60
    astay rdi, 0
    llanu_waqyay

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm qu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build qu programa.masm
```
