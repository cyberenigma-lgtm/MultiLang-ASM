# MultiLang-ASM v1.0.0
<p align="center">
  <img src="assets/banner.png" alt="MultiLang-ASM Banner" width="800">
</p>

**The world's first sovereign multilingual x86_64 assembler engine.**  
Part of the **UPL (Universal Polyglot Layer)** Ecosystem & Neuro-OS Core.

Write assembly in your native language · 150 World Languages & Dialects · 200+ Canonical x86_64 Instructions · 100% ANSI C99 Native Engine · Zero Python Runtime Dependencies · Instant Execution (<2 ms) · NASM/FASM/GAS-compatible.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Standard: ANSI C99](https://img.shields.io/badge/Standard-ANSI%20C99-blue.svg)](src/)
[![Languages](https://img.shields.io/badge/languages-150%20Global-success.svg)](LISTA_PAISES_LENGUAS.md)
[![Instructions](https://img.shields.io/badge/instructions-200%2B%20x86__64-brightgreen.svg)](docs/INSTRUCCIONES_ES.md)
[![Ecosystem: UPL+](https://img.shields.io/badge/Ecosystem-UPL%2B%20Sovereign-purple.svg)](https://github.com/cyberenigma-lgtm/UNIVERSAL-POLYGLOT-LAYER-UPL)

📜 **[Genealogy of the Neuro-ASM Ecosystem](https://github.com/cyberenigma-lgtm/NeuroUniversalASM/blob/main/docs/genealogia_neuro_asm.md)**  
Explore the complete architectural evolution from MultiLang-ASM to NeuroWill-Code.

📖 **[English](README.md)** | **[Español](README_ES.md)** | **[Français](README_FR.md)** | **[Deutsch](README_DE.md)** | **[Italiano](README_IT.md)** | **[Português](README_PT.md)** | **[Русский](README_RU.md)** | **[日本語](README_JA.md)** | **[中文](README_ZH.md)** | **[한국어](README_KO.md)** | **[العربية](README_AR.md)** | **[Bahasa](README_ID.md)** | **[Hindi](README_HI.md)** | **[Türkçe](README_TR.md)** | **[Polski](README_PL.md)** | **[Svenska](README_SV.md)** | **[Nederlands](README_NL.md)**

---

## 🚀 What is MultiLang-ASM?

MultiLang-ASM is an ultra-fast, zero-dependency multilingual assembler and preprocessor for **x86_64**.  
It allows developers, students, and kernel engineers worldwide to write low-level code in their mother tongue, instantly transpiling to standard NASM syntax.

Originally prototyped in Python, **version 1.0.0 is rewritten from the ground up as a pure ANSI C99 native engine**, eliminating all Python runtime requirements and achieving sub-millisecond translation speeds.

It also supports **reverse translation (PRETTY Mode)**, allowing developers to inspect standard NASM code in any of the 150 supported languages.

### Bidirectional Example (Spanish ↔ Standard NASM)

```asm
; Spanish Input (hello_es.masm)
mover rax, 1
mover rdi, 1
mover rsi, msg
mover rdx, 13
llamada_sistema

; Native mlasm compilation → Standard NASM
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 13
syscall
```

---

## 💡 Why Does This Matter? (Technological Sovereignty)

The vast majority of low-level tools were created in an English-centric historical context decades ago. This has built an invisible barrier excluding millions of brilliant minds, creative thinkers, and engineers.

**MultiLang-ASM dismantles that historical legacy** and opens systems programming to:
- **Students** learning computer architecture in their mother tongue.
- **Self-taught developers** without formal English education.
- **Sovereign engineering communities** building custom operating systems across the globe.
- **Children and young students** exploring registers and memory without artificial barriers.

This is not just code. It is **technological justice and digital sovereignty**.

---

## 🏗️ The Philosophy: "A Bridge, Not a Bubble"

To our colleagues in the **OSDev Community**: We are not reinventing the wheel. We are building a ramp to it.

MultiLang-ASM acts as a zero-overhead **Bridge Tool**:
1. **Stage 1: Accessibility** (Native or simplified syntax to understand registers, stack, and logic).
2. **Stage 2: Transition** (Bilingual inspection and bidirectional reverse mode).
3. **Stage 3: Standard Proficiency** (Pure NASM proficiency and bare-metal mastery).

👉 **[Read the Transition Guide](docs/TRANSITION_GUIDE.md)** to see how we guide users step-by-step from native terms to pure NASM.  
**Output is 100% NASM Compatible.** No heavy runtime. No abstraction layer. Just access.

---

## ✨ Features and Version History

### 🔥 What's New in v1.0.0 (Sovereign UPL+ Edition / ANSI C99)
- ⚡ **100% Standalone ANSI C99 Native Engine**: Zero runtime dependencies. Compiles to an ultra-compact binary (<80 KB) with any C99 compiler (`gcc`, `clang`, `tcc`, `msvc`).
- 🌍 **150 World Languages**: Complete coverage across all 5 continents (Europe, Americas, Africa, Asia, Oceania), including indigenous, classical, and regional languages.
- ⚙️ **200+ Canonical x86_64 Instructions**: Comprehensive instruction set (Movement, Arithmetic, Logic, Bit testing, Flags, Strings, Loops, System calls, Descriptor tables, and FPU/x87).
- ⏱️ **Sub-2ms Latency**: Transpiles thousands of lines of assembly in under 2 milliseconds.
- 🤖 **Instant Auto-Detection**: Automatically identifies source language from keyword frequency (`mlasm auto file.masm`).
- 🔁 **Reversible (PRETTY) Mode**: View standard NASM assembly in any of the 150 supported languages (`--reverse`).
- 🧠 **Native Macro Preprocessor**: First-class `%define` constant substitution handled directly in C99.
- 🛡️ **Pass-Through Architecture**: Any instruction not in the dictionary (e.g. `cpuid`, `rdtsc`) passes through to NASM untouched.
- 📦 **Direct Build Pipeline**: One-command compilation from multilingual ASM directly to executable binary (`mlasm --build <lang> <file.masm>`).

### 🔥 What's New in v0.7 (Global Expansion)
- 🏛️ Reached technical parity across 56 languages and dialects.
- 🗺️ Added [List of Countries and Languages](LISTA_PAISES_LENGUAS.md).
- 📚 Created localized instruction manuals in `docs/`.

### 🔥 What's New in v0.6 (Babel Community)
- 📂 Dynamic language pack structure in `langs/`.
- 🛠️ Contributor CLI and governance policies.

### 🔥 What's New in v0.5 (Kids Mode & Professional Mode)
- 🧸 **Kids Mode (Modo Niños)**: Dedicated educational suite. 👉 **[Visit MultiLang-ASM Kids Repository](https://github.com/cyberenigma-lgtm/MultiLang-ASM-Kids)**
  ```asm
  ; Kids Mode (English)
  put rax to 5
  add rax with 3
  show rax
  ```
- 🛡️ **Professional Mode**: Standard assembly syntax (`mov`, `add`, `sub`) with multilingual comments and error handling.

---

## 🛠️ Quick Start & Installation

### 1. Build the Native Engine

**On Windows (MinGW / GCC):**
```cmd
gcc -std=c99 -Wall -Wextra -Werror -O2 src/mlasm_core.c -I src -o bin/mlasm.exe
```
*(Or simply run `mlasm.bat`, which auto-compiles the binary on first execution).*

**On Linux / macOS:**
```bash
make
# or: gcc -std=c99 -Wall -Wextra -Werror -O2 src/mlasm_core.c -I src -o bin/mlasm
```

### 2. Basic CLI Usage

```bash
# Basic Transpilation:
mlasm es examples/hello_es.masm -o hello_es.asm

# Automatic Language Detection:
mlasm auto examples/hello_zh.masm -o hello_zh.asm

# Reverse Translation (NASM -> Native Language):
mlasm --reverse ru program.asm -o program_ru.masm

# Build Directly to Executable (Transpiles + NASM + GCC):
mlasm --build es examples/hello_es.masm

# Run Internal Native Test Suite:
mlasm --test

# List All 150 Supported Languages:
mlasm --list-langs
```

---

## 📊 Comprehensive 200+ Instruction Set

| Category | Supported NASM Mnemonics | Spanish Example | English Example |
| :--- | :--- | :--- | :--- |
| **Data Movement** | `mov`, `xchg`, `lea`, `movzx`, `movsx`, `cmove`, `cmovz`, `cmovne`, `cmova`, `cmovb`, `cmovg`, `cmovl`, `bswap`, `xadd`, `movbe` | `mover`, `intercambiar`, `cargar_efectivo`, `extender_cero`, `mover_si_igual` | `move`, `swap`, `load_effective_address`, `zero_extend`, `move_if_equal` |
| **Integer Arithmetic** | `add`, `adc`, `sub`, `sbb`, `mul`, `imul`, `div`, `idiv`, `inc`, `dec`, `neg`, `daa`, `das`, `aaa`, `aas`, `aam`, `aad` | `sumar`, `sumar_con_acarreo`, `restar`, `multiplicar`, `dividir`, `incrementar` | `add`, `add_with_carry`, `subtract`, `multiply`, `divide`, `increment` |
| **Logic & Bit Manipulation** | `and`, `or`, `not`, `xor`, `shl`, `shr`, `sal`, `sar`, `rol`, `ror`, `rcl`, `rcr`, `shld`, `shrd`, `bt`, `bts`, `btr`, `btc`, `bsf`, `bsr`, `popcnt`, `lzcnt`, `tzcnt`, `andn` | `y`, `o`, `no`, `exclusivo`, `desplazar_izq`, `rotar_der`, `probar_bit`, `contar_unos` | `and`, `or`, `not`, `exclusive_or`, `shift_left`, `rotate_right`, `bit_test`, `population_count` |
| **Comparison & Testing** | `cmp`, `test`, `cmpsb`, `cmpsw`, `cmpsd`, `cmpsq` | `comparar`, `probar`, `comparar_bytes`, `comparar_dobles` | `compare`, `test`, `compare_bytes`, `compare_doublewords` |
| **Set Condition (SETcc)** | `sete`, `setz`, `setne`, `setnz`, `seta`, `setae`, `setb`, `setbe`, `setg`, `setge`, `setl`, `setle`, `sets`, `seto`, `setc`, `setp` | `fijar_si_igual`, `fijar_si_cero`, `fijar_si_mayor`, `fijar_si_menor` | `set_if_equal`, `set_if_zero`, `set_if_greater`, `set_if_less` |
| **Control Flow & Jumps** | `jmp`, `call`, `ret`, `je`, `jz`, `jne`, `jnz`, `jg`, `jge`, `jl`, `jle`, `ja`, `jb`, `jae`, `jbe`, `js`, `jo`, `jp`, `jcxz`, `jecxz`, `jrcxz` | `saltar`, `llamar`, `retornar`, `si_igual`, `si_cero`, `si_no_igual`, `si_mayor` | `jump`, `call`, `return`, `if_equal`, `if_zero`, `if_not_equal`, `if_greater` |
| **Stack Operations** | `push`, `pop`, `pushf`, `popf`, `pushfq`, `popfq`, `pusha`, `popa`, `enter`, `leave` | `meter`, `sacar`, `meter_banderas`, `sacar_banderas`, `entrar`, `salir` | `push`, `pop`, `push_flags`, `pop_flags`, `enter_frame`, `leave_frame` |
| **String Operations** | `movsb`, `movsw`, `movsd`, `movsq`, `stosb`, `stosw`, `stosd`, `stosq`, `lodsb`, `lodsw`, `lodsd`, `lodsq`, `scasb`, `scasw`, `scasd`, `scasq` | `mover_byte`, `mover_palabra`, `almacenar_byte`, `cargar_byte`, `escanear_byte` | `move_byte`, `move_word`, `store_byte`, `load_byte`, `scan_byte` |
| **Loops & Repetitions** | `loop`, `loopz`, `loope`, `loopnz`, `loopne`, `rep`, `repe`, `repz`, `repne`, `repnz`, `pause` | `ciclo`, `ciclo_si_cero`, `repetir`, `repetir_mientras`, `pausa` | `loop`, `loop_if_zero`, `repeat`, `repeat_not_equal`, `pause` |
| **System & CPU Control** | `int`, `int3`, `into`, `syscall`, `sysret`, `sysenter`, `sysexit`, `iret`, `iretd`, `iretq`, `rsm`, `cpuid`, `rdtsc`, `rdtscp`, `rdmsr`, `wrmsr`, `clc`, `stc`, `cmc`, `cld`, `std`, `cli`, `sti`, `lahf`, `sahf`, `nop`, `hlt`, `wait` | `interrupcion`, `llamada_sistema`, `retorno_sistema`, `identificar_cpu`, `leer_contador_tiempo`, `nada`, `detener` | `interrupt`, `syscall`, `sysret`, `cpu_id`, `read_tsc`, `no_operation`, `halt` |
| **Memory & I/O Ports** | `in`, `out`, `insb`, `insw`, `insd`, `outsb`, `outsw`, `outsd`, `lfence`, `mfence`, `sfence`, `clflush`, `invd`, `wbinvd` | `entrada_puerto`, `salida_puerto`, `barrera_carga`, `barrera_memoria`, `limpiar_cache` | `port_in`, `port_out`, `load_fence`, `memory_fence`, `cache_flush` |
| **Descriptor Tables** | `lgdt`, `sgdt`, `lidt`, `sidt`, `lldt`, `sldt`, `ltr`, `str` | `cargar_gdt`, `almacenar_gdt`, `cargar_idt`, `almacenar_idt`, `cargar_tr` | `load_gdt`, `store_gdt`, `load_idt`, `store_idt`, `load_task_register` |
| **FPU / x87** | `fld`, `fst`, `fstp`, `fadd`, `fsub`, `fmul`, `fdiv`, `fchs`, `fabs`, `fsqrt`, `fsin`, `fcos`, `finit`, `fclex`, `fnop` | `fpu_cargar`, `fpu_almacenar`, `fpu_sumar`, `fpu_restar`, `fpu_raiz`, `fpu_inicializar` | `fpu_load`, `fpu_store`, `fpu_add`, `fpu_sub`, `fpu_sqrt`, `fpu_init` |
| **Size Conversions** | `cbw`, `cwd`, `cdq`, `cqo`, `cwde`, `cdqe` | `convertir_byte_palabra`, `convertir_palabra_doble`, `convertir_doble_cuadruple` | `convert_byte_word`, `convert_word_double`, `convert_double_quad` |

---

## 🗺️ 150 Global Languages Directory

See the complete [Country & Language Directory (LISTA_PAISES_LENGUAS.md)](LISTA_PAISES_LENGUAS.md) for detailed regional classifications across all 5 continents:
- **Europe (46 languages)**: [Spanish](docs/INSTRUCCIONES_ES.md), [Catalan](docs/INSTRUCCIONES_CA.md), [Galician](docs/INSTRUCCIONES_GL.md), [Basque](docs/INSTRUCCIONES_EU.md), [Asturian](docs/INSTRUCCIONES_AST.md), [Aragonese](docs/INSTRUCCIONES_AN.md), [French](docs/INSTRUCCIONES_FR.md), [German](docs/INSTRUCCIONES_DE.md), [Italian](docs/INSTRUCCIONES_IT.md), [Portuguese](docs/INSTRUCCIONES_PT.md), [English](docs/INSTRUCCIONES_EN.md), [Russian](docs/INSTRUCCIONES_RU.md), [Ukrainian](docs/INSTRUCCIONES_UK.md), [Polish](docs/INSTRUCCIONES_PL.md), [Czech](docs/INSTRUCCIONES_CS.md), [Slovak](docs/INSTRUCCIONES_SK.md), [Hungarian](docs/INSTRUCCIONES_HU.md), [Greek](docs/INSTRUCCIONES_EL.md), [Latin](docs/INSTRUCCIONES_LA.md), [Esperanto](docs/INSTRUCCIONES_EO.md), etc.
- **Americas (16 languages)**: [Nahuatl](docs/INSTRUCCIONES_NAH.md), [Maya](docs/INSTRUCCIONES_MAY.md), [Quechua](docs/INSTRUCCIONES_QU.md), [Aymara](docs/INSTRUCCIONES_AY.md), [Guarani](docs/INSTRUCCIONES_GN.md), [Cherokee](docs/INSTRUCCIONES_CHR.md), [Navajo](docs/INSTRUCCIONES_NAV.md), [Inuktitut](docs/INSTRUCCIONES_IU.md), [Greenlandic](docs/INSTRUCCIONES_KL.md), [Hawaiian](docs/INSTRUCCIONES_HAW.md), etc.
- **Africa (36 languages)**: [Swahili](docs/INSTRUCCIONES_SW.md), [Amharic](docs/INSTRUCCIONES_AM.md), [Oromo](docs/INSTRUCCIONES_OM.md), [Tigrinya](docs/INSTRUCCIONES_TI.md), [Somali](docs/INSTRUCCIONES_SO.md), [Hausa](docs/INSTRUCCIONES_HA.md), [Yoruba](docs/INSTRUCCIONES_YO.md), [Igbo](docs/INSTRUCCIONES_IG.md), [Zulu](docs/INSTRUCCIONES_ZU.md), [Afrikaans](docs/INSTRUCCIONES_AF.md), etc.
- **Asia & Oceania (52 languages)**: [Chinese](docs/INSTRUCCIONES_ZH.md), [Japanese](docs/INSTRUCCIONES_JA.md), [Korean](docs/INSTRUCCIONES_KO.md), [Vietnamese](docs/INSTRUCCIONES_VI.md), [Hindi](docs/INSTRUCCIONES_HI.md), [Urdu](docs/INSTRUCCIONES_UR.md), [Bengali](docs/INSTRUCCIONES_BN.md), [Tamil](docs/INSTRUCCIONES_TA.md), [Arabic](docs/INSTRUCCIONES_AR.md), [Hebrew](docs/INSTRUCCIONES_HE.md), [Turkish](docs/INSTRUCCIONES_TR.md), [Persian](docs/INSTRUCCIONES_FA.md), [Maori](docs/INSTRUCCIONES_MI.md), [Tok Pisin](docs/INSTRUCCIONES_TPI.md), etc.

---

## 📁 Project Structure

```
MultiLang-ASM/
├── src/                  # 100% ANSI C99 Native Core
│   ├── mlasm_core.c      # Standalone preprocessor and compiler driver
│   └── masm_tables.h     # Monolithic compiled tables for 150 languages
├── bin/                  # Generated native binaries (mlasm / mlasm.exe)
├── langs/                # Universal declarative definitions (150 .json files)
├── examples/             # Multilingual examples (hello_es, hello_zh, hello_la, hello_sw...)
├── docs/                 # Instruction manuals (150 INSTRUCCIONES_<LANG>.md files)
├── wiki/                 # Comprehensive documentation, kernel tutorials, architecture
├── test.bat              # Native test runner for Windows
├── test.sh               # Native test runner for Linux / macOS
├── Makefile              # Master portable C99 Makefile
├── mlasm.bat             # Native Windows launcher (with auto-build)
├── LISTA_PAISES_LENGUAS.md # Worldwide country and language directory
├── CHANGELOG.md          # Version history and changelog
└── README.md             # This file
```

---

## ⚖️ Technical Disclaimer

**MultiLang-ASM does not replace NASM, FASM, or GCC.**

It is a **zero-overhead human preprocessor** that removes linguistic barriers without introducing emulation layers or performance penalties. The generated output is pure standard x86_64 assembly that compiles directly to native machine code. The CPU executes the exact same opcodes.

---

## 💭 Author's Message

> *"Not knowing English should never be a barrier to systems programming. Knowledge belongs to all humanity, across all languages."*

If this project has helped you, share it. Every developer who writes low-level code in their mother tongue is a victory against artificial barriers in computing.

---

## 🤝 Contributing

MultiLang-ASM is open to contributors from all over the world.  
You do not need to be an assembly expert: if you speak a language or dialect, you can help refine vocabulary, translate manuals, or write kernel examples.

Check **[CONTRIBUTING.md](CONTRIBUTING.md)** and **[BABEL_COMMUNITY.md](BABEL_COMMUNITY.md)** to get started.

---

## 📧 Contact & Community

- **Email:** neuro.so.ia.sim@gmail.com
- **Issues:** [GitHub Issues](https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues)
- **Discussions:** [GitHub Discussions](https://github.com/cyberenigma-lgtm/MultiLang-ASM/discussions)

---

**Version:** v1.0.0 (Sovereign UPL+ C99 Edition)  
**License:** MIT - See [LICENSE](LICENSE) for details.  
**Author:** J / Neuro-OS Project  
**Official Repository:** https://github.com/cyberenigma-lgtm/MultiLang-ASM

🛡️ **Integral part of the [Neuro-OS](https://neuro-os.es) and [UNIVERSAL-POLYGLOT-LAYER-UPL](https://github.com/cyberenigma-lgtm/UNIVERSAL-POLYGLOT-LAYER-UPL) ecosystems.**
