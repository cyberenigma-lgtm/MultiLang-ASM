# Makefile para Kernel en Español
# Usa MultiLang-ASM para traducir código

MLASM = python ../mlasm.py
NASM = nasm
DD = dd
QEMU = qemu-system-x86_64

all: kernel.img

# Traducir bootloader de español a NASM
boot.asm: boot.masm
	@echo "Traduciendo bootloader (español -> NASM)..."
	$(MLASM) es $< $@

# Traducir kernel de español a NASM
kernel.asm: kernel.masm
	@echo "Traduciendo kernel (español -> NASM)..."
	$(MLASM) es $< $@

# Compilar bootloader a binario
boot.bin: boot.asm
	@echo "Compilando bootloader..."
	$(NASM) -f bin $< -o $@

# Compilar kernel a binario
kernel.bin: kernel.asm
	@echo "Compilando kernel..."
	$(NASM) -f bin $< -o $@

# Crear imagen de disco
kernel.img: boot.bin kernel.bin
	@echo "Creando imagen de disco..."
	$(DD) if=/dev/zero of=kernel.img bs=512 count=2880 status=none
	$(DD) if=boot.bin of=kernel.img conv=notrunc status=none
	$(DD) if=kernel.bin of=kernel.img seek=1 conv=notrunc status=none
	@echo "Imagen creada: kernel.img"

# Ejecutar en QEMU
run: kernel.img
	@echo "Ejecutando en QEMU..."
	$(QEMU) -drive file=kernel.img,format=raw

# Limpiar archivos generados
clean:
	rm -f *.asm *.bin kernel.img
	@echo "Archivos limpiados"

# Debug: Mostrar código traducido
debug: boot.asm kernel.asm
	@echo "=== BOOTLOADER (NASM) ==="
	@head -20 boot.asm
	@echo ""
	@echo "=== KERNEL (NASM) ==="
	@head -20 kernel.asm

.PHONY: all run clean debug
