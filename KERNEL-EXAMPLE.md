# 🛡️ Crear un Kernel desde Cero con MultiLang-ASM

Ejemplo completo de cómo crear un kernel mínimo en **50 líneas** usando MultiLang-ASM en Español.

---

## 📦 Archivos del Proyecto

```
mi-kernel/
├── mlasm.py              # Copiado del proyecto
├── boot.masm             # Bootloader en español
├── kernel.masm           # Kernel en español
├── linker.ld             # Linker script
└── Makefile              # Automatización
```

---

## 🚀 Paso 1: Bootloader (boot.masm)

**boot.masm** - 16 líneas en Español:

```asm
; boot.masm - Bootloader en Español
[bits 16]
[org 0x7C00]

inicio:
    ; Limpiar segmentos
    mover ax, 0
    mover ds, ax
    mover es, ax
    mover ss, ax
    mover sp, 0x7C00
    
    ; Cargar kernel en 0x1000
    mover ah, 0x02          ; función leer
    mover al, 10            ; 10 sectores
    mover ch, 0             ; cilindro 0
    mover cl, 2             ; sector 2
    mover dh, 0             ; cabeza 0
    mover bx, 0x1000        ; destino
    interrupcion 0x13       ; BIOS disk
    
    ; Saltar al kernel
    saltar 0x1000
    
; Firma de boot
times 510-($-$$) db 0
dw 0xAA55
```

---

## 💻 Paso 2: Kernel (kernel.masm)

**kernel.masm** - 34 líneas en Español:

```asm
; kernel.masm - Kernel Minimalista en Español
[bits 16]
[org 0x1000]

inicio_kernel:
    ; Limpiar pantalla
    mover ah, 0x00
    mover al, 0x03
    interrupcion 0x10
    
    ; Imprimir mensaje
    mover si, mensaje
    llamar imprimir
    
    ; Loop infinito
bucle_infinito:
    detener
    saltar bucle_infinito

; Función: Imprimir cadena
; Entrada: SI = puntero a cadena
imprimir:
    meter ax
    meter bx
    
.ciclo:
    cargar_byte                 ; al = [si], si++
    comparar al, 0
    si_igual .fin
    
    mover ah, 0x0E
    mover bx, 0x07
    interrupcion 0x10
    saltar .ciclo
    
.fin:
    sacar bx
    sacar ax
    retornar

; Datos
mensaje db '¡Kernel en Español funcionando!', 0

; Rellenar hasta 5KB (10 sectores)
times 5120-($-$$) db 0
```

---

## 🔗 Paso 3: Linker Script (linker.ld)

```ld
OUTPUT_FORMAT(binary)
ENTRY(inicio_kernel)

SECTIONS
{
    . = 0x1000;
    .text : { *(.text) }
    .data : { *(.data) }
    .bss  : { *(.bss) }
}
```

---

## ⚙️ Paso 4: Makefile

```makefile
# Makefile para kernel en Español
MLASM = python mlasm.py
NASM = nasm
DD = dd

all: kernel.img

# Traducir bootloader
boot.asm: boot.masm
	$(MLASM) es $< $@

# Traducir kernel
kernel.asm: kernel.masm
	$(MLASM) es $< $@

# Compilar bootloader
boot.bin: boot.asm
	$(NASM) -f bin $< -o $@

# Compilar kernel
kernel.bin: kernel.asm
	$(NASM) -f bin $< -o $@

# Crear imagen de disco
kernel.img: boot.bin kernel.bin
	$(DD) if=/dev/zero of=kernel.img bs=512 count=2880
	$(DD) if=boot.bin of=kernel.img conv=notrunc
	$(DD) if=kernel.bin of=kernel.img seek=1 conv=notrunc

# Ejecutar en QEMU
run: kernel.img
	qemu-system-x86_64 -drive file=kernel.img,format=raw

clean:
	rm -f *.asm *.bin kernel.img

.PHONY: all run clean
```

---

## 🏗️ Paso 5: Compilar y Ejecutar

### Compilación Completa

```bash
# Copiar MultiLang-ASM
cp /path/to/mlasm.py .

# Compilar todo
make

# Ejecutar en QEMU
make run
```

### Paso a Paso (Manual)

