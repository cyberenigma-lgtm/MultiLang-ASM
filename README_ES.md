# 🛡️ MultiLang-ASM v1.0.0
<p align="center">
  <img src="assets/banner.png" alt="MultiLang-ASM Banner" width="800">
</p>

> *"No saber inglés no debería impedirte crear. La imaginación no tiene idioma y la máquina solo entiende binario."*

**El primer motor de ensamblador x86_64 soberano y multilingüe del mundo.**  
Componente oficial de bajo nivel del ecosistema **UPL (Universal Polyglot Layer)** y del núcleo de **Neuro-OS**.

Escribe código ensamblador en tu lengua materna · 150 Idiomas del Mundo · 200+ Instrucciones x86_64 Canónicas · Motor Nativo 100% ANSI C99 · Cero Dependencias de Python · Rendimiento Instantáneo (<2 ms) · 100% Compatible con NASM/FASM/GAS.

[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](LICENSE)
[![Estándar: ANSI C99](https://img.shields.io/badge/Est%C3%A1ndar-ANSI%20C99-blue.svg)](src/)
[![Idiomas](https://img.shields.io/badge/idiomas-150%20Global-success.svg)](LISTA_PAISES_LENGUAS.md)
[![Instrucciones](https://img.shields.io/badge/instrucciones-200%2B%20x86__64-brightgreen.svg)](docs/INSTRUCCIONES_ES.md)
[![Ecosistema: UPL+](https://img.shields.io/badge/Ecosistema-UPL%2B%20Soberano-purple.svg)](https://github.com/cyberenigma-lgtm/UNIVERSAL-POLYGLOT-LAYER-UPL)

📜 **[Genealogía del Ecosistema Neuro-ASM](https://github.com/cyberenigma-lgtm/NeuroUniversalASM/blob/main/docs/genealogia_neuro_asm.md)**  
Consulta la evolución completa desde MultiLang-ASM hasta NeuroWill-Code.

📖 **[Español](README_ES.md)** | **[English](README.md)** | **[Français](README_FR.md)** | **[Deutsch](README_DE.md)** | **[Italiano](README_IT.md)** | **[Português](README_PT.md)** | **[Русский](README_RU.md)** | **[日本語](README_JA.md)** | **[中文](README_ZH.md)** | **[한국어](README_KO.md)** | **[العربية](README_AR.md)** | **[Bahasa](README_ID.md)** | **[Hindi](README_HI.md)** | **[Türkçe](README_TR.md)** | **[Polski](README_PL.md)** | **[Svenska](README_SV.md)** | **[Nederlands](README_NL.md)**

---

## 🚀 ¿Qué es esto?

Ya no necesitas dominar inglés para crear kernels, drivers o firmware.  
Este proyecto demuestra que las barreras lingüísticas en la programación son **artificiales** y eliminables.

**MultiLang-ASM** es una capa de preprocesamiento y ensamblador políglota para **x86_64**. Permite a cualquier persona redactar código de bajo nivel utilizando palabras clave en su idioma materno, transpilándolo de forma instantánea a código compatible con NASM. Además, soporta **traducción reversible (modo PRETTY)**, permitiendo inspeccionar ensamblador estándar en cualquiera de las lenguas soportadas.

---

## 💡 ¿Por qué importa? (Justicia Tecnológica)

La inmensa mayoría de las herramientas de bajo nivel fueron diseñadas bajo una convención histórica anglocéntrica hace décadas. Esto ha levantado una barrera invisible que excluye a millones de personas con talento, creatividad y brillantez lógica.

**MultiLang-ASM rompe esa herencia** y abre la puerta a:
- **Estudiantes** que aprenden arquitectura de computadores en su lengua materna.
- **Autodidactas** sin acceso a educación formal en inglés.
- **Comunidades e ingenieros** de todo el mundo que hoy pueden desarrollar sistemas operativos soberanos.
- **Niños y jóvenes** que pueden experimentar con registros y memoria sin barreras artificiales.

No es solo código. Es **justicia y soberanía tecnológica**.

---

## 🏗️ La Filosofía: "Un Puente, no una Burbuja"

A nuestros colegas de la comunidad **OSDev**: no estamos reinventando la rueda; estamos construyendo una rampa de acceso hacia ella.

MultiLang-ASM funciona como una **herramienta puente** de latencia cero:
1. **Etapa 1: Accesibilidad** (Sintaxis nativa o modo simplificado para comprender el flujo de registros).
2. **Etapa 2: Transición** (Comprensión bilingüe y visualización reversible).
3. **Etapa 3: Competencia Profesional** (Familiaridad total con la arquitectura x86_64 y NASM estándar).

👉 Consulta la **[Guía de Transición](docs/TRANSITION_GUIDE.md)** para ver cómo guiamos a los desarrolladores paso a paso hacia el bajo nivel.  
**El resultado final es 100% compatible con NASM.** No hay capas de abstracción innecesarias ni pérdida de rendimiento: la CPU ejecuta directamente código máquina nativo.

---

## ✨ Novedades y Evolución Histórica

### 🔥 Novedades de la Versión 1.0.0 (Soberana UPL+ / ANSI C99)
- ⚡ **Revolución C99 Nativa (0% Python)**: Se ha reescrito el núcleo completo en ANSI C99 puro (`src/mlasm_core.c` y `src/masm_tables.h`). No requiere instalar Python ni ningún runtime para transcpilar o compilar. Binario autónomo de <80 KB.
- 🌍 **Expansión a 150 Lenguas del Mundo**: Soporte exhaustivo para 150 idiomas de Europa, América, África, Asia y Oceanía (incluyendo Latín, Esperanto, Guaraní, Náhuatl, Maya, Quechua, Suajili, Cheroqui, Inuktitut, etc.).
- ⚙️ **Repertorio de 200+ Instrucciones Canónicas**: Cobertura exhaustiva de x86_64 (Movimiento, Aritmética, Lógica, Bits, Banderas, Cadenas, Bucles, Sistema, Descriptores GDT/IDT y FPU/x87).
- ⏱️ **Rendimiento Instantáneo**: Transpila miles de líneas de ensamblador en **menos de 2 milisegundos**.
- 🤖 **Auto-Detección Avanzada**: Reconocimiento inteligente de idioma por análisis léxico (`mlasm auto archivo.masm`).
- 🔁 **Modo Inverso Reversible Bidireccional**: Convierte código NASM estándar a cualquiera de los 150 idiomas (`mlasm --reverse <lang>`).
- 🧠 **Macros Nativas (`%define`)**: Preprocesador de constantes integrado en C99.
- 📦 **Compilación Directa (`--build`)**: Transpila, compila con NASM y enlaza con GCC en un solo paso (`mlasm --build es archivo.masm`).

### 🔥 Novedades en v0.7 (Global Expansion)
- 🏛️ Cobertura regional de 56 variantes lingüísticas en Europa, América, África, Asia y Oceanía.
- 🗺️ Creación del [Listado Maestro de Países y Lenguas](LISTA_PAISES_LENGUAS.md).
- 📚 Generación de manuales localizados para cada paquete de idioma.

### 🔥 Novedades en v0.6 (Babel Community)
- 📂 Arquitectura modular de diccionarios externos y gobernanza abierta.
- 🛠️ CLI de contribuidores y políticas de seguridad.

### 🔥 Novedades en v0.5 (Modo Niños y Modo Profesional)
- 🧸 **Kids Mode (Modo Niños)**: Suite educativa dedicada. 👉 **[Visitar Repositorio MultiLang-ASM Kids](https://github.com/cyberenigma-lgtm/MultiLang-ASM-Kids)**
  ```asm
  ; Modo Niños (Español)
  pon rax a 5
  suma rax con 3
  enseña rax
  ```
- 🛡️ **Modo Profesional**: Sintaxis estructurada con comentarios multilingües y compatibilidad con pipelines de NASM.

---

## 🛠️ Instalación y Compilación Nativa

### 1. Compilación del Motor Nativo (Cero Dependencias)

**En Windows (MinGW / GCC):**
```cmd
gcc -std=c99 -Wall -Wextra -Werror -O2 src/mlasm_core.c -I src -o bin/mlasm.exe
```
*(O ejecuta directamente `mlasm.bat`, el cual compila automáticamente el binario si no existe).*

**En Linux / macOS:**
```bash
make
# o directamente: gcc -std=c99 -Wall -Wextra -Werror -O2 src/mlasm_core.c -I src -o bin/mlasm
```

### 2. Comandos Principales de la CLI

```bash
# Transpilar especificando el idioma:
mlasm es examples/hello_es.masm -o bin/hello_es.asm

# Auto-detección inteligente del idioma:
mlasm auto examples/hello_zh.masm -o bin/hello_zh.asm

# Modo inverso (NASM Estándar -> Idioma Nativo):
mlasm --reverse es bin/hello_es.asm -o bin/hello_invertido.masm

# Compilación directa de .masm a ejecutable binario:
mlasm --build es examples/hello_es.masm

# Ejecutar la suite nativa de pruebas unitarias:
mlasm --test

# Listar los 150 idiomas soportados:
mlasm --list-langs
```

---

## 🔬 Ejemplo Completo de Flujo de Trabajo

### Paso 1: Escribir el programa en tu idioma
Crea el archivo `hola.masm` en Español:
```asm
; Programa: Hola Mundo en Español
seccion .texto
global _start

_start:
    mover rax, 1        ; llamada al sistema: write (1)
    mover rdi, 1        ; descriptor de archivo: stdout (1)
    mover rsi, mensaje  ; puntero al mensaje
    mover rdx, 13       ; longitud del mensaje
    llamada_sistema     ; invocar al kernel

    mover rax, 60       ; llamada al sistema: exit (60)
    mover rdi, 0        ; código de salida: 0 (éxito)
    llamada_sistema

seccion .datos
    mensaje db "Hola Mundo!", 0xA
```

### Paso 2: Transpilar con MultiLang-ASM
```bash
mlasm es hola.masm -o hola.asm
```
Salida en consola:
```
[OK] Transpilado con exito: hola.masm -> hola.asm
     Idioma: [es] Spanish / Español | Lineas procesadas: 18
```

### Paso 3: Ensamblar y Enlazar
```bash
nasm -f win64 hola.asm -o hola.o
gcc hola.o -o hola.exe -nostartfiles
```

### Paso 4: Ejecutar
```cmd
.\hola.exe
# Salida: Hola Mundo!
```

---

## 📊 Repertorio de 200+ Instrucciones Canónicas Soportadas

| Categoría | Instrucciones NASM Soportadas | Ejemplos en Español |
| :--- | :--- | :--- |
| **Transferencia de Datos** | `mov`, `xchg`, `lea`, `movzx`, `movsx`, `cmove`, `cmovz`, `cmovne`, `cmova`, `cmovb`, `cmovg`, `cmovl`, `bswap`, `xadd`, `movbe` | `mover`, `intercambiar`, `cargar_efectivo`, `extender_cero`, `mover_si_igual`, `intercambiar_bytes` |
| **Aritmética Entera** | `add`, `adc`, `sub`, `sbb`, `mul`, `imul`, `div`, `idiv`, `inc`, `dec`, `neg`, `daa`, `das`, `aaa`, `aas`, `aam`, `aad` | `sumar`, `sumar_con_acarreo`, `restar`, `multiplicar`, `dividir`, `incrementar`, `decrementar`, `negar` |
| **Lógica y Manipulación de Bits** | `and`, `or`, `not`, `xor`, `shl`, `shr`, `sal`, `sar`, `rol`, `ror`, `rcl`, `rcr`, `shld`, `shrd`, `bt`, `bts`, `btr`, `btc`, `bsf`, `bsr`, `popcnt`, `lzcnt`, `tzcnt`, `andn` | `y`, `o`, `no`, `exclusivo`, `desplazar_izq`, `rotar_der`, `probar_bit`, `fijar_bit`, `contar_unos` |
| **Comparación y Prueba** | `cmp`, `test`, `cmpsb`, `cmpsw`, `cmpsd`, `cmpsq` | `comparar`, `probar`, `comparar_bytes`, `comparar_dobles` |
| **Fijar Condición (SETcc)** | `sete`, `setz`, `setne`, `setnz`, `seta`, `setae`, `setb`, `setbe`, `setg`, `setge`, `setl`, `setle`, `sets`, `seto`, `setc`, `setp` | `fijar_si_igual`, `fijar_si_cero`, `fijar_si_mayor`, `fijar_si_menor`, `fijar_si_acarreo` |
| **Control de Flujo y Saltos** | `jmp`, `call`, `ret`, `je`, `jz`, `jne`, `jnz`, `jg`, `jge`, `jl`, `jle`, `ja`, `jb`, `jae`, `jbe`, `js`, `jo`, `jp`, `jcxz`, `jecxz`, `jrcxz` | `saltar`, `llamar`, `retornar`, `si_igual`, `si_cero`, `si_no_igual`, `si_mayor`, `si_menor` |
| **Gestión de Pila (Stack)** | `push`, `pop`, `pushf`, `popf`, `pushfq`, `popfq`, `pusha`, `popa`, `enter`, `leave` | `meter`, `sacar`, `meter_banderas`, `sacar_banderas`, `entrar`, `salir` |
| **Cadenas de Memoria** | `movsb`, `movsw`, `movsd`, `movsq`, `stosb`, `stosw`, `stosd`, `stosq`, `lodsb`, `lodsw`, `lodsd`, `lodsq`, `scasb`, `scasw`, `scasd`, `scasq` | `mover_byte`, `mover_palabra`, `almacenar_byte`, `cargar_byte`, `escanear_byte` |
| **Bucles y Repetición** | `loop`, `loopz`, `loope`, `loopnz`, `loopne`, `rep`, `repe`, `repz`, `repne`, `repnz`, `pause` | `ciclo`, `ciclo_si_cero`, `repetir`, `repetir_mientras`, `pausa` |
| **Sistema, Privilegios y CPU** | `int`, `int3`, `into`, `syscall`, `sysret`, `sysenter`, `sysexit`, `iret`, `iretd`, `iretq`, `rsm`, `cpuid`, `rdtsc`, `rdtscp`, `rdmsr`, `wrmsr`, `clc`, `stc`, `cmc`, `cld`, `std`, `cli`, `sti`, `lahf`, `sahf`, `nop`, `hlt`, `wait` | `interrupcion`, `llamada_sistema`, `retorno_sistema`, `identificar_cpu`, `leer_contador_tiempo`, `nada`, `detener` |
| **Puertos y Barreras de Memoria** | `in`, `out`, `insb`, `insw`, `insd`, `outsb`, `outsw`, `outsd`, `lfence`, `mfence`, `sfence`, `clflush`, `invd`, `wbinvd` | `entrada_puerto`, `salida_puerto`, `barrera_carga`, `barrera_memoria`, `limpiar_cache` |
| **Tablas del Sistema** | `lgdt`, `sgdt`, `lidt`, `sidt`, `lldt`, `sldt`, `ltr`, `str` | `cargar_gdt`, `almacenar_gdt`, `cargar_idt`, `almacenar_idt`, `cargar_tr` |
| **FPU / x87** | `fld`, `fst`, `fstp`, `fadd`, `fsub`, `fmul`, `fdiv`, `fchs`, `fabs`, `fsqrt`, `fsin`, `fcos`, `finit`, `fclex`, `fnop` | `fpu_cargar`, `fpu_almacenar`, `fpu_sumar`, `fpu_restar`, `fpu_raiz`, `fpu_seno`, `fpu_inicializar` |
| **Conversión de Tamaños** | `cbw`, `cwd`, `cdq`, `cqo`, `cwde`, `cdqe` | `convertir_byte_palabra`, `convertir_palabra_doble`, `convertir_doble_cuadruple` |

*(Cualquier instrucción x86_64 adicional que no figure explícitamente en el diccionario pasa automáticamente a NASM sin alteraciones gracias al motor pass-through).*

---

## 🗺️ Cobertura Lingüística Mundial (150 Lenguas)

MultiLang-ASM cuenta con manuales técnicos individuales para cada una de sus **150 lenguas**:
- **Europa (46 lenguas)**: [Español](docs/INSTRUCCIONES_ES.md), [Catalán](docs/INSTRUCCIONES_CA.md), [Gallego](docs/INSTRUCCIONES_GL.md), [Euskera](docs/INSTRUCCIONES_EU.md), [Asturiano](docs/INSTRUCCIONES_AST.md), [Aragonés](docs/INSTRUCCIONES_AN.md), [Francés](docs/INSTRUCCIONES_FR.md), [Alemán](docs/INSTRUCCIONES_DE.md), [Italiano](docs/INSTRUCCIONES_IT.md), [Portugués](docs/INSTRUCCIONES_PT.md), [Inglés](docs/INSTRUCCIONES_EN.md), [Ruso](docs/INSTRUCCIONES_RU.md), [Ucraniano](docs/INSTRUCCIONES_UK.md), [Polaco](docs/INSTRUCCIONES_PL.md), [Checo](docs/INSTRUCCIONES_CS.md), [Eslovaco](docs/INSTRUCCIONES_SK.md), [Húngaro](docs/INSTRUCCIONES_HU.md), [Griego](docs/INSTRUCCIONES_EL.md), [Latín](docs/INSTRUCCIONES_LA.md), [Esperanto](docs/INSTRUCCIONES_EO.md), etc.
- **América (16 lenguas)**: [Náhuatl](docs/INSTRUCCIONES_NAH.md), [Maya](docs/INSTRUCCIONES_MAY.md), [Quechua](docs/INSTRUCCIONES_QU.md), [Aimara](docs/INSTRUCCIONES_AY.md), [Guaraní](docs/INSTRUCCIONES_GN.md), [Cheroqui](docs/INSTRUCCIONES_CHR.md), [Navajo](docs/INSTRUCCIONES_NAV.md), [Inuktitut](docs/INSTRUCCIONES_IU.md), [Groenlandés](docs/INSTRUCCIONES_KL.md), [Hawaiano](docs/INSTRUCCIONES_HAW.md), etc.
- **África (36 lenguas)**: [Suajili](docs/INSTRUCCIONES_SW.md), [Amárico](docs/INSTRUCCIONES_AM.md), [Oromo](docs/INSTRUCCIONES_OM.md), [Tigriña](docs/INSTRUCCIONES_TI.md), [Somalí](docs/INSTRUCCIONES_SO.md), [Hausa](docs/INSTRUCCIONES_HA.md), [Yoruba](docs/INSTRUCCIONES_YO.md), [Igbo](docs/INSTRUCCIONES_IG.md), [Zulú](docs/INSTRUCCIONES_ZU.md), [Afrikaans](docs/INSTRUCCIONES_AF.md), etc.
- **Asia y Oceanía (52 lenguas)**: [Chino](docs/INSTRUCCIONES_ZH.md), [Japonés](docs/INSTRUCCIONES_JA.md), [Coreano](docs/INSTRUCCIONES_KO.md), [Vietnamita](docs/INSTRUCCIONES_VI.md), [Hindi](docs/INSTRUCCIONES_HI.md), [Urdu](docs/INSTRUCCIONES_UR.md), [Bengalí](docs/INSTRUCCIONES_BN.md), [Tamil](docs/INSTRUCCIONES_TA.md), [Árabe](docs/INSTRUCCIONES_AR.md), [Hebreo](docs/INSTRUCCIONES_HE.md), [Turco](docs/INSTRUCCIONES_TR.md), [Persa](docs/INSTRUCCIONES_FA.md), [Maorí](docs/INSTRUCCIONES_MI.md), [Tok Pisin](docs/INSTRUCCIONES_TPI.md), etc.

Consulta el desglose geográfico en **[LISTA_PAISES_LENGUAS.md](LISTA_PAISES_LENGUAS.md)**.

---

## 📁 Estructura del Proyecto

```
MultiLang-ASM/
├── src/                  # Motor nativo en ANSI C99
│   ├── mlasm_core.c      # Preprocesador y transpilador autónomo
│   └── masm_tables.h     # Tablas maestras compiladas de 150 lenguas
├── bin/                  # Ejecutables generados (mlasm / mlasm.exe)
├── langs/                # Paquetes declarativos universales (150 archivos .json)
├── examples/             # Ejemplos políglotas (hello_es, hello_zh, hello_la, hello_sw...)
├── docs/                 # Manuales de instrucciones (150 archivos INSTRUCCIONES_<LANG>.md)
├── wiki/                 # Documentación técnica, tutoriales de kernel y arquitectura
├── test.bat              # Suite de validación nativa para Windows
├── test.sh               # Suite de validación nativa para Linux / macOS
├── Makefile              # Compilación nativa estándar multiplataforma
├── mlasm.bat             # Lanzador nativo de Windows (con auto-compilación)
├── LISTA_PAISES_LENGUAS.md # Directorio mundial de cobertura por países
├── CHANGELOG.md          # Registro de cambios y evolución de versiones
└── README.md             # Documentación maestra
```

---

## ⚖️ Disclaimer Técnico

**MultiLang-ASM no pretende sustituir a NASM, FASM o GCC.**

Es un **preprocesador humano de latencia cero** que suprime la barrera del idioma sin introducir capas de emulación ni consumo de recursos. El archivo resultante es ensamblador x86_64 estándar que se compila directamente a binario nativo. La CPU recibe exactamente los mismos opcodes.

---

## 💭 Mensaje del Autor

> *"No saber inglés no debería ser una barrera para crear. El conocimiento debe fluir en todos los idiomas."*

Si este proyecto te ha resultado útil, compártelo. Cada desarrollador que programa en su lengua materna es una victoria contra las barreras artificiales en la tecnología.

---

## 🤝 ¿Quieres Contribuir?

MultiLang-ASM está abierto a colaboraciones de todo el mundo.  
No necesitas dominar ensamblador: si hablas una lengua o dialecto, puedes colaborar mejorando equivalencias, redactando ejemplos o creando tutoriales.

- 🌍 Añadir o afinar equivalencias en los diccionarios de `langs/*.json`.
- 📚 Crear ejemplos de kernels o bootloaders en tu lengua.
- 🐛 Reportar incidencias o sugerir mejoras en el motor C99.
- ⭐ Dar una estrella al repositorio para apoyar la soberanía tecnológica.

Consulta **[CONTRIBUTING.md](CONTRIBUTING.md)** y la guía de **[BABEL_COMMUNITY.md](BABEL_COMMUNITY.md)** para comenzar.

---

## 📧 Contacto y Comunidad

- **Email:** neuro.so.ia.sim@gmail.com
- **Issues:** [GitHub Issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)
- **Discussions:** [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions)

---

**Versión:** v1.0.0 (Sovereign UPL+ C99 Edition)  
**Licencia:** MIT - Ver [LICENSE](LICENSE) para más detalles.  
**Autor:** J / Neuro-OS Project  
**Repositorio Oficial:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

🛡️ **Parte integral de los ecosistemas [Neuro-OS](https://neuro-os.es) y [UNIVERSAL-POLYGLOT-LAYER-UPL](https://github.com/cyberenigma-lgtm/UNIVERSAL-POLYGLOT-LAYER-UPL).**  
*Este proyecto es un manifiesto de soberanía: la tecnología debe adaptarse a los seres humanos, no los seres humanos a la tecnología.*
