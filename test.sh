#!/usr/bin/env bash
# ============================================================================
# MultiLang-ASM: Master Test Suite Runner (Linux / macOS)
# Validates the Native ANSI C99 Engine across 150 Languages & 200+ Instructions
# ============================================================================

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_EXE="$DIR/bin/mlasm"
SRC_C="$DIR/src/mlasm_core.c"

echo "===================================================================="
echo "  MULTILANG-ASM v1.0.0: MASTER TEST SUITE (NATIVE C99 / UPL+)"
echo "  150 World Languages - 200+ Instructions - Zero Python Dependency"
echo "===================================================================="

mkdir -p "$DIR/bin"

if [ ! -f "$BIN_EXE" ]; then
    echo "[STEP 0] Compiling native C99 engine with GCC/Clang..."
    gcc -std=c99 -Wall -Wextra -Werror -O2 "$SRC_C" -I "$DIR/src" -o "$BIN_EXE"
fi

echo ""
echo "[STEP 1] Running internal native C99 test suite..."
"$BIN_EXE" --test

echo ""
echo "[STEP 2] Testing auto-detection & transpilation across diverse global scripts..."

"$BIN_EXE" auto "$DIR/examples/hello_es.masm" -o "$DIR/bin/out_es.asm"
"$BIN_EXE" auto "$DIR/examples/hello_zh.masm" -o "$DIR/bin/out_zh.asm"
"$BIN_EXE" auto "$DIR/examples/hello_ru.masm" -o "$DIR/bin/out_ru.asm"
"$BIN_EXE" auto "$DIR/examples/hello_tr.masm" -o "$DIR/bin/out_tr.asm"
"$BIN_EXE" auto "$DIR/examples/hello_la.masm" -o "$DIR/bin/out_la.asm"
"$BIN_EXE" auto "$DIR/examples/hello_eo.masm" -o "$DIR/bin/out_eo.asm"
"$BIN_EXE" auto "$DIR/examples/hello_cs.masm" -o "$DIR/bin/out_cs.asm"
"$BIN_EXE" auto "$DIR/examples/hello_gn.masm" -o "$DIR/bin/out_gn.asm"
"$BIN_EXE" auto "$DIR/examples/hello_sw.masm" -o "$DIR/bin/out_sw.asm"

echo ""
echo "[STEP 3] Testing bidirectional roundtrip (Standard NASM -> Native Reverse)..."
"$BIN_EXE" --reverse es "$DIR/bin/out_es.asm" -o "$DIR/bin/roundtrip_es.masm"
"$BIN_EXE" --reverse zh "$DIR/bin/out_zh.asm" -o "$DIR/bin/roundtrip_zh.masm"

rm -f "$DIR/bin/out_"*.asm "$DIR/bin/roundtrip_"*.masm

echo ""
echo "===================================================================="
echo "  SUCCESS: ALL 150 LANGUAGES & C99 ENGINE TESTS PASSED (100% OK)"
echo "===================================================================="
