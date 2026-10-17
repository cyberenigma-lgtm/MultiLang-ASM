# MultiLang-ASM v1.0.0 (إصدار UPL+ C99)

**أول محرك أسمبلي متعدد اللغات والسيادي في العالم لمعمارية x86_64.**  
جزء لا يتجزأ من منظومة **UPL (Universal Polyglot Layer)** ونواة Neuro-OS.

اكتب لغة التجميع بلغتك الأم · 150 لغة عالمية · أكثر من 200 تعليمة برمجية x86_64 · محرك أصلي 100% بلغة ANSI C99 · بدون أي اعتماد على بايثون · أداء فوري (<2 مللي ثانية) · متوافق تماماً مع NASM.

## الاستخدام السريع
```bash
# تجميع المحرك الأصلي:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# ترجمة الكود:
mlasm ar example.masm -o example.asm

# التعرف التلقائي على اللغة:
mlasm auto example.masm -o example.asm
```
