# Code Examples

Complete code examples in all 10 supported languages.

---

## 🇪🇸 Spanish Example

### Hello World
```asm
; hello.masm
seccion .datos
    mensaje db 'Hola Mundo!', 0xA
    longitud equ $ - mensaje

seccion .texto
global _inicio

_inicio:
    ; write(1, mensaje, longitud)
    mover rax, 1
    mover rdi, 1
    mover rsi, mensaje
    mover rdx, longitud
    llamada_sistema
    
    ; exit(0)
    mover rax, 60
    mover rdi, 0
    llamada_sistema
```

**Usage:**
```bash
python mlasm.py es hello.masm hello.asm
nasm -f elf64 hello.asm
ld hello.o -o hello
./hello
```

---

## 🇫🇷 French Example

### Arithmetic Operations
```asm
; calcul.masm
seccion .texto
global _debut

_debut:
    deplacer rax, 10        ; rax = 10
    deplacer rbx, 5         ; rbx = 5
    
    ajouter rax, rbx        ; rax = rax + rbx (15)
    soustraire rax, 3       ; rax = rax - 3 (12)
    multiplier rbx          ; rax = rax * rbx
    
    deplacer rdi, rax       ; exit code = rax
    deplacer rax, 60        ; syscall exit
    appel_systeme
```

---

## 🇩🇪 German Example

### Simple Loop
```asm
; schleife.masm
seccion .texto
global _start

_start:
    bewegen rcx, 10         ; counter = 10

schleife_anfang:
    addieren rax, rcx       ; rax += rcx
    dekrementieren rcx      ; rcx--
    wenn_nicht_null schleife_anfang
    
    bewegen rdi, rax
    bewegen rax, 60
    unterbrechung 0x80
```

---

## 🇮🇹 Italian Example

### Function Call
```asm
; funzione.masm
seccion .texto
global _inizio

_inizio:
    spostare rdi, 5
    chiamare calcola_quadrato
    
    spostare rdi, rax
    spostare rax, 60
    interruzione 0x80

calcola_quadrato:
    spingere rbp
    spostare rbp, rsp
    
    spostare rax, rdi
    moltiplicare rdi
    
    spostare rsp, rbp
    estrarre rbp
    ritornare
```

---

## 🇸🇦 Arabic Example

### Conditional Jump
```asm
; شرط.masm
القسم .نص
عام _بداية

_بداية:
    نقل rax, 10
    نقل rbx, 20
    
    مقارنة rax, rbx
    إذا_يساوي متساوية
    إذا_لا_يساوي غير_متساوية

متساوية:
    نقل rdi, 1
    اقفز نهاية

غير_متساوية:
    نقل rdi, 0

نهاية:
    نقل rax, 60
    مقاطعة 0x80
```

---

## 🇷🇺 Russian Example

### Stack Operations
```asm
; стек.masm
секция .текст
global _начало

_начало:
    перенести rax, 10
    перенести rbx, 20
    
    положить rax             ; push rax
    положить rbx             ; push rbx
    
    извлечь rcx              ; pop -> rcx (20)
    извлечь rdx              ; pop -> rdx (10)
    
    добавить rcx, rdx        ; rcx = 30
    
    перенести rdi, rcx
    перенести rax, 60
    прерывание 0x80
```

---

## 🇰🇷 Korean Example

### Register Operations
```asm
; 레지스터.masm
섹션 .텍스트
global _시작

_시작:
    이동 rax, 100
    이동 rbx, 50
    
    더하기 rax, rbx          ; rax = 150
    빼기 rax, 25             ; rax = 125
    
    이동 rdi, rax
    이동 rax, 60
    인터럽트 0x80
```

---

## 🇮🇩 Indonesian Example

### Comparison
```asm
; perbandingan.masm
bagian .teks
global _mulai

_mulai:
    pindah rax, 15
    pindah rbx, 15
    
    bandingkan rax, rbx
    jika_sama sama
    lompat tidak_sama

sama:
    pindah rdi, 1
    lompat selesai

tidak_sama:
    pindah rdi, 0

selesai:
    pindah rax, 60
    interupsi 0x80
```

---

## 🇨🇳 Chinese Example

### Array Access
```asm
; 数组.masm
区段 .数据
    数组 dq 10, 20, 30, 40, 50

区段 .代码
global _开始

_开始:
    载入有效位址 rsi, [数组]
    移動 rax, [rsi]          ; rax = 10
    移動 rbx, [rsi + 8]      ; rbx = 20
    移動 rcx, [rsi + 16]     ; rcx = 30
    
    加 rax, rbx
    加 rax, rcx              ; rax = 60
    
    移動 rdi, rax
    移動 rax, 60
    中斷 0x80
```

---

## 🇯🇵 Japanese Example

### System Call
```asm
; システムコール.masm
セクション .データ
    文字列 db 'こんにちは', 0xA
    長さ equ $ - 文字列

セクション .コード
global _開始

_開始:
    ; write(1, 文字列, 長さ)
    移動 rax, 1
    移動 rdi, 1
    実効アドレス読込 rsi, [文字列]
    移動 rdx, 長さ
    システムコール
    
    ; exit(0)
    移動 rax, 60
    移動 rdi, 0
    システムコール
```

---

## 🔄 Reverse Mode Examples

### View NASM in Your Language

**Standard NASM code:**
```asm
mov rax, 1
add rbx, 10
jmp loop_start
call function
ret
```

**View in Spanish:**
```bash
python mlasm.py es code.asm code_es.masm --reverse
```

**Result:**
```asm
mover rax, 1
sumar rbx, 10
saltar loop_start
llamar function
retornar
```

---

## 📚 More Examples

### Complete Projects

1. **Simple Bootloader** (Spanish)
   - Location: `examples/bootloader_es.masm`
   - 512-byte bootloader example

2. **Calculator** (French)
   - Location: `examples/calculat rice_fr.masm`
   - Basic arithmetic operations

3. **String Operations** (German)
   - Location: `examples/string_de.masm`
   - String manipulation in assembly

---

## 🧪 Testing Examples

To test any example:

```bash
# 1. Translate
python mlasm.py <lang> example.masm example.asm

# 2. Assemble
nasm -f elf64 example.asm

# 3. Link
ld example.o -o example

# 4. Run
./example
```

---

## 💡 Tips

- Start with simple examples (Hello World)
- Test incrementally
- Use comments extensively
- Verify with reverse mode
- Compare with standard NASM

---

**See Also:**
- [How to Use](How-to-Use) - Basic usage
- [Supported Languages](Supported-Languages) - Language list
- [PRETTY Mode](PRETTY-Mode) - Reverse translation
