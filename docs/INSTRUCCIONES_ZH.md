# MultiLang-ASM: Manual de Instrucciones [ZH]

**Idioma:** Chinese / 中文 (`zh`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 41  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `中斷` | `int` |
| `乘` | `mul` |
| `交換` | `xchg` |
| `位元組轉字` | `cbw` |
| `儲存位元組` | `stosb` |
| `加` | `add` |
| `呼叫` | `call` |
| `字轉雙字` | `cwd` |
| `彈出` | `pop` |
| `彈出旗標` | `popf` |
| `推入` | `push` |
| `推入旗標` | `pushf` |
| `暫停` | `hlt` |
| `比較` | `cmp` |
| `求反` | `neg` |
| `減` | `sub` |
| `測試` | `test` |
| `無操作` | `nop` |
| `移動` | `mov` |
| `移動位元組` | `movsb` |
| `符號擴充` | `movsx` |
| `系統呼叫` | `syscall` |
| `系統返回` | `sysret` |
| `若不等` | `jne` |
| `若大於` | `jg` |
| `若小於` | `jl` |
| `若為零` | `jz` |
| `若為零迴圈` | `loopz` |
| `若相等` | `je` |
| `複製` | `mov` |
| `跳躍` | `jmp` |
| `載入位元組` | `lodsb` |
| `載入有效位址` | `lea` |
| `返回` | `ret` |
| `迴圈` | `loop` |
| `遞增` | `inc` |
| `遞減` | `dec` |
| `重複` | `rep` |
| `除` | `div` |
| `雙字轉四字` | `cdq` |
| `零擴充` | `movzx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Chinese / 中文 (zh)
section .text
global _start

_start:
    移動 rax, 1
    移動 rdi, 1
    移動 rsi, msg
    移動 rdx, 13
    系統呼叫

    移動 rax, 60
    移動 rdi, 0
    系統呼叫

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm zh programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build zh programa.masm
```
