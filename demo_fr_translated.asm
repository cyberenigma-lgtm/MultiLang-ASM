; Programme de test en Français
section .text
global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, message
    mov rdx, 15
    syscall

    mov rax, 60
    mov rdi, 0
    syscall

section .data
    message db "Bonjour monde!", 0xA
