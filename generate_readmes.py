
import os
import sys

# Import mlasm to use its translation engine and dictionaries
sys.path.append(os.getcwd())
try:
    import mlasm
except ImportError:
    print("Error: Could not import mlasm.py")
    sys.exit(1)


# Localized strings for each language
TRANSLATIONS = {
    "fr": {
        "slogan": "Le premier assembleur x86_64 multilingue.",
        "desc": "Écrivez de l'assembleur dans votre langue maternelle.",
        "what_title": "Qu'est-ce que c'est ?",
        "what_desc": "MultiLang-ASM vous permet d'écrire de l'assembleur x86_64 en utilisant des mots-clés en **Français**.\nIl traduit automatiquement votre code en assembleur NASM standard.",
        "features": "Fonctionnalités",
        "write_in": "Écrire en Français",
        "auto_detect": "Détection Auto",
        "example": "Exemple en Français",
        "usage": "Utilisation"
    },
    "de": {
        "slogan": "Der erste mehrsprachige x86_64-Assembler.",
        "desc": "Schreiben Sie Assembler in Ihrer Muttersprache.",
        "what_title": "Was ist das?",
        "what_desc": "Mit MultiLang-ASM können Sie x86_64-Assembly mit Schlüsselwörtern auf **Deutsch** schreiben.\nEs übersetzt Ihren Code automatisch in Standard-NASM-Assembly.",
        "features": "Funktionen",
        "write_in": "Auf Deutsch schreiben",
        "auto_detect": "Auto-Erkennung",
        "example": "Beispiel auf Deutsch",
        "usage": "Verwendung"
    },
    "it": {
        "slogan": "Il primo assemblatore x86_64 multilingue.",
        "desc": "Scrivi assembler nella tua lingua madre.",
        "what_title": "Che cos'è?",
        "what_desc": "MultiLang-ASM ti permette di scrivere assembly x86_64 usando parole chiave in **Italiano**.\nTraduce automaticamente il tuo codice in assembly NASM standard.",
        "features": "Caratteristiche",
        "write_in": "Scrivi in Italiano",
        "auto_detect": "Rilevamento Auto",
        "example": "Esempio in Italiano",
        "usage": "Utilizzo"
    },
    "pt": {
        "slogan": "O primeiro assembler x86_64 multilíngue.",
        "desc": "Escreva assembly em sua língua nativa.",
        "what_title": "O que é isso?",
        "what_desc": "MultiLang-ASM permite escrever assembly x86_64 usando palavras-chave em **Português**.\nEle traduz automaticamente seu código para assembly NASM padrão.",
        "features": "Recursos",
        "write_in": "Escrever em Português",
        "auto_detect": "Detecção Automática",
        "example": "Exemplo em Português",
        "usage": "Uso"
    },
    "ru": {
        "slogan": "Первый многоязычный ассемблер x86_64.",
        "desc": "Пишите на ассемблере на своем родном языке.",
        "what_title": "Что это?",
        "what_desc": "MultiLang-ASM позволяет писать ассемблерный код x86_64, используя ключевые слова на **Русском**.\nОн автоматически переводит ваш код в стандартный ассемблер NASM.",
        "features": "Особенности",
        "write_in": "Писать на Русском",
        "auto_detect": "Автоопределение",
        "example": "Пример на Русском",
        "usage": "Использование"
    },
    "ja": {
        "slogan": "世界初の多言語 x86_64 アセンブラ。",
        "desc": "母国語でアセンブリを書きましょう。",
        "what_title": "これは何ですか？",
        "what_desc": "MultiLang-ASM は、**日本語**のキーワードを使用して x86_64 アセンブリを書くことを可能にします。\nコードは自動的に標準的な NASM アセンブリに翻訳されます。",
        "features": "特徴",
        "write_in": "日本語で書く",
        "auto_detect": "自動検出",
        "example": "日本語の例",
        "usage": "使い方"
    },
    "zh": {
        "slogan": "第一个多语言 x86_64 汇编器。",
        "desc": "用您的母语编写汇编代码。",
        "what_title": "这是什么？",
        "what_desc": "MultiLang-ASM 允许您使用**中文**关键字编写 x86_64 汇编。\n它会自动将您的代码翻译成标准的 NASM 汇编。",
        "features": "特性",
        "write_in": "用中文编写",
        "auto_detect": "自动检测",
        "example": "中文示例",
        "usage": "用法"
    },
    "ko": {
        "slogan": "최초의 다국어 x86_64 어셈블러.",
        "desc": "모국어로 어셈블리를 작성하세요.",
        "what_title": "이것은 무엇입니까?",
        "what_desc": "MultiLang-ASM을 사용하면 **한국어** 키워드를 사용하여 x86_64 어셈블리를 작성할 수 있습니다.\n코드는 자동으로 표준 NASM 어셈블리로 번역됩니다.",
        "features": "특징",
        "write_in": "한국어로 작성",
        "auto_detect": "자동 감지",
        "example": "한국어 예제",
        "usage": "사용법"
    },
    "ar": {
        "slogan": "أول مجمع x86_64 متعدد اللغات.",
        "desc": "اكتب لغة التجميع بلغتك الأم.",
        "what_title": "ما هذا؟",
        "what_desc": "يسمح لك MultiLang-ASM بكتابة تجميع x86_64 باستخدام كلمات رئيسية باللغة **العربية**.\nيترجم الكود الخاص بك تلقائيًا إلى تجميع NASM القياسي.",
        "features": "الميزات",
        "write_in": "اكتب باللغة العربية",
        "auto_detect": "الكشف التلقائي",
        "example": "مثال بالعربية",
        "usage": "الاستخدام"
    },
    "id": {
        "slogan": "Assembler x86_64 multibahasa pertama.",
        "desc": "Tulis assembly dalam bahasa ibu Anda.",
        "what_title": "Apa ini?",
        "what_desc": "MultiLang-ASM memungkinkan Anda menulis assembly x86_64 menggunakan kata kunci dalam **Bahasa Indonesia**.\nIni secara otomatis menerjemahkan kode Anda ke assembly NASM standar.",
        "features": "Fitur",
        "write_in": "Tulis dalam Bahasa Indonesia",
        "auto_detect": "Deteksi Otomatis",
        "example": "Contoh Bahasa Indonesia",
        "usage": "Penggunaan"
    },
    "hi": {
        "slogan": "पहला बहुभाषी x86_64 असेंबलर।",
        "desc": "अपनी मातृभाषा में असेंबली लिखें।",
        "what_title": "यह क्या है?",
        "what_desc": "MultiLang-ASM आपको **हिंदी** कीवर्ड का उपयोग करके x86_64 असेंबली लिखने की अनुमति देता है।\nयह स्वचालित रूप से आपके कोड को मानक NASM असेंबली में अनुवादित करता है।",
        "features": "विशेषताएं",
        "write_in": "हिंदी में लिखें",
        "auto_detect": "स्वतः पहचान",
        "example": "हिंदी उदाहरण",
        "usage": "उपयोग"
    },
    "tr": {
        "slogan": "İlk çok dilli x86_64 çevirici (assembler).",
        "desc": "Kendi ana dilinizde assembly yazın.",
        "what_title": "Bu nedir?",
        "what_desc": "MultiLang-ASM, **Türkçe** anahtar kelimeler kullanarak x86_64 assembly yazmanıza olanak tanır.\nKodunuzu otomatik olarak standart NASM assembly diline çevirir.",
        "features": "Özellikler",
        "write_in": "Türkçe yazın",
        "auto_detect": "Otomatik Algılama",
        "example": "Türkçe Örnek",
        "usage": "Kullanım"
    },
    "pl": {
        "slogan": "Pierwszy wielojęzyczny asembler x86_64.",
        "desc": "Pisz w asemblerze w swoim ojczystym języku.",
        "what_title": "Co to jest?",
        "what_desc": "MultiLang-ASM umożliwia pisanie w asemblerze x86_64 przy użyciu słów kluczowych w języku **Polskim**.\nAutomatycznie tłumaczy Twój kod na standardowy asembler NASM.",
        "features": "Funkcje",
        "write_in": "Pisz po Polsku",
        "auto_detect": "Wykrywanie Auto",
        "example": "Przykład po Polsku",
        "usage": "Użycie"
    },
    "sv": {
        "slogan": "Den första flerspråkiga x86_64-assemblern.",
        "desc": "Skriv assembler på ditt modersmål.",
        "what_title": "Vad är detta?",
        "what_desc": "MultiLang-ASM låter dig skriva x86_64-assembler med nyckelord på **Svenska**.\nDen översätter automatiskt din kod till standard NASM-assembler.",
        "features": "Funktioner",
        "write_in": "Skriv på Svenska",
        "auto_detect": "Automatisk Detektering",
        "example": "Svenskt Exempel",
        "usage": "Användning"
    },
    "nl": {
        "slogan": "De eerste meertalige x86_64 assembler.",
        "desc": "Schrijf assembler in je moedertaal.",
        "what_title": "Wat is dit?",
        "what_desc": "Met MultiLang-ASM kun je x86_64 assembler schrijven met trefwoorden in het **Nederlands**.\nHet vertaalt je code automatisch naar standaard NASM assembler.",
        "features": "Functies",
        "write_in": "Schrijf in het Nederlands",
        "auto_detect": "Automatische Detectie",
        "example": "Nederlands Voorbeeld",
        "usage": "Gebruik"
    }
}

