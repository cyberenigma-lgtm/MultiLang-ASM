# MultiLang-ASM: Manual de Instrucciones [JA]

**Idioma:** Japanese / 日本語 (`ja`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 41  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `より大きければ` | `jg` |
| `より小さければ` | `jl` |
| `インクリメント` | `inc` |
| `コピー` | `mov` |
| `システムコール` | `syscall` |
| `システム帰還` | `sysret` |
| `ジャンプ` | `jmp` |
| `ゼロならば` | `jz` |
| `ゼロならばループ` | `loopz` |
| `ゼロ拡張` | `movzx` |
| `ダブルをクアッドへ` | `cdq` |
| `テスト` | `test` |
| `デクリメント` | `dec` |
| `バイトをワードへ` | `cbw` |
| `バイト格納` | `stosb` |
| `バイト移動` | `movsb` |
| `バイト読込` | `lodsb` |
| `フラグ保存` | `pushf` |
| `フラグ復元` | `popf` |
| `プッシュ` | `push` |
| `ポップ` | `pop` |
| `ループ` | `loop` |
| `ワードをダブルへ` | `cwd` |
| `乗算` | `mul` |
| `交換` | `xchg` |
| `何もしない` | `nop` |
| `停止` | `hlt` |
| `割込` | `int` |
| `加算` | `add` |
| `否定` | `neg` |
| `呼出` | `call` |
| `実効アドレス読込` | `lea` |
| `戻る` | `ret` |
| `比較` | `cmp` |
| `減算` | `sub` |
| `移動` | `mov` |
| `符号拡張` | `movsx` |
| `等しくなければ` | `jne` |
| `等しければ` | `je` |
| `繰返` | `rep` |
| `除算` | `div` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Japanese / 日本語 (ja)
section .text
global _start

_start:
    移動 rax, 1
    移動 rdi, 1
    移動 rsi, msg
    移動 rdx, 13
    システムコール

    移動 rax, 60
    移動 rdi, 0
    システムコール

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm ja programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build ja programa.masm
```
