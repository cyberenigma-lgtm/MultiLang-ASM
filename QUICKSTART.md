# ⚡ Guía de Inicio Rápido - MultiLang-ASM

## 🎯 Flujo de Trabajo Ultra-Rápido

### Opción 1: Uso Directo (1 comando)

```bash
# Escribir en tu idioma -> Compilar -> Ejecutar
python mlasm.py es mi_programa.masm programa.asm && nasm -f elf64 programa.asm && ld programa.o -o programa && ./programa
```

### Opción 2: Con Scripts de Ayuda (Recomendado)

**1. Configuración inicial (solo una vez):**
```bash
# Windows
copy mlasm.bat C:\Windows\System32\

# Linux/Mac
chmod +x mlasm
sudo ln -s $(pwd)/mlasm /usr/local/bin/
```

**2. Uso diario (simplificado):**
```bash
# Traducir y compilar en un solo paso
mlasm build es mi_programa.masm

# Solo traducir
mlasm translate es mi_programa.masm programa.asm

# Ver en otro idioma
mlasm view fr mi_programa.asm
```

---

## 🔧 Integración con Makefile

Crea un `Makefile` en tu proyecto:

```makefile
# Configuración
MLASM = python mlasm.py
LANG = es
NASM = nasm
LD = ld

# Archivos
SRC = main.masm
ASM = main.asm
OBJ = main.o
BIN = programa

# Reglas
all: $(BIN)

# MultiLang-ASM: traduce de tu idioma a ASM estándar
$(ASM): $(SRC)
	$(MLASM) $(LANG) $< $@

# NASM: compila ASM a objeto
$(OBJ): $(ASM)
	$(NASM) -f elf64 $< -o $@

# LD: enlaza objeto a binario
$(BIN): $(OBJ)
	$(LD) $< -o $@

clean:
	rm -f $(ASM) $(OBJ) $(BIN)

run: $(BIN)
	./$(BIN)

.PHONY: all clean run
```

**Ahora solo haces:**
```bash
make        # Compila todo
make run    # Ejecuta
make clean  # Limpia
```

---

## 🚀 Integración con Build Systems Modernos

### CMake

```cmake
# Encuentra Python
find_package(Python3 REQUIRED)

# Función personalizada para MultiLang-ASM
function(add_mlasm_executable target lang source)
    set(ASM_FILE "${CMAKE_CURRENT_BINARY_DIR}/${target}.asm")
    set(OBJ_FILE "${CMAKE_CURRENT_BINARY_DIR}/${target}.o")
    
    # Paso 1: MultiLang-ASM traduce
    add_custom_command(
        OUTPUT ${ASM_FILE}
        COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/mlasm.py ${lang} ${source} ${ASM_FILE}
        DEPENDS ${source}
        COMMENT "Traduciendo ${source} (${lang}) a ASM estándar..."
    )
    
    # Paso 2: NASM compila
    add_custom_command(
        OUTPUT ${OBJ_FILE}
        COMMAND nasm -f elf64 ${ASM_FILE} -o ${OBJ_FILE}
        DEPENDS ${ASM_FILE}
        COMMENT "Compilando ${ASM_FILE}..."
    )
    
    # Paso 3: Enlaza
    add_custom_target(${target} ALL
        COMMAND ld ${OBJ_FILE} -o ${target}
        DEPENDS ${OBJ_FILE}
    )
endfunction()

# Uso
add_mlasm_executable(mi_programa es main.masm)
```

---

## ⚡ Flujo de Desarrollo Típico

### Caso 1: Proyecto Simple

```bash
# 1. Escribir código en tu idioma
nano kernel.masm

# 2. Traducir
python mlasm.py es kernel.masm kernel.asm

# 3. Compilar
nasm -f elf64 kernel.asm -o kernel.o

# 4. Enlazar
ld kernel.o -o kernel.bin

# 5. Ejecutar/Probar
qemu-system-x86_64 -kernel kernel.bin
```

### Caso 2: Proyecto con Makefile

