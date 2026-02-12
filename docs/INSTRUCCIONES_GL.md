# MultiLang-ASM: Instrucións (Galego - gl)

Benvido ao soporte galego para MultiLang-ASM.

## 🛠 Comandos Básicos

| MultiLang-ASM | NASM (x86_64) | Descrición |
| :--- | :--- | :--- |
| `mover` | `mov` | Mover datos |
| `sumar` | `add` | Sumar valores |
| `restar` | `sub` | Restar valores |
| `comparar` | `cmp` | Comparar valores |
| `saltar` | `jmp` | Salto a unha dirección |
| `chamar` | `call` | Chamar unha función |
| `retornar` | `ret` | Retorno de función |
| `interrupción` | `int` | Interrupción de software |
| `chamada_sistema` | `syscall` | Chamada ao sistema |

## 📝 Exemplo de Códido

```asm
; Ola mundo en galego
sección .data
    mensaxe: db "Ola mundo!", 10

sección .text
    global _start

_start:
    mover rax, 1          ; syscall: write
    mover rdi, 1          ; fd: stdout
    mover rsi, mensaxe    ; buffer
    mover rdx, 11         ; length
    chamada_sistema

    mover rax, 60         ; syscall: exit
    mover rdi, 0          ; código de erro
    chamada_sistema
```

## 🚀 Uso

```bash
python mlasm.py gl programa.masm
```
