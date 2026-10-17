# MultiLang-ASM: Manual de Instrucciones [DE]

**Idioma:** German / Deutsch (`de`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 44  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `addieren` | `add` |
| `bewegen` | `mov` |
| `byte_bewegen` | `movsb` |
| `byte_laden` | `lodsb` |
| `byte_speichern` | `stosb` |
| `byte_zu_wort` | `cbw` |
| `dekrementieren` | `dec` |
| `dividieren` | `div` |
| `dividieren_vorzeichen` | `idiv` |
| `doppel_zu_quad` | `cdq` |
| `druecken` | `push` |
| `effektiv_laden` | `lea` |
| `holen` | `pop` |
| `inkrementieren` | `inc` |
| `multiplizieren` | `mul` |
| `multiplizieren_vorzeichen` | `imul` |
| `negieren` | `neg` |
| `nichts` | `nop` |
| `null_erweitern` | `movzx` |
| `rufen` | `call` |
| `schleife` | `loop` |
| `schleife_wenn_null` | `loopz` |
| `springen` | `jmp` |
| `stapel_druecken` | `push` |
| `stapel_flags_druecken` | `pushf` |
| `stapel_flags_holen` | `popf` |
| `stapel_holen` | `pop` |
| `stoppen` | `hlt` |
| `subtrahieren` | `sub` |
| `system_rueckkehr` | `sysret` |
| `systemaufruf` | `syscall` |
| `tauschen` | `xchg` |
| `testen` | `test` |
| `unterbrechung` | `int` |
| `vergleichen` | `cmp` |
| `vorzeichen_erweitern` | `movsx` |
| `wenn_gleich` | `je` |
| `wenn_groesser` | `jg` |
| `wenn_kleiner` | `jl` |
| `wenn_nicht_gleich` | `jne` |
| `wenn_null` | `jz` |
| `wiederholen` | `rep` |
| `wort_zu_doppel` | `cwd` |
| `zurueckkehren` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en German / Deutsch (de)
section .text
global _start

_start:
    bewegen rax, 1
    bewegen rdi, 1
    bewegen rsi, msg
    bewegen rdx, 13
    systemaufruf

    bewegen rax, 60
    bewegen rdi, 0
    systemaufruf

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm de programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build de programa.masm
```
