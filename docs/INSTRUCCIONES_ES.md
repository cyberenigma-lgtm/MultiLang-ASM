# 📚 Referencia Completa de Instrucciones — Español (MultiLang-ASM)

Esta guía recoge todas las instrucciones soportadas en Español para el ensamblador multilingüe **MultiLang-ASM**, parte del ecosistema **Neuro-OS.es**.

> MultiLang-ASM permite escribir código ensamblador en tu idioma nativo y generar ASM estándar compatible con NASM/FASM/GAS.

---

## 🎨 Diseño del Lenguaje en Español

El diseño de las instrucciones en español de MultiLang-ASM sigue principios específicos:

### Filosofía de Diseño

**1. Naturalidad sobre Literalidad**
- No traducimos palabra por palabra del inglés
- Usamos términos que sean naturales para un hispanohablante
- Ejemplo: `saltar` suena más natural que `brincar` o `jumpar`

**2. Claridad sobre Brevedad**
- Preferimos `comparar` sobre `comp` porque es más claro
- Las abreviaturas están disponibles pero no son obligatorias
- El programador elige: `mover` o `mov` - ambos funcionan

**3. Consistencia Lingüística**
- Usamos infinitivos verbales: `sumar`, `restar`, `comparar`
- Mantenemos coherencia en familias de instrucciones
- Los nombres son predecibles: si existe `sumar`, existe `restar`

**4. Compatibilidad Universal**
- **Todas las instrucciones en inglés siguen funcionando**
- Puedes mezclar: `mover rax, rbx` y `push rcx` en el mismo código
- El ensamblador es agnóstico: traduce lo que necesita, ignora lo que ya es estándar

**5. Alias Múltiples**
- `mover` = `mov` = `copiar`
- `retornar` = `ret` = `volver`
- Esto permite estilos de código personalizados

### ¿Por Qué No es Solo "Traducción"?

Esto no es un diccionario inglés-español aplicado ciegamente. Es **diseño de lenguaje** pensado para:
- Que suene natural al leerlo en voz alta
- Que sea intuitivo para alguien que nunca vio ASM
- Que respete las convenciones de la CPU sin crear confusión

**Ejemplo:**
```asm
; Versión natural en español
mover rax, 10
comparar rax, 5
si_mayor etiqueta_positivo
saltar fin

; Versión mixta (igualmente válida)
mov rax, 10
comparar rax, 5
jg etiqueta_positivo
jmp fin
```

Ambas son correctas. El programador elige su estilo.

---

## 📦 Movimiento de Datos

| Español | ASM | Descripción |
|---------|-----|-------------|
| `mover`, `copiar` | `mov` | Mover datos entre registros/memoria |
| `intercambiar` | `xchg` | Intercambiar valores entre operandos |
| `cargar_efectivo` | `lea` | Cargar dirección efectiva |
| `extender_cero` | `movzx` | Mover con extensión de ceros |
| `extender_signo` | `movsx` | Mover con extensión de signo |

---

## ➕ Aritmética

| Español | ASM | Descripción |
|---------|-----|-------------|
| `sumar`, `añadir` | `add` | Sumar dos operandos |
| `restar` | `sub` | Restar dos operandos |
| `multiplicar` | `mul` | Multiplicación sin signo |
| `multiplicar_signado` | `imul` | Multiplicación con signo |
| `dividir` | `div` | División sin signo |
| `dividir_signado` | `idiv` | División con signo |
| `incrementar` | `inc` | Incrementar en 1 |
| `decrementar` | `dec` | Decrementar en 1 |
| `negar` | `neg` | Negar (complemento a 2) |

---

## 🔢 Operaciones Lógicas

| Español | ASM | Descripción |
|---------|-----|-------------|
| `y` | `and` | AND lógico bit a bit |
| `o` | `or` | OR lógico bit a bit |
| `no` | `not` | NOT lógico (complemento a 1) |
| `exclusivo` | `xor` | XOR lógico bit a bit |
| `desplazar_izq` | `shl`, `sal` | Desplazamiento lógico/aritmético izq. |
| `desplazar_der` | `shr`, `sar` | Desplazamiento lógico/aritmético der. |
| `rotar_izq` | `rol` | Rotación a la izquierda |
| `rotar_der` | `ror` | Rotación a la derecha |

---

## 🔍 Comparación y Prueba

| Español | ASM | Descripción |
|---------|-----|-------------|
| `comparar` | `cmp` | Comparar dos operandos |
| `probar` | `test` | AND lógico sin guardar el resultado |

---

## 🎯 Control de Flujo

### Saltos Incondicionales

| Español | ASM | Descripción |
|---------|-----|-------------|
| `saltar` | `jmp` | Salto incondicional |
| `llamar` | `call` | Llamar a subrutina |
| `retornar`, `volver` | `ret` | Retornar de subrutina |

### Saltos Condicionales

