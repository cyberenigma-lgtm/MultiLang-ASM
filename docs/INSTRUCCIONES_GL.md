# MultiLang-ASM: Manual de Instrucciones [GL]

**Idioma:** Galician / Galego (`gl`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `almacenar_byte` | `stosb` |
| `bucle` | `loop` |
| `bucle_se_cero` | `loopz` |
| `byte_a_palabra` | `cbw` |
| `cargar_byte` | `lodsb` |
| `cargar_efectiva` | `lea` |
| `chamada_sistema` | `syscall` |
| `chamar` | `call` |
| `comparar` | `cmp` |
| `decrementar` | `dec` |
| `deter` | `hlt` |
| `dividir` | `div` |
| `dobre_a_quad` | `cdq` |
| `estender_cero` | `movzx` |
| `estender_signo` | `movsx` |
| `incrementar` | `inc` |
| `intercambiar` | `xchg` |
| `interrupción` | `int` |
| `meter` | `push` |
| `meter_bandeiras` | `pushf` |
| `mover` | `mov` |
| `mover_byte` | `movsb` |
| `multiplicar` | `mul` |
| `nada` | `nop` |
| `negar` | `neg` |
| `palabra_a_dobre` | `cwd` |
| `probar` | `test` |
| `repetir` | `rep` |
| `restar` | `sub` |
| `retornar` | `ret` |
| `retorno_sistema` | `sysret` |
| `sacar` | `pop` |
| `sacar_bandeiras` | `popf` |
| `saltar` | `jmp` |
| `se_cero` | `jz` |
| `se_igual` | `je` |
| `se_maior` | `jg` |
| `se_menor` | `jl` |
| `se_non_igual` | `jne` |
| `sumar` | `add` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Galician / Galego (gl)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    chamada_sistema

    mover rax, 60
    mover rdi, 0
    chamada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm gl programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build gl programa.masm
```
