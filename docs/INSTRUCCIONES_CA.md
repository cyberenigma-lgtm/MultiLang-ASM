# MultiLang-ASM: Instruccions (Català - ca)

Benvingut al suport català per a MultiLang-ASM.

## 🛠 Comandes Bàsiques

| MultiLang-ASM | NASM (x86_64) | Descripció |
| :--- | :--- | :--- |
| `moure` | `mov` | Moure dades |
| `sumar` | `add` | Sumar valors |
| `restar` | `sub` | Restar valors |
| `comparar` | `cmp` | Comparar valors |
| `saltar` | `jmp` | Salt a una adreça |
| `cridar` | `call` | Cridar una funció |
| `retornar` | `ret` | Retorn de funció |
| `interrupció` | `int` | Interrupció de programari |
| `crida_sistema` | `syscall` | Crida al nucli |

## 📝 Exemple de Codi

```asm
; Hola món en català
secció .data
    missatge: db "Hola mon!", 10

secció .text
    global _start

_start:
    moure rax, 1          ; syscall: write
    moure rdi, 1          ; fd: stdout
    moure rsi, missatge   ; buffer
    moure rdx, 10         ; length
    crida_sistema

    moure rax, 60         ; syscall: exit
    moure rdi, 0          ; codi d'error
    crida_sistema
```

## 🚀 Ús

```bash
python mlasm.py ca programa.masm
```
