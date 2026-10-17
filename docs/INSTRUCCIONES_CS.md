# MultiLang-ASM: Manual de Instrucciones [CS]

**Idioma:** Czech / Čeština (`cs`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 26  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `a` | `and` |
| `cyklus` | `loop` |
| `delit` | `div` |
| `exkluzivni` | `xor` |
| `nasobit` | `mul` |
| `ne` | `not` |
| `nebo` | `or` |
| `nic` | `nop` |
| `odecist` | `sub` |
| `otestovat` | `test` |
| `pokud_nerovno` | `jne` |
| `pokud_rovno` | `je` |
| `porovnat` | `cmp` |
| `preruseni` | `int` |
| `presunout` | `mov` |
| `pridat` | `add` |
| `skocit` | `jmp` |
| `snizit` | `dec` |
| `systemove_volani` | `syscall` |
| `vlozit` | `push` |
| `vratit` | `ret` |
| `vyjmout` | `pop` |
| `vymenit` | `xchg` |
| `zastavit` | `hlt` |
| `zavolat` | `call` |
| `zvysit` | `inc` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Czech / Čeština (cs)
section .text
global _start

_start:
    presunout rax, 1
    presunout rdi, 1
    presunout rsi, msg
    presunout rdx, 13
    systemove_volani

    presunout rax, 60
    presunout rdi, 0
    systemove_volani

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm cs programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build cs programa.masm
```
