# MultiLang-ASM v1.0.0 (UPL+ C99 에디션)

**세계 최초의 x86_64 다국어 어셈블러 엔진.**  
**UPL (Universal Polyglot Layer)** 생태계 및 Neuro-OS 핵심 구성 요소.

모국어로 어셈블리 코드 작성 · 전 세계 150개 언어 지원 · 200개 이상의 x86_64 명령어 세트 · 100% 순수 ANSI C99 네이티브 엔진 · 파이썬 런타임 의존성 제로 · 초고속 변환 (<2 ms) · NASM 완벽 호환.

## 빠른 시작
```bash
# 네이티브 바이너리 빌드:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# 코드 변환:
mlasm ko sample.masm -o sample.asm

# 자동 언어 감지:
mlasm auto sample.masm -o sample.asm
```
