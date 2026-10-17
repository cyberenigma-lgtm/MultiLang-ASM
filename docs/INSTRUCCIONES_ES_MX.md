# MultiLang-ASM: Manual de Instrucciones [ES_MX]

**Idioma:** Spanish (Mexico) / Español (México) (`es_mx`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 50  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `alto` | `hlt` |
| `añadir` | `add` |
| `cargar` | `mov` |
| `cargar_byte` | `lodsb` |
| `cargar_dirección` | `lea` |
| `ciclo` | `loop` |
| `ciclo_si_cero` | `loopz` |
| `comparar` | `cmp` |
| `conv_byte_palabra` | `cbw` |
| `conv_palabra_doble` | `cwd` |
| `copiar` | `mov` |
| `decrementar` | `dec` |
| `desplazar_der` | `shr` |
| `desplazar_izq` | `shl` |
| `dividir` | `div` |
| `dividir_signado` | `idiv` |
| `exclusivo` | `xor` |
| `extender_cero` | `movzx` |
| `extender_signo` | `movsx` |
| `guardar_byte` | `stosb` |
| `incrementar` | `inc` |
| `intercambiar` | `xchg` |
| `interrupcion` | `int` |
| `llamada_sistema` | `syscall` |
| `meter` | `push` |
| `meter_flags` | `pushf` |
| `mover` | `mov` |
| `mover_byte` | `movsb` |
| `multiplicar` | `mul` |
| `multiplicar_signado` | `imul` |
| `nadamás` | `nop` |
| `negar` | `neg` |
| `no` | `not` |
| `o` | `or` |
| `probar` | `test` |
| `pueblos` | `call` |
| `regresar` | `ret` |
| `regreso_sistema` | `sysret` |
| `repetir` | `rep` |
| `restar` | `sub` |
| `sacar` | `pop` |
| `sacar_flags` | `popf` |
| `saltar` | `jmp` |
| `si_cero` | `jz` |
| `si_igual` | `je` |
| `si_mayor` | `jg` |
| `si_menor` | `jl` |
| `si_no_igual` | `jne` |
| `sumar` | `add` |
| `y` | `and` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Spanish (Mexico) / Español (México) (es_mx)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    llamada_sistema

    mover rax, 60
    mover rdi, 0
    llamada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm es_mx programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build es_mx programa.masm
```
