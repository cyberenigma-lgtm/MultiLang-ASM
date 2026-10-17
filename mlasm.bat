@echo off
REM ============================================================================
REM MultiLang-ASM - Native CLI Launcher (UPL Systems Standard)
REM 100% ANSI C99 Native Engine - Zero Python Dependency
REM ============================================================================

setlocal enabledelayedexpansion

set "ROOT_DIR=%~dp0"
set "BIN_EXE=%ROOT_DIR%bin\mlasm.exe"
set "SRC_C=%ROOT_DIR%src\mlasm_core.c"

REM Si el binario nativo no existe, compilarlo en el acto con GCC
if not exist "%BIN_EXE%" (
    if not exist "%ROOT_DIR%bin" mkdir "%ROOT_DIR%bin"
    echo [BUILD] Compilando motor nativo MultiLang-ASM (ANSI C99)...
    where gcc >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] GCC no encontrado en el PATH. Instala MinGW-w64 o GCC para compilar el motor nativo.
        exit /b 1
    )
    gcc -std=c99 -Wall -Wextra -O2 "%SRC_C%" -I "%ROOT_DIR%src" -o "%BIN_EXE%"
    if errorlevel 1 (
        echo [ERROR] Fallo la compilacion del motor nativo.
        exit /b 1
    )
    echo [BUILD] Motor nativo compilado con exito: %BIN_EXE%
)

REM Si no hay argumentos, mostrar ayuda de mlasm.exe
if "%~1"=="" (
    "%BIN_EXE%" --help
    exit /b 0
)

REM Ejecutar binario nativo con todos los argumentos
"%BIN_EXE%" %*
exit /b %ERRORLEVEL%
