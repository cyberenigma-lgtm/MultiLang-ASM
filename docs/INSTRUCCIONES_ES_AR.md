# MultiLang-ASM: Manual de Instrucciones [ES_AR]

**Idioma:** Spanish (Argentina) / Español (Argentina) (`es_ar`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 42  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `atencion` | `int` |
| `aumentar` | `inc` |
| `aviso_sistema` | `syscall` |
| `bajar` | `dec` |
| `cargar` | `mov` |
| `cargar_byte` | `lodsb` |
| `chau_sistema` | `sysret` |
| `che_byte_a_word` | `cbw` |
| `chequear` | `test` |
| `comparar` | `cmp` |
| `copiar` | `mov` |
| `cortar` | `hlt` |
| `dividir` | `div` |
| `empujar` | `push` |
| `guardar_byte` | `stosb` |
| `intercambiar` | `xchg` |
| `llamar` | `call` |
| `mandar` | `mov` |
| `mandar_flags` | `pushf` |
| `mover` | `mov` |
| `mover_byte` | `movsb` |
| `multiplicar` | `mul` |
| `nada` | `nop` |
| `no` | `not` |
| `o` | `or` |
| `pasar` | `mov` |
| `repetir` | `rep` |
| `restar` | `sub` |
| `sacar` | `pop` |
| `saltar` | `jmp` |
| `si_es_cero` | `jz` |
| `si_es_distinto` | `jne` |
| `si_es_igual` | `je` |
| `si_es_mayor` | `jg` |
| `si_es_menor` | `jl` |
| `sumar` | `add` |
| `traer_flags` | `popf` |
| `volver` | `ret` |
| `vuelta` | `loop` |
| `vuelta_si_cero` | `loopz` |
| `word_a_doble` | `cwd` |
| `y` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Spanish (Argentina) / Español (Argentina) (es_ar)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    aviso_sistema

    mover rax, 60
    mover rdi, 0
    aviso_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm es_ar programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build es_ar programa.masm
```
