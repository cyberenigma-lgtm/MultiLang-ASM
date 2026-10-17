# MultiLang-ASM: Manual de Instrucciones [KO]

**Idioma:** Korean / 한국어 (`ko`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 40  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `감소` | `dec` |
| `같으면` | `je` |
| `곱하기` | `mul` |
| `교환` | `xchg` |
| `나누기` | `div` |
| `넣기` | `push` |
| `다르면` | `jne` |
| `더블을쿼드로` | `cdq` |
| `더하기` | `add` |
| `돌아가기` | `ret` |
| `루프` | `loop` |
| `무작작` | `nop` |
| `바이트로드` | `lodsb` |
| `바이트를워드로` | `cbw` |
| `바이트이동` | `movsb` |
| `바이트저장` | `stosb` |
| `반복` | `rep` |
| `부정` | `neg` |
| `부호확장` | `movsx` |
| `비교` | `cmp` |
| `빼기` | `pop` |
| `뺄셈` | `sub` |
| `시스템복귀` | `sysret` |
| `시스템호출` | `syscall` |
| `영이면` | `jz` |
| `영이면루프` | `loopz` |
| `영확장` | `movzx` |
| `워드를더블로` | `cwd` |
| `이동` | `mov` |
| `인터럽트` | `int` |
| `작으면` | `jl` |
| `점프` | `jmp` |
| `정지` | `hlt` |
| `주소로드` | `lea` |
| `증가` | `inc` |
| `크면` | `jg` |
| `테스트` | `test` |
| `플래그넣기` | `pushf` |
| `플래그빼기` | `popf` |
| `호출` | `call` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Korean / 한국어 (ko)
section .text
global _start

_start:
    이동 rax, 1
    이동 rdi, 1
    이동 rsi, msg
    이동 rdx, 13
    시스템호출

    이동 rax, 60
    이동 rdi, 0
    시스템호출

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ko programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ko programa.masm
```
