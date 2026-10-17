# MultiLang-ASM: Manual de Instrucciones [ES]

**Idioma:** Spanish / Español (`es`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 227  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `activar_acarreo` | `stc` |
| `activar_interrupciones` | `sti` |
| `agregar` | `add` |
| `ajuste_ascii_division` | `aad` |
| `ajuste_ascii_multiplicacion` | `aam` |
| `ajuste_ascii_resta` | `aas` |
| `ajuste_ascii_suma` | `aaa` |
| `ajuste_decimal_resta` | `das` |
| `ajuste_decimal_suma` | `daa` |
| `almacenar_ah_en_banderas` | `sahf` |
| `almacenar_byte` | `stosb` |
| `almacenar_cuadruple` | `stosq` |
| `almacenar_doble` | `stosd` |
| `almacenar_gdt` | `sgdt` |
| `almacenar_idt` | `sidt` |
| `almacenar_ldt` | `sldt` |
| `almacenar_palabra` | `stosw` |
| `almacenar_tr` | `str` |
| `añadir` | `add` |
| `barrera_almacenamiento` | `sfence` |
| `barrera_carga` | `lfence` |
| `barrera_memoria` | `mfence` |
| `cargar` | `mov` |
| `cargar_ah_desde_banderas` | `lahf` |
| `cargar_byte` | `lodsb` |
| `cargar_cuadruple` | `lodsq` |
| `cargar_doble` | `lodsd` |
| `cargar_efectivo` | `lea` |
| `cargar_gdt` | `lgdt` |
| `cargar_idt` | `lidt` |
| `cargar_ldt` | `lldt` |
| `cargar_palabra` | `lodsw` |
| `cargar_tr` | `ltr` |
| `ciclo` | `loop` |
| `ciclo_si_cero` | `loopz` |
| `ciclo_si_igual` | `loope` |
| `ciclo_si_no_cero` | `loopnz` |
| `ciclo_si_no_igual` | `loopne` |
| `comparar` | `cmp` |
| `comparar_bytes` | `cmpsb` |
| `comparar_cuadruples` | `cmpsq` |
| `comparar_dobles` | `cmpsd` |
| `comparar_palabras` | `cmpsw` |
| `complementar_acarreo` | `cmc` |
| `contar_ceros_cola` | `tzcnt` |
| `contar_ceros_lideres` | `lzcnt` |
| `contar_unos` | `popcnt` |
| `convertir_byte_palabra` | `cbw` |
| `convertir_cuadruple_octo` | `cqo` |
| `convertir_doble_cuadruple` | `cdq` |
| `convertir_doble_cuadruple_ext` | `cdqe` |
| `convertir_palabra_doble` | `cwd` |
| `convertir_palabra_doble_ext` | `cwde` |
| `copiar` | `mov` |
| `decrementar` | `dec` |
| `desplazar_arit_der` | `sar` |
| `desplazar_arit_izq` | `sal` |
| `desplazar_der` | `shr` |
| `desplazar_doble_der` | `shrd` |
| `desplazar_doble_izq` | `shld` |
| `desplazar_izq` | `shl` |
| `detener` | `hlt` |
| `dividir` | `div` |
| `dividir_signado` | `idiv` |
| `entrada_puerto` | `in` |
| `entrada_puerto_byte` | `insb` |
| `entrada_puerto_doble` | `insd` |
| `entrada_puerto_palabra` | `insw` |
| `entrar` | `enter` |
| `entrar_sistema` | `sysenter` |
| `escanear_bit_adelante` | `bsf` |
| `escanear_bit_atras` | `bsr` |
| `escanear_byte` | `scasb` |
| `escanear_cuadruple` | `scasq` |
| `escanear_doble` | `scasd` |
| `escanear_palabra` | `scasw` |
| `escribir_e_invalidar_cache` | `wbinvd` |
| `escribir_msr` | `wrmsr` |
| `esperar` | `wait` |
| `exclusivo` | `xor` |
| `extender_cero` | `movzx` |
| `extender_signo` | `movsx` |
| `fijar_bit` | `bts` |
| `fijar_direccion` | `std` |
| `fijar_si_abajo` | `setb` |
| `fijar_si_abajo_igual` | `setbe` |
| `fijar_si_acarreo` | `setc` |
| `fijar_si_arriba` | `seta` |
| `fijar_si_arriba_igual` | `setae` |
| `fijar_si_cero` | `setz` |
| `fijar_si_desborde` | `seto` |
| `fijar_si_igual` | `sete` |
| `fijar_si_mayor` | `setg` |
| `fijar_si_mayor_igual` | `setge` |
| `fijar_si_menor` | `setl` |
| `fijar_si_menor_igual` | `setle` |
| `fijar_si_no_acarreo` | `setnc` |
| `fijar_si_no_cero` | `setnz` |
| `fijar_si_no_desborde` | `setno` |
| `fijar_si_no_igual` | `setne` |
| `fijar_si_no_signo` | `setns` |
| `fijar_si_paridad` | `setp` |
| `fijar_si_signo` | `sets` |
| `fpu_absoluto` | `fabs` |
| `fpu_almacenar` | `fst` |
| `fpu_cambiar_signo` | `fchs` |
| `fpu_cargar` | `fld` |
| `fpu_coseno` | `fcos` |
| `fpu_dividir` | `fdiv` |
| `fpu_inicializar` | `finit` |
| `fpu_limpiar_excepciones` | `fclex` |
| `fpu_multiplicar` | `fmul` |
| `fpu_nada` | `fnop` |
| `fpu_raiz` | `fsqrt` |
| `fpu_restar` | `fsub` |
| `fpu_sacar` | `fstp` |
| `fpu_seno` | `fsin` |
| `fpu_sumar` | `fadd` |
| `identificar_cpu` | `cpuid` |
| `incrementar` | `inc` |
| `intercambiar` | `xchg` |
| `intercambiar_bytes` | `bswap` |
| `intercambiar_sumar` | `xadd` |
| `interrupcion` | `int` |
| `interrupcion_desborde` | `into` |
| `invalidar_cache` | `invd` |
| `invertir_bit` | `btc` |
| `leer_contador_tiempo` | `rdtsc` |
| `leer_contador_tiempo_p` | `rdtscp` |
| `leer_msr` | `rdmsr` |
| `limpiar_acarreo` | `clc` |
| `limpiar_cache` | `clflush` |
| `limpiar_direccion` | `cld` |
| `limpiar_interrupciones` | `cli` |
| `llamada_sistema` | `syscall` |
| `llamar` | `call` |
| `meter` | `push` |
| `meter_banderas` | `pushf` |
| `meter_banderas_q` | `pushfq` |
| `meter_todo` | `pusha` |
| `mover` | `mov` |
| `mover_byte` | `movsb` |
| `mover_cuadruple` | `movsq` |
| `mover_doble` | `movsd` |
| `mover_endian` | `movbe` |
| `mover_palabra` | `movsw` |
| `mover_si_abajo` | `cmovb` |
| `mover_si_abajo_igual` | `cmovbe` |
| `mover_si_arriba` | `cmova` |
| `mover_si_arriba_igual` | `cmovae` |
| `mover_si_cero` | `cmovz` |
| `mover_si_desborde` | `cmovo` |
| `mover_si_igual` | `cmove` |
| `mover_si_mayor` | `cmovg` |
| `mover_si_mayor_igual` | `cmovge` |
| `mover_si_menor` | `cmovl` |
| `mover_si_menor_igual` | `cmovle` |
| `mover_si_no_cero` | `cmovnz` |
| `mover_si_no_desborde` | `cmovno` |
| `mover_si_no_igual` | `cmovne` |
| `mover_si_no_signo` | `cmovns` |
| `mover_si_signo` | `cmovs` |
| `multiplicar` | `mul` |
| `multiplicar_signado` | `imul` |
| `nada` | `nop` |
| `negar` | `neg` |
| `no` | `not` |
| `o` | `or` |
| `pausa` | `pause` |
| `probar` | `test` |
| `probar_bit` | `bt` |
| `punto_interrupcion` | `int3` |
| `repetir` | `rep` |
| `repetir_mientras` | `repne` |
| `repetir_si_cero` | `repz` |
| `repetir_si_igual` | `repe` |
| `repetir_si_no_cero` | `repnz` |
| `restablecer_bit` | `btr` |
| `restar` | `sub` |
| `restar_con_prestamo` | `sbb` |
| `resumir_modo_sistema` | `rsm` |
| `retornar` | `ret` |
| `retorno_interrupcion` | `iret` |
| `retorno_interrupcion_doble` | `iretd` |
| `retorno_interrupcion_q` | `iretq` |
| `retorno_sistema` | `sysret` |
| `rotar_con_acarreo_der` | `rcr` |
| `rotar_con_acarreo_izq` | `rcl` |
| `rotar_der` | `ror` |
| `rotar_izq` | `rol` |
| `sacar` | `pop` |
| `sacar_banderas` | `popf` |
| `sacar_banderas_q` | `popfq` |
| `sacar_todo` | `popa` |
| `salida_puerto` | `out` |
| `salida_puerto_byte` | `outsb` |
| `salida_puerto_doble` | `outsd` |
| `salida_puerto_palabra` | `outsw` |
| `salir` | `leave` |
| `salir_sistema` | `sysexit` |
| `saltar` | `jmp` |
| `saltar_si_cx_cero` | `jcxz` |
| `saltar_si_ecx_cero` | `jecxz` |
| `saltar_si_rcx_cero` | `jrcxz` |
| `si_abajo` | `jb` |
| `si_abajo_igual` | `jbe` |
| `si_arriba` | `ja` |
| `si_arriba_igual` | `jae` |
| `si_cero` | `jz` |
| `si_desborde` | `jo` |
| `si_igual` | `je` |
| `si_mayor` | `jg` |
| `si_mayor_igual` | `jge` |
| `si_menor` | `jl` |
| `si_menor_igual` | `jle` |
| `si_no_cero` | `jnz` |
| `si_no_desborde` | `jno` |
| `si_no_igual` | `jne` |
| `si_no_paridad` | `jnp` |
| `si_no_signo` | `jns` |
| `si_paridad` | `jp` |
| `si_signo` | `js` |
| `sumar` | `add` |
| `sumar_con_acarreo` | `adc` |
| `volver` | `ret` |
| `y` | `and` |
| `y_negada` | `andn` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Spanish / Español (es)
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
mlasm es programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build es programa.masm
```
