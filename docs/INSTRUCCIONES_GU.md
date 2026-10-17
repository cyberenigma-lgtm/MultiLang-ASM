# MultiLang-ASM: Manual de Instrucciones [GU]

**Idioma:** Gujarati / ગુજરાતી (`gu`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 21  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `અટકો` | `hlt` |
| `અથવા` | `or` |
| `અને` | `and` |
| `અવરોધ` | `int` |
| `ઉમેરો` | `add` |
| `કંઈ_નહીં` | `nop` |
| `કાઢો` | `pop` |
| `કૂદો` | `jmp` |
| `ખસેડો` | `mov` |
| `ગુણાકાર` | `mul` |
| `નથી` | `not` |
| `પરીક્ષણ` | `test` |
| `પાછા` | `ret` |
| `બાદ_કરો` | `sub` |
| `બોલાવો` | `call` |
| `ભાગાકાર` | `div` |
| `મૂકો` | `push` |
| `લૂપ` | `loop` |
| `વિશિષ્ટ` | `xor` |
| `સરખામણી` | `cmp` |
| `સિસ્ટમ_કૉલ` | `syscall` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Gujarati / ગુજરાતી (gu)
section .text
global _start

_start:
    ખસેડો rax, 1
    ખસેડો rdi, 1
    ખસેડો rsi, msg
    ખસેડો rdx, 13
    સિસ્ટમ_કૉલ

    ખસેડો rax, 60
    ખસેડો rdi, 0
    સિસ્ટમ_કૉલ

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm gu programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build gu programa.masm
```
