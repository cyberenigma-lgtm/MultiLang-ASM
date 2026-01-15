; ============================================================
; DEMO PORTUGUÊS-BR (MultiLang-ASM)
; Exemplo de função de soma em linguagem natural
; ============================================================

funcao_somar:
    push    rbp         ; Guardar base da pilha
    mov       rbp, rsp    ; Nova base
    
    add       rdi, rsi    ; Somar argumentos
    mov       rax, rdi    ; Resultado em RAX
    
    pop rbp         ; Restaurar base
    ret                ; Voltar ao fluxo principal

principal:
    cli     ; cli
    mov       rdi, 10
    mov       rsi, 20
    call      funcao_somar
    hlt                   ; hlt
