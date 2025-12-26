# 📚 Guia Completo de Referência — Português-BR (MultiLang-ASM)

Este guia contém todas as instruções em português para o montador multilíngue **MultiLang-ASM**, parte do ecossistema **Neuro-OS.es**.

> O MultiLang-ASM permite escrever código assembly em uma linguagem nativa e gerar ASM padrão compatível com NASM/FASM/GAS.

---

## 🎨 Projeto em Linguagem Aportuguesada

O design das instruções em português no MultiLang-ASM segue princípios específicos:

### Filosofia de Projeto

**1. Naturalidade em vez de Literalidade**
- Não traduziremos palavra por palavra do inglês.
- Usaremos termos que soarão mais naturais para um falante de português.
- Exemplo: `desviar` soa mais natural do que `ir` ou `saltar`.

**2. Clareza em vez de concisão**
- Prefere-se `comparar` a `comp` porque é mais claro
- Abreviações estarão disponíveis, mas não serão obrigatórias
- O programador poderá escolher: `mover` ou `mov` - ambos funcionarão

**3. Consistência Linguística**
- Serão usados infinitivos verbais: `add`, `subtract`, `compare`
- Será mantida a consistência entre as famílias de instruções
- Os nomes são previsíveis: se `add` existir, então `subtract` existirá

**4. Compatibilidade Universal**
- **Todas as instruções em inglês ainda funcionarão**
- Você poderá misturar: `move rax, rbx` e `push rcx` no mesmo código
- O montador é agnóstico: ele traduzirá o que precisar e ignorará o que já for padrão

**5. Múltiplos Aliases**
- `move`   = `mov` = `copy`
- `return` = `ret` = `return`
- Isso permitirá estilos de código personalizados

### Por que não é simplesmente "Tradução"?

Este não é um dicionário inglês-português aplicado cegamente. 
É um **design de linguagem** com o objetivo de:
- Soar natural quando lido em voz alta
- Ser intuitivo para alguém que nunca viu ASM
- Respeitar as convenções da CPU sem causar confusão

**Exemplo:**
```asm
; Versão natural em português
mover    rax, 10
comparar rax, 5
se_maior rotulo_positivo
saltar   fim

; Versão mista (igualmente válida)
mov      rax, 10
comparar rax, 5
jg       rotulo_positivo
jmp      fim
```

Ambas estão corretas. O programador pode escolher seu estilo.

---

## 📦 Movimentação de Dados

| Português | ASM | Descrição |
|-----------|-----|-------------|
| `mover`, `copiar` | `mov` | Mover dados entre registradores/memória |
| `trocar` | `xchg` | Trocar valores entre operandos |
| `carregar_efetivo` | `lea` | Carregar endereço efetivo |
| `estender_zero`  | `movzx` | Mover com extensão de zeros |
| `estender_sinal` | `movsx` | Mover con extensão de sinal |

---

## ➕ Aritmética

| Português | ASM | Descrição |
|-----------|-----|-------------|
| `somar`, `adicionar` | `add` | Somar dois operandos |
| `subtrair` | `sub` | Subtrair dois operandos |
| `multiplicar` | `mul` | Multiplicação sem sinal |
| `multiplicar_sinal` | `imul` | Multiplicação com sinal |
| `dividir` | `div` | Divisão sem signal |
| `dividir_sinal` | `idiv` | Divisão com sinal |
| `incrementar` | `inc` | Incrementar de 1 |
| `decrementar` | `dec` | Decrementar de 1 |
| `negar` | `neg` | Negar (complemento de 2) |

---

## 🔢 Operações Lógicas

| Português | ASM | Descrição |
|---------|-----|-------------|
| `e` | `and` | AND lógico bit a bit |
| `ou` | `or` | OR lógico bit a bit |
| `nao` | `not` | NOT lógico (complemento de 1) |
| `exclusivo` | `xor` | XOR lógico bit a bit |
| `deslocar_esq` | `shl`, `sal` | Deslocamento lógico/aritmético esq. |
| `deslocar_dir` | `shr`, `sar` | Deslocamento lógico/aritmético dir. |
| `rotacionar_esq` | `rol` | Rotação para a esquerda |
| `rotacionar_dir` | `ror` | Rotação para a direita  |

---

## 🔍 Comparação e teste

| Português | ASM | Descrição |
|---------|-----|-------------|
| `comparar` | `cmp` | Comparar dois operandos |
| `testar` | `test` | AND lógico sem guardar o resultado |

---

## 🎯 Control de Fluxo

### Saltos Incondicionais

| Português | ASM | Descrição |
|---------|-----|-------------|
| `desviar` | `jmp` | Desviar incondicional |
| `chamar` | `call` | Chamar subrotina |
| `retornar`, `voltar` | `ret` | Retornar de subrotina |

### Saltos Condicionais