```bash
# 1. Traducir código español → NASM
python mlasm.py es boot.masm boot.asm
python mlasm.py es kernel.masm kernel.asm

# 2. Compilar a binario
nasm -f bin boot.asm -o boot.bin
nasm -f bin kernel.asm -o kernel.bin

# 3. Crear imagen de disco
dd if=/dev/zero of=kernel.img bs=512 count=2880
dd if=boot.bin of=kernel.img conv=notrunc
dd if=kernel.bin of=kernel.img seek=1 conv=notrunc

# 4. Ejecutar
qemu-system-x86_64 -drive file=kernel.img,format=raw
```

---

## 🎯 Resultado Esperado

Al ejecutar `make run`, verás:

```
┌─────────────────────────────────┐
│                                 │
│ ¡Kernel en Español funcionando! │
│                                 │
│                                 │
└─────────────────────────────────┘
```

---

## 📊 Análisis del Código

### Líneas de Código

| Archivo | Líneas | Idioma |
|---------|--------|--------|
| boot.masm | 16 | Español |
| kernel.masm | 34 | Español |
| **Total** | **50** | **100% Español** |

### Instrucciones Usadas (en Español)

- `mover` (mov) - Movimiento de datos
- `saltar` (jmp) - Saltos incondicionales
- `comparar` (cmp) - Comparaciones
- `si_igual` (je) - Salto condicional
- `llamar` (call) - Llamada a función
- `retornar` (ret) - Retorno de función
- `meter` (push) - Push a pila
- `sacar` (pop) - Pop de pila
- `interrupcion` (int) - Interrupciones BIOS
- `detener` (hlt) - Detener CPU
- `cargar_byte` (lodsb) - Cargar byte

---

## 🔍 Cómo Funciona

### Bootloader
1. BIOS carga los primeros 512 bytes en `0x7C00`
2. Bootloader configura segmentos
3. Lee 10 sectores del disco a `0x1000` (kernel)
4. Salta a `0x1000` para ejecutar kernel

### Kernel
1. Limpia la pantalla (INT 10h, AH=00h)
2. Imprime mensaje carácter por carácter (INT 10h, AH=0Eh)
3. Entra en loop infinito con `hlt`

---

## 🌍 Versiones en Otros Idiomas

### Francés
```asm
; Cambia "mover" → "deplacer"
deplacer ax, 0
deplacer ds, ax
appeler imprimer
```

### Alemán
```asm
; Cambia "mover" → "bewegen"
bewegen ax, 0
bewegen ds, ax
rufen drucken
```

### Japonés
```asm
; Cambia "mover" → "移動"
移動 ax, 0
移動 ds, ax
呼出 印刷
```

**Solo cambia el código, todo lo demás igual.**

---

## 🚀 Próximos Pasos

### Expandir el Kernel

1. **Modo Protegido (32-bit)**
```asm
; Activar A20
; Cargar GDT
; Cambiar a modo protegido
```

2. **Drivers Básicos**
```asm
; Driver de teclado
; Driver de timer
; Driver VGA
```

3. **Sistema de Archivos**
```asm
; FAT12/FAT16
; Leer/escribir archivos
```

---

## 📚 Recursos

- [OSDev Wiki](https://wiki.osdev.org/) - Documentación técnica
- [MultiLang-ASM Docs](https://github.com/cyberenigma-lgtm/MultiLang-ASM/tree/main/docs) - Referencias
- [NASM Manual](https://nasm.us/doc/) - Sintaxis ASM

---

## 💡 Ventajas de MultiLang-ASM

### Antes (Inglés)
```asm
mov ax, 0
mov ds, ax
call print
jmp loop
```

### Ahora (Tu Idioma)
```asm
mover ax, 0
mover ds, ax
llamar imprimir
saltar bucle
```

**Misma funcionalidad, código más natural.**

---

## 🎓 Ejercicios

1. **Cambiar el mensaje** - Modifica `mensaje` en kernel.masm
2. **Agregar colores** - Usa BH para color de texto
3. **Múltiples líneas** - Imprime varias cadenas
4. **Entrada de teclado** - Lee teclas con INT 16h
5. **Modo gráfico** - Cambia a modo VGA 13h

---

## 📧 ¿Dudas?

- **Email:** neuro.so.ia.sim@gmail.com
- **Wiki:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/wiki
- **Issues:** https://github.com/cyberenigma-lgtm/MultiLang-ASM/issues

---

**¡Acabas de crear un kernel en tu idioma nativo!** 🛡️✨

**Versión:** v0.3  
**Fecha:** 2025-12-25
