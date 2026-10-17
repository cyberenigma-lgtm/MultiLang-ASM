# MultiLang-ASM: Manual de Instrucciones [PT]

**Idioma:** Portuguese / Português (`pt`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 61  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `adicionar` | `add` |
| `carregar_efetivo` | `lea` |
| `chamada_sistema` | `syscall` |
| `chamar` | `call` |
| `comparar` | `cmp` |
| `conv_byte_palavra` | `cbw` |
| `conv_dupla_quad` | `cdq` |
| `conv_palavra_dupla` | `cwd` |
| `copiar` | `mov` |
| `decrementar` | `dec` |
| `desempilhar` | `pop` |
| `desempilhar_flags` | `popf` |
| `deslocar_dir` | `shr` |
| `deslocar_esq` | `shl` |
| `desviar` | `jmp` |
| `dividir` | `div` |
| `dividir_sinal` | `idiv` |
| `e` | `and` |
| `empilhar` | `push` |
| `empilhar_flags` | `pushf` |
| `estender_sinal` | `movsx` |
| `estender_zero` | `movzx` |
| `exclusivo` | `xor` |
| `incrementar` | `inc` |
| `interrupcao` | `int` |
| `mover` | `mov` |
| `multiplicar` | `mul` |
| `multiplicar_sinal` | `imul` |
| `nada` | `nop` |
| `nao` | `not` |
| `negar` | `neg` |
| `ou` | `or` |
| `parar` | `hlt` |
| `retornar` | `ret` |
| `retorno_sistema` | `sysret` |
| `rotacionar_dir` | `ror` |
| `rotacionar_esq` | `rol` |
| `saltar` | `jmp` |
| `se_abaixo` | `jb` |
| `se_abaixo_igual` | `jbe` |
| `se_acima` | `ja` |
| `se_acima_igual` | `jae` |
| `se_cero` | `jz` |
| `se_igual` | `je` |
| `se_maior` | `jg` |
| `se_maior_igual` | `jge` |
| `se_nao_cero` | `jnz` |
| `se_nao_igual` | `jne` |
| `se_nao_paridade` | `jnp` |
| `se_nao_sinal` | `jns` |
| `se_nao_transbordo` | `jno` |
| `se_paridade` | `jp` |
| `se_sinal` | `js` |
| `se_transbordo` | `jo` |
| `si_menor` | `jl` |
| `si_menor_igual` | `jle` |
| `somar` | `add` |
| `subtrair` | `sub` |
| `testar` | `test` |
| `trocar` | `xchg` |
| `voltar` | `ret` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en Portuguese / Português (pt)
section .text
global _start

_start:
    mover rax, 1
    mover rdi, 1
    mover rsi, msg
    mover rdx, 13
    chamada_sistema

    mover rax, 60
    mover rdi, 0
    chamada_sistema

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm pt programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build pt programa.masm
```
