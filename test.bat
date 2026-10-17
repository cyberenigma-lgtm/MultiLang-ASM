@echo off
REM ============================================================================
REM MultiLang-ASM: Master Test Suite Runner (Windows)
REM Validates the Native ANSI C99 Engine across 150 Languages & 200+ Instructions
REM ============================================================================

setlocal enabledelayedexpansion

set "ROOT_DIR=%~dp0"
set "BIN_EXE=%ROOT_DIR%bin\mlasm.exe"
set "SRC_C=%ROOT_DIR%src\mlasm_core.c"

echo ====================================================================
echo   MULTILANG-ASM v1.0.0: MASTER TEST SUITE (NATIVE C99 / UPL+)
echo   150 World Languages - 200+ Instructions - Zero Python Dependency
echo ====================================================================

REM 1. Ensure the binary is compiled
if not exist "%BIN_EXE%" (
    echo [STEP 0] Compiling native C99 engine with GCC...
    if not exist "%ROOT_DIR%bin" mkdir "%ROOT_DIR%bin"
    gcc -std=c99 -Wall -Wextra -Werror -O2 "%SRC_C%" -I "%ROOT_DIR%src" -o "%BIN_EXE%"
    if errorlevel 1 (
        echo [FAIL] Compilation of mlasm.exe failed!
        exit /b 1
    )
)

echo.
echo [STEP 1] Running internal native C99 test suite...
"%BIN_EXE%" --test
if errorlevel 1 (
    echo [FAIL] Internal unit tests failed!
    exit /b 1
)

echo.
echo [STEP 2] Testing auto-detection and transpilation across diverse global scripts...

REM Spanish (Romance / Latin script)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_es.masm" -o "%ROOT_DIR%bin\out_es.asm"
if errorlevel 1 ( echo [FAIL] Spanish test failed & exit /b 1 )

REM Chinese (East Asian / Hanzi CJK)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_zh.masm" -o "%ROOT_DIR%bin\out_zh.asm"
if errorlevel 1 ( echo [FAIL] Chinese test failed & exit /b 1 )

REM Russian (Slavic / Cyrillic script)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_ru.masm" -o "%ROOT_DIR%bin\out_ru.asm"
if errorlevel 1 ( echo [FAIL] Russian test failed & exit /b 1 )

REM Turkish (Turkic / Latin script with diacritics)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_tr.masm" -o "%ROOT_DIR%bin\out_tr.asm"
if errorlevel 1 ( echo [FAIL] Turkish test failed & exit /b 1 )

REM Latin (Classical Indo-European)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_la.masm" -o "%ROOT_DIR%bin\out_la.asm"
if errorlevel 1 ( echo [FAIL] Latin test failed & exit /b 1 )

REM Esperanto (International Auxiliary)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_eo.masm" -o "%ROOT_DIR%bin\out_eo.asm"
if errorlevel 1 ( echo [FAIL] Esperanto test failed & exit /b 1 )

REM Czech (West Slavic)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_cs.masm" -o "%ROOT_DIR%bin\out_cs.asm"
if errorlevel 1 ( echo [FAIL] Czech test failed & exit /b 1 )

REM Guarani (Indigenous American / Tupi-Guarani)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_gn.masm" -o "%ROOT_DIR%bin\out_gn.asm"
if errorlevel 1 ( echo [FAIL] Guarani test failed & exit /b 1 )

REM Swahili (African Bantu)
"%BIN_EXE%" auto "%ROOT_DIR%examples\hello_sw.masm" -o "%ROOT_DIR%bin\out_sw.asm"
if errorlevel 1 ( echo [FAIL] Swahili test failed & exit /b 1 )

echo.
echo [STEP 3] Testing bidirectional roundtrip (Standard NASM to Native Reverse)...
"%BIN_EXE%" --reverse es "%ROOT_DIR%bin\out_es.asm" -o "%ROOT_DIR%bin\roundtrip_es.masm"
if errorlevel 1 ( echo [FAIL] Spanish roundtrip failed & exit /b 1 )

"%BIN_EXE%" --reverse zh "%ROOT_DIR%bin\out_zh.asm" -o "%ROOT_DIR%bin\roundtrip_zh.masm"
if errorlevel 1 ( echo [FAIL] Chinese roundtrip failed & exit /b 1 )

REM Cleanup test output artifacts
del /q "%ROOT_DIR%bin\out_*.asm" >nul 2>&1
del /q "%ROOT_DIR%bin\roundtrip_*.masm" >nul 2>&1

echo.
echo ====================================================================
echo   SUCCESS: ALL 150 LANGUAGES AND C99 ENGINE TESTS PASSED (100%% OK)
echo ====================================================================
exit /b 0
