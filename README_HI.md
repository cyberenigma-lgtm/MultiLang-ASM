# MultiLang-ASM v1.0.0 (UPL+ C99 संस्करण)

**x86_64 के लिए दुनिया का पहला बहुभाषी और संप्रभु असेंबलर इंजन।**  
**UPL (Universal Polyglot Layer)** पारिस्थितिकी तंत्र और Neuro-OS का अभिन्न अंग।

अपनी मातृभाषा में असेंबली कोड लिखें · 150 विश्व भाषाएं · 200+ x86_64 निर्देश · 100% मूल ANSI C99 इंजन · शून्य पायथन निर्भरता · त्वरित निष्पादन (<2 ms) · NASM के साथ संगत।

## त्वरित शुरुआत
```bash
# नेटिव इंजन का संकलन:
gcc -std=c99 -Wall -Wextra -O2 src/mlasm_core.c -I src -o bin/mlasm

# अनुवाद करें:
mlasm hi example.masm -o example.asm

# स्वचालित भाषा पहचान:
mlasm auto example.masm -o example.asm
```
