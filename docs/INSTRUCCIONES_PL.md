# MultiLang-ASM: Manual de Instrucciones [PL]

**Idioma:** Polish / Polski (`pl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 43  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `albo` | `xor` |
| `bajt_na_slowo` | `cbw` |
| `dodaj` | `add` |
| `i` | `and` |
| `jesli_mniejsze` | `jl` |
| `jesli_nierowne` | `jne` |
| `jesli_rowne` | `je` |
| `jesli_wieksze` | `jg` |
| `jesli_zero` | `jz` |
| `laduj_bajt` | `lodsb` |
| `lub` | `or` |
| `nic` | `nop` |
| `odejmij` | `sub` |
| `oraz` | `and` |
| `petla` | `loop` |
| `petla_jesli_zero` | `loopz` |
| `podziel` | `div` |
| `poloz` | `push` |
| `poloz_flagi` | `pushf` |
| `pomnoz` | `mul` |
| `porownaj` | `cmp` |
| `powrot_systemowy` | `sysret` |
| `powtarzaj` | `rep` |
| `przenies` | `mov` |
| `przenies_bajt` | `movsb` |
| `przerwanie` | `int` |
| `przesun` | `mov` |
| `przesuń` | `mov` |
| `skocz` | `jmp` |
| `slowo_na_podwojne` | `cwd` |
| `stop` | `hlt` |
| `testuj` | `test` |
| `wolaj` | `call` |
| `wroc` | `ret` |
| `wywolanie_systemowe` | `syscall` |
| `zaladuj_adres` | `lea` |
| `zamien` | `xchg` |
| `zaneguj` | `neg` |
| `zapisz_bajt` | `stosb` |
| `zdejmij` | `pop` |
| `zdejmij_flagi` | `popf` |
| `zmniejsz` | `dec` |
| `zwieksz` | `inc` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Polish / Polski (pl)
section .text
global _start

_start:
    przenies rax, 1
    przenies rdi, 1
    przenies rsi, msg
    przenies rdx, 13
    wywolanie_systemowe

    przenies rax, 60
    przenies rdi, 0
    wywolanie_systemowe

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm pl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build pl programa.masm
```
