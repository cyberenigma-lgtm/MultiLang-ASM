@echo off
REM ============================================================================
REM mlasm.bat - Wrapper para MultiLang-ASM en Windows
REM ============================================================================

setlocal enabledelayedexpansion

REM Detectar la ruta del script
set "MLASM_DIR=%~dp0"
set "MLASM_SCRIPT=%MLASM_DIR%mlasm.py"

REM Verificar que existe mlasm.py
if not exist "%MLASM_SCRIPT%" (
    echo Error: No se encontro mlasm.py en %MLASM_DIR%
    exit /b 1
)

REM Si no hay argumentos, mostrar ayuda
if "%~1"=="" (
    python "%MLASM_SCRIPT%"
    exit /b 0
)

REM Comandos especiales
if "%~1"=="build" (
    REM mlasm build es archivo.masm
    set LANG=%~2
    set SRC=%~3
    set ASM=!SRC:.masm=.asm!
    set OBJ=!SRC:.masm=.o!
    set BIN=!SRC:.masm=.exe!
    
    echo [1/4] Traduciendo !SRC! ^(!LANG!^) -^> !ASM!
    python "%MLASM_SCRIPT%" !LANG! "!SRC!" "!ASM!"
    if errorlevel 1 exit /b 1
    
    echo [2/4] Compilando !ASM! -^> !OBJ!
    nasm -f win64 "!ASM!" -o "!OBJ!"
    if errorlevel 1 exit /b 1
    
    echo [3/4] Enlazando !OBJ! -^> !BIN!
    gcc "!OBJ!" -o "!BIN!" -nostartfiles
    if errorlevel 1 exit /b 1
    
    echo [4/4] Listo: !BIN!
    exit /b 0
)

if "%~1"=="translate" (
    REM mlasm translate es entrada.masm salida.asm
    python "%MLASM_SCRIPT%" %~2 %~3 %~4
    exit /b !ERRORLEVEL!
)

if "%~1"=="view" (
    REM mlasm view fr archivo.asm
    set LANG=%~2
    set SRC=%~3
    set OUT=!SRC:.asm=_!LANG!.masm!
    python "%MLASM_SCRIPT%" !LANG! "!SRC!" "!OUT!" --reverse
    echo Archivo generado: !OUT!
    exit /b !ERRORLEVEL!
)

REM Modo directo: pasar todos los argumentos
python "%MLASM_SCRIPT%" %*
exit /b !ERRORLEVEL!
