# ============================================================================
# MultiLang-ASM - Master Makefile (UPL Systems Standard)
# 100% Standalone ANSI C99 Native Engine - Zero External Dependencies
# ============================================================================

CC ?= gcc
CFLAGS ?= -std=c99 -Wall -Wextra -Werror -O2
INCLUDES = -I src

BIN_DIR = bin
SRC_DIR = src

ifeq ($(OS),Windows_NT)
    TARGET = $(BIN_DIR)/mlasm.exe
    RM = del /q /f
    MKDIR = if not exist $(BIN_DIR) mkdir $(BIN_DIR)
else
    TARGET = $(BIN_DIR)/mlasm
    RM = rm -rf
    MKDIR = mkdir -p $(BIN_DIR)
endif

.PHONY: all clean test help

all: $(TARGET)

$(TARGET): $(SRC_DIR)/mlasm_core.c $(SRC_DIR)/masm_tables.h
	@echo [CC] Compilando motor nativo MultiLang-ASM ($@)...
	@$(MKDIR)
	$(CC) $(CFLAGS) $(SRC_DIR)/mlasm_core.c $(INCLUDES) -o $(TARGET)
	@echo [OK] Compilacion completada con exito: $(TARGET)

test: $(TARGET)
	@echo [TEST] Ejecutando suite de pruebas...
	./$(TARGET) --test

clean:
	@echo [CLEAN] Limpiando binarios generados...
	$(RM) $(TARGET)

help:
	@echo "MultiLang-ASM - Comandos Disponibles:"
	@echo "  make        - Compila el motor nativo mlasm en bin/"
	@echo "  make test   - Ejecuta la suite de pruebas nativas"
	@echo "  make clean  - Elimina los binarios generados"
