# MultiLang-ASM: Manual de Instrucciones [EN]

**Idioma:** English (`en`)  
**Versión:** 1.0.0 (Estándar Nativo ANSI C99 / UPL+)  
**Mnemónicos soportados:** 224  

---

## 📋 Tabla de Correspondencia (Nativo ↔ NASM)

| Palabra Clave Nativa | Mnemónico NASM Estándar |
| :--- | :--- |
| `add` | `add` |
| `add_with_carry` | `adc` |
| `and` | `and` |
| `and_not` | `andn` |
| `arithmetic_shift_left` | `sal` |
| `arithmetic_shift_right` | `sar` |
| `ascii_adjust_add` | `aaa` |
| `ascii_adjust_div` | `aad` |
| `ascii_adjust_mul` | `aam` |
| `ascii_adjust_sub` | `aas` |
| `bit_invert` | `btc` |
| `bit_reset` | `btr` |
| `bit_scan_forward` | `bsf` |
| `bit_scan_reverse` | `bsr` |
| `bit_set` | `bts` |
| `bit_test` | `bt` |
| `breakpoint` | `int3` |
| `byte_swap` | `bswap` |
| `cache_flush` | `clflush` |
| `call` | `call` |
| `clear_carry` | `clc` |
| `clear_direction` | `cld` |
| `clear_interrupts` | `cli` |
| `compare` | `cmp` |
| `compare_bytes` | `cmpsb` |
| `compare_doublewords` | `cmpsd` |
| `compare_quadwords` | `cmpsq` |
| `compare_words` | `cmpsw` |
| `complement_carry` | `cmc` |
| `convert_byte_word` | `cbw` |
| `convert_double_quad` | `cdq` |
| `convert_double_quad_ext` | `cdqe` |
| `convert_quad_octo` | `cqo` |
| `convert_word_double` | `cwd` |
| `convert_word_double_ext` | `cwde` |
| `copy` | `mov` |
| `cpu_id` | `cpuid` |
| `decimal_adjust_add` | `daa` |
| `decimal_adjust_sub` | `das` |
| `decrement` | `dec` |
| `divide` | `div` |
| `double_shift_left` | `shld` |
| `double_shift_right` | `shrd` |
| `enter_frame` | `enter` |
| `exchange_add` | `xadd` |
| `exclusive_or` | `xor` |
| `fpu_absolute` | `fabs` |
| `fpu_add` | `fadd` |
| `fpu_change_sign` | `fchs` |
| `fpu_clear` | `fclex` |
| `fpu_cos` | `fcos` |
| `fpu_div` | `fdiv` |
| `fpu_init` | `finit` |
| `fpu_load` | `fld` |
| `fpu_mul` | `fmul` |
| `fpu_nop` | `fnop` |
| `fpu_pop` | `fstp` |
| `fpu_sin` | `fsin` |
| `fpu_sqrt` | `fsqrt` |
| `fpu_store` | `fst` |
| `fpu_sub` | `fsub` |
| `halt` | `hlt` |
| `if_above` | `ja` |
| `if_above_equal` | `jae` |
| `if_below` | `jb` |
| `if_below_equal` | `jbe` |
| `if_equal` | `je` |
| `if_greater` | `jg` |
| `if_greater_equal` | `jge` |
| `if_less` | `jl` |
| `if_less_equal` | `jle` |
| `if_not_equal` | `jne` |
| `if_not_overflow` | `jno` |
| `if_not_parity` | `jnp` |
| `if_not_sign` | `jns` |
| `if_not_zero` | `jnz` |
| `if_overflow` | `jo` |
| `if_parity` | `jp` |
| `if_sign` | `js` |
| `if_zero` | `jz` |
| `increment` | `inc` |
| `interrupt` | `int` |
| `interrupt_overflow` | `into` |
| `interrupt_return` | `iret` |
| `interrupt_return_double` | `iretd` |
| `interrupt_return_q` | `iretq` |
| `invalidate_cache` | `invd` |
| `jump` | `jmp` |
| `jump_cx_zero` | `jcxz` |
| `jump_ecx_zero` | `jecxz` |
| `jump_rcx_zero` | `jrcxz` |
| `leading_zeros` | `lzcnt` |
| `leave_frame` | `leave` |
| `load` | `mov` |
| `load_byte` | `lodsb` |
| `load_double` | `lodsd` |
| `load_effective_address` | `lea` |
| `load_fence` | `lfence` |
| `load_flags_ah` | `lahf` |
| `load_gdt` | `lgdt` |
| `load_idt` | `lidt` |
| `load_ldt` | `lldt` |
| `load_quad` | `lodsq` |
| `load_task_register` | `ltr` |
| `load_word` | `lodsw` |
| `loop` | `loop` |
| `loop_if_equal` | `loope` |
| `loop_if_not_equal` | `loopne` |
| `loop_if_not_zero` | `loopnz` |
| `loop_if_zero` | `loopz` |
| `memory_fence` | `mfence` |
| `move` | `mov` |
| `move_byte` | `movsb` |
| `move_double` | `movsd` |
| `move_endian` | `movbe` |
| `move_if_above` | `cmova` |
| `move_if_above_equal` | `cmovae` |
| `move_if_below` | `cmovb` |
| `move_if_below_equal` | `cmovbe` |
| `move_if_equal` | `cmove` |
| `move_if_greater` | `cmovg` |
| `move_if_greater_equal` | `cmovge` |
| `move_if_less` | `cmovl` |
| `move_if_less_equal` | `cmovle` |
| `move_if_not_equal` | `cmovne` |
| `move_if_not_overflow` | `cmovno` |
| `move_if_not_sign` | `cmovns` |
| `move_if_not_zero` | `cmovnz` |
| `move_if_overflow` | `cmovo` |
| `move_if_sign` | `cmovs` |
| `move_if_zero` | `cmovz` |
| `move_quad` | `movsq` |
| `move_word` | `movsw` |
| `multiply` | `mul` |
| `negate` | `neg` |
| `no_operation` | `nop` |
| `not` | `not` |
| `or` | `or` |
| `pause` | `pause` |
| `pop` | `pop` |
| `pop_all` | `popa` |
| `pop_flags` | `popf` |
| `pop_flags_q` | `popfq` |
| `population_count` | `popcnt` |
| `port_in` | `in` |
| `port_in_byte` | `insb` |
| `port_in_double` | `insd` |
| `port_in_word` | `insw` |
| `port_out` | `out` |
| `port_out_byte` | `outsb` |
| `port_out_double` | `outsd` |
| `port_out_word` | `outsw` |
| `push` | `push` |
| `push_all` | `pusha` |
| `push_flags` | `pushf` |
| `push_flags_q` | `pushfq` |
| `read_msr` | `rdmsr` |
| `read_tsc` | `rdtsc` |
| `read_tscp` | `rdtscp` |
| `repeat` | `rep` |
| `repeat_equal` | `repe` |
| `repeat_not_equal` | `repne` |
| `repeat_not_zero` | `repnz` |
| `repeat_zero` | `repz` |
| `resume` | `rsm` |
| `return` | `ret` |
| `rotate_carry_left` | `rcl` |
| `rotate_carry_right` | `rcr` |
| `rotate_left` | `rol` |
| `rotate_right` | `ror` |
| `scan_byte` | `scasb` |
| `scan_double` | `scasd` |
| `scan_quad` | `scasq` |
| `scan_word` | `scasw` |
| `set_carry` | `stc` |
| `set_direction` | `std` |
| `set_if_above` | `seta` |
| `set_if_above_equal` | `setae` |
| `set_if_below` | `setb` |
| `set_if_below_equal` | `setbe` |
| `set_if_carry` | `setc` |
| `set_if_equal` | `sete` |
| `set_if_greater` | `setg` |
| `set_if_greater_equal` | `setge` |
| `set_if_less` | `setl` |
| `set_if_less_equal` | `setle` |
| `set_if_not_carry` | `setnc` |
| `set_if_not_equal` | `setne` |
| `set_if_not_overflow` | `setno` |
| `set_if_not_sign` | `setns` |
| `set_if_not_zero` | `setnz` |
| `set_if_overflow` | `seto` |
| `set_if_parity` | `setp` |
| `set_if_sign` | `sets` |
| `set_if_zero` | `setz` |
| `set_interrupts` | `sti` |
| `shift_left` | `shl` |
| `shift_right` | `shr` |
| `sign_extend` | `movsx` |
| `signed_divide` | `idiv` |
| `signed_multiply` | `imul` |
| `store_ah_flags` | `sahf` |
| `store_byte` | `stosb` |
| `store_double` | `stosd` |
| `store_fence` | `sfence` |
| `store_gdt` | `sgdt` |
| `store_idt` | `sidt` |
| `store_ldt` | `sldt` |
| `store_quad` | `stosq` |
| `store_task_register` | `str` |
| `store_word` | `stosw` |
| `sub_with_borrow` | `sbb` |
| `subtract` | `sub` |
| `swap` | `xchg` |
| `syscall` | `syscall` |
| `sysenter` | `sysenter` |
| `sysexit` | `sysexit` |
| `sysret` | `sysret` |
| `test` | `test` |
| `trailing_zeros` | `tzcnt` |
| `wait` | `wait` |
| `write_msr` | `wrmsr` |
| `writeback_invalidate_cache` | `wbinvd` |
| `zero_extend` | `movzx` |

---

## 💻 Ejemplo de Uso Rápido

```asm
; Ejemplo en English (en)
section .text
global _start

_start:
    move rax, 1
    move rdi, 1
    move rsi, msg
    move rdx, 13
    syscall

    move rax, 60
    move rdi, 0
    syscall

section .data
    msg db "Hello World!", 0xA
```

## 🛠️ Compilación con Motor Nativo C99

```bash
# Transpilar a NASM estándar:
mlasm en programa.masm -o programa.asm

# Auto-detección del idioma:
mlasm auto programa.masm -o programa.asm

# Compilar directo a binario ejecutable (.exe):
mlasm --build en programa.masm
```
