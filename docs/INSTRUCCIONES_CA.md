# MultiLang-ASM: Manual de Instrucciones [CA]

**Idioma:** Catalan / Català (`ca`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `aturar` | `hlt` |
| `bucle` | `loop` |
| `bucle_si_zero` | `loopz` |
| `byte_a_paraula` | `cbw` |
| `carregar_byte` | `lodsb` |
| `carregar_efectiva` | `lea` |
| `comparar` | `cmp` |
| `crida_sistema` | `syscall` |
| `cridar` | `call` |
| `decrementar` | `dec` |
| `dividir` | `div` |
| `doble_a_quad` | `cdq` |
| `emmagatzemar_byte` | `stosb` |
| `empènyer` | `push` |
| `empènyer_banderes` | `pushf` |
| `estendre_signe` | `movsx` |
| `estendre_zero` | `movzx` |
| `extreure` | `pop` |
| `extreure_banderes` | `popf` |
| `incrementar` | `inc` |
| `intercanviar` | `xchg` |
| `interrupció` | `int` |
| `moure` | `mov` |
| `moure_byte` | `movsb` |
| `multiplicar` | `mul` |
| `negar` | `neg` |
| `paraula_a_doble` | `cwd` |
| `repetir` | `rep` |
| `res` | `nop` |
| `restar` | `sub` |
| `retorn_sistema` | `sysret` |
| `retornar` | `ret` |
| `saltar` | `jmp` |
| `si_igual` | `je` |
| `si_major` | `jg` |
| `si_menor` | `jl` |
| `si_no_igual` | `jne` |
| `si_zero` | `jz` |
| `sumar` | `add` |
| `testar` | `test` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Catalan / Català (ca)
section .text
global _start

_start:
    moure rax, 1
    moure rdi, 1
    moure rsi, msg
    moure rdx, 13
    crida_sistema

    moure rax, 60
    moure rdi, 0
    crida_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ca programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ca programa.masm
```