TEMPLATE = """# 🛡️ MultiLang-ASM v0.4

> *"{slogan}"*

**{desc}**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Languages](https://img.shields.io/badge/languages-16-blue.svg)](docs/)
[![Instructions](https://img.shields.io/badge/instructions-80+-green.svg)](docs/)

📖 **{lang_name}** | **[English](README.md)** | **[Español](README_ES.md)**

---

## 🚀 {what_title}

{what_desc}

## ✨ {features}

- 🌍 **{write_in}** ({lang_code})
- 🤖 **{auto_detect}:** `python mlasm.py auto program.masm`
- ⚡ **Macros:** `%define` supported
- 🔁 **Reversible:** `{lang_name} <-> ASM`

## 📖 {example}

### Source Code (`hello.masm`)
```asm
{example_code}
```

### Generates Standard ASM
```asm
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 13
syscall

mov rax, 60
mov rdi, 0
syscall
```

## 🛠️ {usage}

```bash
python mlasm.py auto hello.masm
```

---
**Version:** v0.4 | **Project:** [MultiLang-ASM](https://github.com/cyberenigma-lgtm/MultiLang-ASM)
"""

# Example standard code to translate to native
STANDARD_EXAMPLE = """mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 13
syscall

mov rax, 60
mov rdi, 0
syscall"""