| Português | ASM | Descrição |
|---------|-----|-------------|
| `se_igual` | `je`, `jz` | Desviar se igual / se zero |
| `se_nao_igual` | `jne`, `jnz` | Desviar se não igual / se não zero |
| `se_maior` | `jg` | Desviar se maior (com sinal) |
| `se_maior_igual` | `jge` | Desviar se maior ou igual (sinal) |
| `se_menor` | `jl` | Desviar se menor (sinal) |
| `se_menor_igual` | `jle` | Desviar se menor ou igual (sinal) |
| `se_acima` | `ja` | Desviar se acima (sem signal) |
| `se_abaixo` | `jb` | Desviar se abaixo (sem sinal) |
| `se_acima_igual` | `jae` | Desviar se acima ou igual (sem sinal) |
| `se_abaixo_igual` | `jbe` | Desviar se abaixo ou igual (sem sinal) |
| `se_sinal" | `js` | Desviar se o bit de sinal estiver ativado |
| `se_nao_sinal` | `jns` | Desviar se o bit de sinal não estiver ativado |
| `se_transbordo` | `jo` | Desviar se houve transbordamento |
| `se_nao_transbordo` | `jno` | Desviar se não houve transbordamento |
| `se_paridade` | `jp` | Desviar se paridade par |
| `se_nao_paridade` | `jnp` | Desviar se paridade ímpar |

---

## 📚 Pilha (Stack)

| Português | ASM | Descrição |
|---------|-----|-------------|
| `empilhar` | `push` | Inserir valor na pilha |
| `desempilhar` | `pop` | Remover valor da pilha |
| `empilhar_flags` | `pushf` | Inserir registrador com flags |
| `desempilhar_flags` | `popf` | Remover registrador com flags |

---

## 🔤 Operações sobre sequências

| Português | ASM | Descrição |
|---------|-----|-------------|
| `mover_byte` | `movsb` | Mover byte em sequência |
| `mover_palavra` | `movsw` | Mover palavra em sequência |
| `mover_dupla` | `movsd` | Mover palavra dupla em sequência |
| `armazenar_byte` | `stosb` | Armazenar byte em sequência |
| `cargar_byte` | `lodsb` | Carregar byte em sequência |
| `escanear_byte" | `scasb` | Escanear byte em sequência |
| `repetir` | `rep` | Repetir operação |
| `repetir_enquanto` | `repne` | Repetir enquanto não for igual |

---

## 🔁 Repetições

| Português | ASM | Descrição |
|---------|-----|-------------|
| `repetir` | `loop` | Decrementar RCX e deviar se RCX ≠ 0 |
| `repetir_se_zero` | `loopz` | Loop se zero flag estiver ativado |
| `repetir_se_nao_zero` | `loopnz` | Loop se zero flag não estiver ativado |

---

## ⚙️ Sistema

| Português | ASM | Descrição |
|---------|-----|-------------|
| `interrupcao` | `int` | Chamar interrupção de software |
| `chamada_sistema` | `syscall` | Chamada ao sistema (x86_64) |
| `retorno_sistema` | `sysret` | Retorno de chamada ao sistema |
| `retorno_interrupcao` | `iret` | Retorno de interrupção |

---

## 🛠️ Miscelânea

| Português | ASM | Descrição |
|---------|-----|-------------|
| `nada` | `nop` | Não fazer nada |
| `parar` | `hlt` | Parar CPU até próxima interrupção |
| `limpar_interrupcoes` | `cli` | Desabilitar interrupções |
| `ativar_interrupcoes` | `sti` | Habilitar interrupções |
| `limpar_direcao` | `cld` | Limpar flag de direção |
| `fixar_direcao` | `std` | Fixar flag de direção |
| `esperar` | `wait` | Esperar operação de coprocessador |

---

## 🔄 Conversão de Tamanhos

| Português | ASM | Descrição |
|---------|-----|-------------|
| `converter_byte_palavra` | `cbw` | Converter byte para palavra |
| `converter_palavra_dupla` | `cwd` | Converter palavra para palavra dupla |
| `converter_dupla_quadrupla` | `cdq` | Converter palavra dupla para quádrupla |
| `converter_quadrupla_octupla" | `cqo` | Converter quádrupla para óctupla |

---

## 📝 Exemplo de Uso

```asm
; Funcão para somar dois números
funcao_somar:
    empilhar    rbp         ; push rbp
    mover       rbp, rsp    ; mov rbp, rsp
    
    somar       rdi, rsi    ; add rdi, rsi
    mover       rax, rdi    ; mov rax, rdi
    
    desempilhar rbp         ; pop rbp
    retornar                ; ret
```

> [!TIP]
> Todas as instruções padrões em inglês (mov, add, jmp, etc.) também funcionarão diretamente sem tradução.

---

## 🔬 Exemplos Funcionais Detalhados

### 1. Programa "Olá Mundo" (Linux x86_64)

```asm
; Arquivo: ola.masm
secao .dados
    mensagem db "Olá do Neuro-OS!", 0xA
    tamanho  equ $ - mensagem

secao .texto
    global _inicio

_inicio:
    ; syscall write(1, mensagem, tamanho)
    mover   rax, 1          ; mover rax, 1
    mover   rdi, 1          ; mover rdi, 1
    mover   rsi, mensagem
    mover   rdx, tamanho
    chamada_sistema         ; syscall

    ; syscall exit(0)
    mover   rax, 60
    exclusivo rdi, rdi      ; xor rdi, rdi (zero)
    chamada_sistema
```

### 2. Manipulação de Pilha e Fluxo

```asm
verificar_valor:
    comparar    rdi, 10
    se_maior    e_maior
    mover       rax, 0
    retornar

e_maior:
    mover       rax, 1
    retornar
```

---

## 🛠️ Como usar o Tradutor

Para converter seu código "aportuguesado" em ASM padrão pronto para o **nasm**:

```bash
python mlasm.py pt seu_arquivo.masm seu_arquivo.asm
```

O arquivo resultante (`seu_arquivo.asm`) usará os mnemônicos padrão do Intel x86_64, mas manterá todos os seus comentários originais.

---
**MultiLang-ASM** — Parte do ecossistema **Neuro-OS.es**.
