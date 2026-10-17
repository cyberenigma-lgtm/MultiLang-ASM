# MultiLang-ASM: Manual de Instrucciones [FR]

**Idioma:** French / Français (`fr`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 56  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ajouter` | `add` |
| `appel_systeme` | `syscall` |
| `appeler` | `call` |
| `arreter` | `hlt` |
| `boucle` | `loop` |
| `boucle_si_zero` | `loopz` |
| `charger_effectif` | `lea` |
| `charger_octet` | `lodsb` |
| `comparer` | `cmp` |
| `conv_mot_double` | `cwd` |
| `conv_octet_mot` | `cbw` |
| `copier` | `mov` |
| `decaler_arith_droite` | `sar` |
| `decaler_arith_gauche` | `sal` |
| `decaler_droite` | `shr` |
| `decaler_gauche` | `shl` |
| `decrementer` | `dec` |
| `depiler` | `pop` |
| `deplacer` | `mov` |
| `deplacer_octet` | `movsb` |
| `diviser` | `div` |
| `diviser_signe` | `idiv` |
| `echanger` | `xchg` |
| `empiler` | `push` |
| `et` | `and` |
| `etendre_signe` | `movsx` |
| `etendre_zero` | `movzx` |
| `incrementer` | `inc` |
| `interruption` | `int` |
| `multiplier` | `mul` |
| `multiplier_signe` | `imul` |
| `negativer` | `neg` |
| `non` | `not` |
| `ou` | `or` |
| `ou_exclusif` | `xor` |
| `pousser_drapeaux` | `pushf` |
| `repeter` | `rep` |
| `retour_interruption` | `iret` |
| `retour_systeme` | `sysret` |
| `retourner` | `ret` |
| `rien` | `nop` |
| `rot_droite` | `ror` |
| `rot_gauche` | `rol` |
| `sauter` | `jmp` |
| `si_egal` | `je` |
| `si_pas_egal` | `jne` |
| `si_pas_zero` | `jnz` |
| `si_plus_grand` | `jg` |
| `si_plus_grand_egal` | `jge` |
| `si_plus_petit` | `jl` |
| `si_plus_petit_egal` | `jle` |
| `si_zero` | `jz` |
| `soustraire` | `sub` |
| `stocker_octet` | `stosb` |
| `tester` | `test` |
| `tirer_drapeaux` | `popf` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en French / Français (fr)
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
mlasm fr programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build fr programa.masm
```