# Language Names map
LANG_NAMES = {
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "pt": "Português",
    "ru": "Русский",
    "ja": "日本語",
    "zh": "中文",
    "ko": "한국어",
    "ar": "العربية",
    "id": "Bahasa Indonesia",
    "hi": "Hindi",
    "tr": "Türkçe",
    "pl": "Polski",
    "sv": "Svenska",
    "nl": "Nederlands"
}

def generate_readmes():
    print("Generating Localized READMEs...")
    
    for lang_code, lang_name in LANG_NAMES.items():
        print(f"Processing {lang_name} ({lang_code})...")
        
        # Translate standard example to native language (Reverse Translation)
        try:
            native_code = mlasm.translate(STANDARD_EXAMPLE, lang_code, to_standard=False)
        except Exception as e:
            print(f"Error translating for {lang_code}: {e}")
            native_code = STANDARD_EXAMPLE
            
        # Get translation strings
        t = TRANSLATIONS.get(lang_code, TRANSLATIONS["fr"]) # Fallback to FR if missing (should not happen)
        
        # Fill template
        content = TEMPLATE.format(
            lang_name=lang_name,
            lang_code=lang_code,
            slogan=t["slogan"],
            desc=t["desc"],
            what_title=t["what_title"],
            what_desc=t["what_desc"],
            features=t["features"],
            write_in=t["write_in"],
            auto_detect=t["auto_detect"],
            example=t["example"],
            usage=t["usage"],
            example_code=native_code
        )
        
        # Write file
        filename = f"README_{lang_code.upper()}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Created {filename}")

if __name__ == "__main__":
    generate_readmes()
