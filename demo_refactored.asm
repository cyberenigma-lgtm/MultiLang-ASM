; 🛡️ PROGRAMA DE PRUEBA: MultiLang-ASM (Español)
; Este código será traducido a NASM estándar

seccion .texto
global _inicio

_inicio:
    mov rax, 1          ; syscall write
    mov rdi, 1          ; stdout
    mov rsi, mensaje    ; direccion del mensaje
    mov rdx, 14         ; longitud
    int 0x80     ; llamar al kernel

    mov rax, 60         ; syscall exit
    mov rdi, 0          ; codigo de salida
    int 0x80

seccion .datos
    mensaje db "Hola Mundo!", 0xA
