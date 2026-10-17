# MultiLang-ASM: Manual de Instrucciones [FR_BE]

**Idioma:** Belgian French / Français (Belgique) (`fr_be`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ajouter` | `add` |
| `appel_systeme` | `syscall` |
| `appeler` | `call` |
| `bouger_octet` | `movsb` |
| `charger_adresse` | `lea` |
| `charger_octet` | `lodsb` |
| `comparer` | `cmp` |
| `copier` | `mov` |
| `deplacer` | `mov` |
| `diviser` | `div` |
| `encore` | `rep` |
| `et` | `and` |
| `interrompre` | `int` |
| `moins_un` | `dec` |
| `mot_en_double` | `cwd` |
| `multiplier` | `mul` |
| `non` | `not` |
| `octet_en_mot` | `cbw` |
| `ou` | `or` |
| `plus_un` | `inc` |
| `pousser` | `push` |
| `pousser_flags` | `pushf` |
| `retour_systeme` | `sysret` |
| `revenir` | `ret` |
| `rien` | `nop` |
| `sauter` | `jmp` |
| `septante` | `mov` |
| `si_egal` | `je` |
| `si_pas_egal` | `jne` |
| `si_plus_grand` | `jg` |
| `si_plus_petit` | `jl` |
| `si_zero` | `jz` |
| `si_zero_tourner` | `loopz` |
| `soustraire` | `sub` |
| `stocker_octet` | `stosb` |
| `stop` | `hlt` |
| `tester` | `test` |
| `tirer` | `pop` |
| `tirer_flags` | `popf` |
| `tourner` | `loop` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Belgian French / Français (Belgique) (fr_be)
section .text
global _start

_start:
    deplacer rax, 1
    deplacer rdi, 1
    deplacer rsi, msg
    deplacer rdx, 13
    appel_systeme

    deplacer rax, 60
    deplacer rdi, 0
    appel_systeme

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm fr_be programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fr_be programa.masm
```
