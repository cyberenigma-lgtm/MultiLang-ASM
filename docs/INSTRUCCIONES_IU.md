# MultiLang-ASM: Manual de Instrucciones [IU]

**Idioma:** Inuktitut / ᐃᓄᒃᑎᑐᑦ (`iu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `ᐃᓚᓯᕗᖅ` | `add` |
| `ᐃᓚᖔᖅᐹ` | `sub` |
| `ᐃᓯᖅᑎᑉᐹ` | `push` |
| `ᐅᑎᖅᐳᖅ` | `ret` |
| `ᐅᕝᕙᓘᓐᓃᑦ` | `or` |
| `ᐊᒥᓱᖑᖅᑎᐹ` | `mul` |
| `ᐊᒻᒪᓗ` | `and` |
| `ᐊᓂᑎᑉᐹ` | `pop` |
| `ᐊᓯᐊᒍᑦ` | `xor` |
| `ᐊᔾᔨᒌᖕᓂᖏᑦ` | `cmp` |
| `ᐊᕕᒃᑐᖅᐹ` | `div` |
| `ᐋᒃᑲ` | `not` |
| `ᑲᐃᕙᓪᓚᒍᑎ` | `loop` |
| `ᓄᖅᑲᕆᑦ` | `hlt` |
| `ᓄᖅᑲᖅᑎᑦᑎᕗᖅ` | `int` |
| `ᓅᑎᕆᕗᖅ` | `mov` |
| `ᓱᓇᖃᙱᑦᑐᖅ` | `nop` |
| `ᖃᐃᖁᔨᕗᖅ` | `call` |
| `ᖃᐅᔨᓴᖅᐳᖅ` | `test` |
| `ᖃᕆᑕᐅᔭᐅᑉ_ᑐᒃᓯᕋᐅᑎᖓ` | `syscall` |
| `ᖃᖓᑕᕗᖅ` | `jmp` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Inuktitut / ᐃᓄᒃᑎᑐᑦ (iu)
section .text
global _start

_start:
    ᓅᑎᕆᕗᖅ rax, 1
    ᓅᑎᕆᕗᖅ rdi, 1
    ᓅᑎᕆᕗᖅ rsi, msg
    ᓅᑎᕆᕗᖅ rdx, 13
    ᖃᕆᑕᐅᔭᐅᑉ_ᑐᒃᓯᕋᐅᑎᖓ

    ᓅᑎᕆᕗᖅ rax, 60
    ᓅᑎᕆᕗᖅ rdi, 0
    ᖃᕆᑕᐅᔭᐅᑉ_ᑐᒃᓯᕋᐅᑎᖓ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm iu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build iu programa.masm
```
