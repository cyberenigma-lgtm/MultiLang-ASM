# MultiLang-ASM: Manual de Instrucciones [RU]

**Idioma:** Russian / Русский (`ru`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 42  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `байт_в_слово` | `cbw` |
| `вернуться` | `ret` |
| `возврат_системы` | `sysret` |
| `вызвать` | `call` |
| `вычесть` | `sub` |
| `двойное_в_квадро` | `cdq` |
| `если_больше` | `jg` |
| `если_меньше` | `jl` |
| `если_не_равно` | `jne` |
| `если_ноль` | `jz` |
| `если_равно` | `je` |
| `загрузить_байт` | `lodsb` |
| `загрузить_эффективный` | `lea` |
| `извлечь` | `pop` |
| `извлечь_флаги` | `popf` |
| `обменять` | `xchg` |
| `остановка` | `hlt` |
| `отнять` | `sub` |
| `отрицание` | `neg` |
| `перенести` | `mov` |
| `перенести_байт` | `movsb` |
| `повторить` | `rep` |
| `положить` | `push` |
| `положить_флаги` | `pushf` |
| `прерывание` | `int` |
| `прибавить` | `add` |
| `проверить` | `test` |
| `прыгнуть` | `jmp` |
| `пусто` | `nop` |
| `разделить` | `div` |
| `расширить_знаком` | `movsx` |
| `расширить_нулями` | `movzx` |
| `системный_вызов` | `syscall` |
| `слово_в_двойное` | `cwd` |
| `сложить` | `add` |
| `сохранить_байт` | `stosb` |
| `сравнить` | `cmp` |
| `увеличить` | `inc` |
| `уменьшить` | `dec` |
| `умножить` | `mul` |
| `цикл` | `loop` |
| `цикл_если_ноль` | `loopz` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Russian / Русский (ru)
section .text
global _start

_start:
    перенести rax, 1
    перенести rdi, 1
    перенести rsi, msg
    перенести rdx, 13
    системный_вызов

    перенести rax, 60
    перенести rdi, 0
    системный_вызов

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ru programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ru programa.masm
```