| Español | ASM | Descripción |
|---------|-----|-------------|
| `si_igual` | `je`, `jz` | Saltar si igual / si cero |
| `si_no_igual` | `jne`, `jnz` | Saltar si no igual / si no cero |
| `si_mayor` | `jg` | Saltar si mayor (signado) |
| `si_mayor_igual` | `jge` | Saltar si mayor o igual (signado) |
| `si_menor` | `jl` | Saltar si menor (signado) |
| `si_menor_igual` | `jle` | Saltar si menor o igual (signado) |
| `si_arriba` | `ja` | Saltar si arriba (sin signo) |
| `si_abajo` | `jb` | Saltar si abajo (sin signo) |
| `si_arriba_igual` | `jae` | Saltar si arriba o igual (sin signo) |
| `si_abajo_igual` | `jbe` | Saltar si abajo o igual (sin signo) |
| `si_signo` | `js` | Saltar si el bit de signo está activado |
| `si_no_signo` | `jns` | Saltar si el bit de signo no está activado |
| `si_desborde` | `jo` | Saltar si hubo desborde |
| `si_no_desborde` | `jno` | Saltar si no hubo desborde |
| `si_paridad` | `jp` | Saltar si paridad par |
| `si_no_paridad` | `jnp` | Saltar si paridad impar |

---

## 📚 Pila (Stack)

| Español | ASM | Descripción |
|---------|-----|-------------|
| `meter` | `push` | Insertar valor en la pila |
| `sacar` | `pop` | Extraer valor de la pila |
| `meter_banderas` | `pushf` | Insertar registro de banderas |
| `sacar_banderas` | `popf` | Extraer registro de banderas |

---

## 🔤 Operaciones de Cadenas

| Español | ASM | Descripción |
|---------|-----|-------------|
| `mover_byte` | `movsb` | Mover byte de cadena |
| `mover_palabra` | `movsw` | Mover palabra de cadena |
| `mover_doble` | `movsd` | Mover doble palabra de cadena |
| `almacenar_byte` | `stosb` | Almacenar byte en cadena |
| `cargar_byte` | `lodsb` | Cargar byte de cadena |
| `escanear_byte` | `scasb` | Escanear byte en cadena |
| `repetir` | `rep` | Repetir operación |
| `repetir_mientras` | `repne` | Repetir mientras no sea igual |

---

## 🔁 Bucles

| Español | ASM | Descripción |
|---------|-----|-------------|
| `ciclo` | `loop` | Decrementar RCX y saltar si RCX ≠ 0 |
| `ciclo_si_cero` | `loopz` | Loop si zero flag está activado |
| `ciclo_si_no_cero` | `loopnz` | Loop si zero flag no está activado |

---

## ⚙️ Sistema

| Español | ASM | Descripción |
|---------|-----|-------------|
| `interrupcion` | `int` | Llamar interrupción software |
| `llamada_sistema` | `syscall` | Llamada al sistema (x86_64) |
| `retorno_sistema` | `sysret` | Retorno de llamada al sistema |
| `retorno_interrupcion` | `iret` | Retorno de interrupción |

---

## 🛠️ Miscelánea

| Español | ASM | Descripción |
|---------|-----|-------------|
| `nada` | `nop` | No hacer nada |
| `detener` | `hlt` | Detener CPU hasta próxima interrupción |
| `limpiar_interrupciones` | `cli` | Deshabilitar interrupciones |
| `activar_interrupciones` | `sti` | Habilitar interrupciones |
| `limpiar_direccion` | `cld` | Limpiar flag de dirección |
| `fijar_direccion` | `std` | Fijar flag de dirección |
| `esperar` | `wait` | Esperar operación de coprocesador |

---

## 🔄 Conversión de Tamaños

| Español | ASM | Descripción |
|---------|-----|-------------|
| `convertir_byte_palabra` | `cbw` | Convertir byte a palabra |
| `convertir_palabra_doble` | `cwd` | Convertir palabra a doble palabra |
| `convertir_doble_cuadruple` | `cdq` | Convertir doble palabra a cuádruple |
| `convertir_cuadruple_octo` | `cqo` | Convertir cuádruple a octopalabra |

---

## 📝 Ejemplo de Uso

```asm
; Función que suma dos números
funcion_suma:
    meter rbp               ; push rbp
    mover rbp, rsp          ; mov rbp, rsp
    
    sumar rdi, rsi          ; add rdi, rsi
    mover rax, rdi          ; mov rax, rdi
    
    sacar rbp               ; pop rbp
    retornar                ; ret
```

> [!TIP]
> Todas las instrucciones estándar en inglés (mov, add, jmp, etc.) también funcionan directamente sin traducción.

---

**Total:** 80+ instrucciones x86_64 soportadas en Español.  
**MultiLang-ASM** — Parte del ecosistema **Neuro-OS.es**.
