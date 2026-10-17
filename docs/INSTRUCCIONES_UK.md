# MultiLang-ASM: Manual de Instrucciones [UK]

**Idioma:** Ukrainian / Українська (`uk`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `байт_у_слово` | `cbw` |
| `викликати` | `call` |
| `витягти` | `pop` |
| `витягти_прапорці` | `popf` |
| `відняти` | `sub` |
| `додати` | `add` |
| `завантажити_байт` | `lodsb` |
| `завантажити_ефективну` | `lea` |
| `заперечити` | `neg` |
| `зберегти_байт` | `stosb` |
| `збільшити` | `inc` |
| `зменшити` | `dec` |
| `зупинити` | `hlt` |
| `нічого` | `nop` |
| `обміняти` | `xchg` |
| `перенести` | `mov` |
| `перенести_байт` | `movsb` |
| `переривання` | `int` |
| `повернутися` | `ret` |
| `повторити` | `rep` |
| `подвійне_у_квадро` | `cdq` |
| `поділити` | `div` |
| `покласти` | `push` |
| `покласти_прапорці` | `pushf` |
| `помножити` | `mul` |
| `порівняти` | `cmp` |
| `розширити_знаком` | `movsx` |
| `розширити_нулем` | `movzx` |
| `системне_повернення` | `sysret` |
| `системний_виклик` | `syscall` |
| `слово_у_подвійне` | `cwd` |
| `стрибнути` | `jmp` |
| `тестувати` | `test` |
| `цикл` | `loop` |
| `цикл_якщо_нуль` | `loopz` |
| `якщо_більше` | `jg` |
| `якщо_менше` | `jl` |
| `якщо_не_рівно` | `jne` |
| `якщо_нуль` | `jz` |
| `якщо_рівно` | `je` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Ukrainian / Українська (uk)
section .text
global _start

_start:
    перенести rax, 1
    перенести rdi, 1
    перенести rsi, msg
    перенести rdx, 13
    системний_виклик

    перенести rax, 60
    перенести rdi, 0
    системний_виклик

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm uk programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build uk programa.masm
```
