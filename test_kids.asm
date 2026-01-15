; Kids Mode Test (Spanish)
; Should detect as ES/Kids and compile to MOV, ADD, SUB, SYSCALL

mov rax 10
add rax 5
sub rax 2
syscall rax