```bash
# 1. Escribir código
nano src/boot.masm
nano src/kernel.masm

# 2. Compilar todo
make

# 3. Ejecutar
make run
```

### Caso 3: Colaboración Multilingüe

```bash
# Programador español escribe:
python mlasm.py es bootloader_es.masm bootloader.asm

# Programador francés revisa en su idioma:
python mlasm.py fr bootloader.asm bootloader_fr.masm --reverse
nano bootloader_fr.masm

# Ambos comparten el mismo bootloader.asm estándar
```

---

## 📝 Ejemplos de Proyectos Reales

### Kernel Básico

**Estructura:**
```
mi-kernel/
├── mlasm.py
├── Makefile
├── src/
│   ├── boot.masm      (Español)
│   ├── kernel.masm    (Español)
│   └── drivers.masm   (Español)
└── build/
    └── (generado automáticamente)
```

**Makefile:**
```makefile
all:
	python mlasm.py es src/boot.masm build/boot.asm
	python mlasm.py es src/kernel.masm build/kernel.asm
	nasm -f elf64 build/boot.asm -o build/boot.o
	nasm -f elf64 build/kernel.asm -o build/kernel.o
	ld -T linker.ld build/*.o -o kernel.bin
```

### Bootloader

```bash
# boot.masm (Español)
python mlasm.py es boot.masm boot.asm
nasm -f bin boot.asm -o boot.bin
dd if=boot.bin of=disk.img
qemu-system-x86_64 -drive file=disk.img,format=raw
```

---

## 🎨 Configuración del Editor

### VSCode

Crea `.vscode/tasks.json`:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "MultiLang-ASM: Traducir",
            "type": "shell",
            "command": "python mlasm.py es ${file} ${fileDirname}/${fileBasenameNoExtension}.asm",
            "group": "build",
            "problemMatcher": []
        },
        {
            "label": "Compilar y Ejecutar",
            "type": "shell",
            "command": "python mlasm.py es ${file} temp.asm && nasm -f elf64 temp.asm && ld temp.o -o programa && ./programa",
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

Ahora: `Ctrl+Shift+B` traduce y compila automáticamente.

---

## 💡 Tips de Productividad

### 1. Alias en tu Shell

**Bash/Zsh (.bashrc o .zshrc):**
```bash
alias mlasm='python /ruta/a/mlasm.py'
alias mlas='mlasm es'
alias mlaf='mlasm fr'
```

**Windows (PowerShell Profile):**
```powershell
function mlasm { python C:\ruta\mlasm.py $args }
function mlas { mlasm es $args }
```

### 2. Script de Compilación Rápida

**Linux/Mac (`compile.sh`):**
```bash
#!/bin/bash
python mlasm.py $1 $2 temp.asm
nasm -f elf64 temp.asm -o temp.o
ld temp.o -o programa
./programa
rm temp.asm temp.o
```

**Uso:**
```bash
chmod +x compile.sh
./compile.sh es mi_codigo.masm
```

---

## 🔄 Workflow Continuo (Watch Mode)

Usa `inotifywait` (Linux) o `watchdog` (Python) para recompilar automáticamente:

```bash
#!/bin/bash
while inotifywait -e modify src/*.masm; do
    make
done
```

---

## ⏱️ Tiempo Total de Setup

| Acción | Tiempo |
|--------|--------|
| Descargar MultiLang-ASM | 10 segundos |
| Copiar mlasm.py a tu proyecto | 5 segundos |
| Crear Makefile | 30 segundos |
| **Primer uso** | **45 segundos** |
| Uso subsiguiente | 1 comando (`make`) |

---

## 🎯 Resumen: 3 Formas de Usar

### 🔹 Nivel 1: Directo (Aprendizaje)
```bash
python mlasm.py es codigo.masm codigo.asm
```

### 🔹 Nivel 2: Makefile (Proyectos)
```bash
make
```

### 🔹 Nivel 3: Integración (Producción)
- CMake
- Build scripts
- CI/CD pipelines

---

**MultiLang-ASM se integra sin fricción en cualquier workflow existente.** 🛡️✨
