import sys
import re
import os

# ███╗   ███╗██╗     ██╗     ██╗     █████╗ ███╗   ██╗ ██████╗ 
# ████╗ ████║██║     ██║     ██║    ██╔══██╗████╗  ██║██╔════╝ 
# ██╔████╔██║██║     ██║     ██║    ███████║██╔██╗ ██║██║  ███╗
# ██║╚██╔╝██║██║     ██║     ██║    ██╔══██║██║╚██╗██║██║   ██║
# ██║ ╚═╝ ██║███████╗███████╗███████╗██║  ██║██║ ╚████║╚██████╔╝
# ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
#
#        MultiLang-ASM v0.2 — Parte del ecosistema Neuro-OS
#        Ensamblador Multilingüe Universal | Accesibilidad sin Barreras
#        https://github.com/tuusuario/MultiLang-ASM

# Fix para Windows: forzar UTF-8 en consola
if os.name == 'nt':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# ============================================================================
# NÚCLEO CANÓNICO DE INSTRUCCIONES (independiente del idioma)
# ============================================================================
INSTRUCTIONS = {
    # Movimiento
    "mov": {"category": "movimiento"},
    "xchg": {"category": "movimiento"},
    "lea": {"category": "movimiento"},
    "movzx": {"category": "movimiento"},
    "movsx": {"category": "movimiento"},

    # Aritmética
    "add": {"category": "aritmetica"},
    "sub": {"category": "aritmetica"},
    "mul": {"category": "aritmetica"},
    "imul": {"category": "aritmetica"},
    "div": {"category": "aritmetica"},
    "idiv": {"category": "aritmetica"},
    "inc": {"category": "aritmetica"},
    "dec": {"category": "aritmetica"},
    "neg": {"category": "aritmetica"},

    # Lógica
    "and": {"category": "logica"},
    "or": {"category": "logica"},
    "not": {"category": "logica"},
    "xor": {"category": "logica"},
    "shl": {"category": "logica"},
    "shr": {"category": "logica"},
    "sal": {"category": "logica"},
    "sar": {"category": "logica"},
    "rol": {"category": "logica"},
    "ror": {"category": "logica"},

    # Comparación
    "cmp": {"category": "comparacion"},
    "test": {"category": "comparacion"},

    # Flujo
    "jmp": {"category": "flujo"},
    "call": {"category": "flujo"},
    "ret": {"category": "flujo"},
    "je": {"category": "flujo"},
    "jz": {"category": "flujo"},
    "jne": {"category": "flujo"},
    "jnz": {"category": "flujo"},
    "jg": {"category": "flujo"},
    "jge": {"category": "flujo"},
    "jl": {"category": "flujo"},
    "jle": {"category": "flujo"},
    "ja": {"category": "flujo"},
    "jb": {"category": "flujo"},
    "jae": {"category": "flujo"},
    "jbe": {"category": "flujo"},
    "js": {"category": "flujo"},
    "jns": {"category": "flujo"},
    "jo": {"category": "flujo"},
    "jno": {"category": "flujo"},
    "jp": {"category": "flujo"},
    "jnp": {"category": "flujo"},

    # Pila
    "push": {"category": "pila"},
    "pop": {"category": "pila"},
    "pushf": {"category": "pila"},
    "popf": {"category": "pila"},

    # Cadenas
    "movsb": {"category": "cadenas"},
    "movsw": {"category": "cadenas"},
    "movsd": {"category": "cadenas"},
    "stosb": {"category": "cadenas"},
    "lodsb": {"category": "cadenas"},
    "scasb": {"category": "cadenas"},
    "rep": {"category": "cadenas"},
    "repne": {"category": "cadenas"},

    # Bucles
    "loop": {"category": "bucles"},
    "loopz": {"category": "bucles"},
    "loopnz": {"category": "bucles"},

    # Sistema
    "int": {"category": "sistema"},
    "syscall": {"category": "sistema"},
    "sysret": {"category": "sistema"},
    "iret": {"category": "sistema"},
    "iretq": {"category": "sistema"},

    # Miscelánea
    "nop": {"category": "miscelanea"},
    "hlt": {"category": "miscelanea"},
    "cli": {"category": "miscelanea"},
    "sti": {"category": "miscelanea"},
    "cld": {"category": "miscelanea"},
    "std": {"category": "miscelanea"},
    "wait": {"category": "miscelanea"},

    # Conversión
    "cbw": {"category": "conversion"},
    "cwd": {"category": "conversion"},
    "cdq": {"category": "conversion"},
    "cqo": {"category": "conversion"},
}

# ============================================================================
# TABLA DE ALIAS POR IDIOMA (Idioma Nativo -> Mnemónico Estándar)
# ============================================================================
TABLE = {
    "es": {
        # Movimiento
        "mover": "mov", "copiar": "mov", "intercambiar": "xchg", "cargar": "mov",
        "cargar_efectivo": "lea", "extender_cero": "movzx", "extender_signo": "movsx",
        
        # Aritmética
        "sumar": "add", "añadir": "add", "agregar": "add", "restar": "sub",
        "multiplicar": "mul", "multiplicar_signado": "imul",
        "dividir": "div", "dividir_signado": "idiv",
        "incrementar": "inc", "decrementar": "dec", "negar": "neg",
        
        # Lógica
        "y": "and", "o": "or", "no": "not", "exclusivo": "xor",
        "desplazar_izq": "shl", "desplazar_der": "shr",
        "desplazar_arit_izq": "sal", "desplazar_arit_der": "sar",
        "rotar_izq": "rol", "rotar_der": "ror",
        
        # Comparación
        "comparar": "cmp", "probar": "test",
        
        # Flujo
        "saltar": "jmp", "llamar": "call", "retornar": "ret", "volver": "ret",
        "si_igual": "je", "si_cero": "jz", "si_no_igual": "jne", "si_no_cero": "jnz",
        "si_mayor": "jg", "si_mayor_igual": "jge", "si_menor": "jl", "si_menor_igual": "jle",
        "si_arriba": "ja", "si_abajo": "jb", "si_arriba_igual": "jae", "si_abajo_igual": "jbe",
        "si_signo": "js", "si_no_signo": "jns", "si_desborde": "jo", "si_no_desborde": "jno",
        "si_paridad": "jp", "si_no_paridad": "jnp",
        
        # Pila
        "meter": "push", "sacar": "pop", "meter_banderas": "pushf", "sacar_banderas": "popf",
        
        # Cadenas
        "mover_byte": "movsb", "mover_palabra": "movsw", "mover_doble": "movsd",
        "almacenar_byte": "stosb", "cargar_byte": "lodsb", "escanear_byte": "scasb",
        "repetir": "rep", "repetir_mientras": "repne",
        
        # Bucles
        "ciclo": "loop", "ciclo_si_cero": "loopz", "ciclo_si_no_cero": "loopnz",
        
        # Sistema
        "interrupcion": "int", "llamada_sistema": "syscall",
        "retorno_sistema": "sysret", "retorno_interrupcion": "iret",
        
        # Miscelánea
        "nada": "nop", "detener": "hlt",
        "limpiar_interrupciones": "cli", "activar_interrupciones": "sti",
        "limpiar_direccion": "cld", "fijar_direccion": "std", "esperar": "wait",
        
        # Conversión
        "convertir_byte_palabra": "cbw", "convertir_palabra_doble": "cwd",
        "convertir_doble_cuadruple": "cdq", "convertir_cuadruple_octo": "cqo",
    },
    
    "fr": {
        # Mouvement
        "deplacer": "mov", "copier": "mov", "echanger": "xchg",
        "charger_effectif": "lea", "etendre_zero": "movzx", "etendre_signe": "movsx",
        
        # Arithmétique
        "ajouter": "add", "soustraire": "sub", "multiplier": "mul",
        "multiplier_signe": "imul", "diviser": "div", "diviser_signe": "idiv",
        "incrementer": "inc", "decrementer": "dec", "negativer": "neg",
        
        # Logique
        "et": "and", "ou": "or", "non": "not", "ou_exclusif": "xor",
        "decaler_gauche": "shl",  "decaler_droite": "shr",
        "decaler_arith_gauche": "sal", "decaler_arith_droite": "sar",
        "rot_gauche": "rol", "rot_droite": "ror",
        
        # Comparaison
        "comparer": "cmp", "tester": "test",
        
        # Sauts
        "sauter": "jmp", "appeler": "call", "retourner": "ret",
        "si_egal": "je", "si_zero": "jz", "si_pas_egal": "jne", "si_pas_zero": "jnz",
        "si_plus_grand": "jg", "si_plus_grand_egal": "jge",
        "si_plus_petit": "jl", "si_plus_petit_egal": "jle",
        
        # Pile
        "empiler": "push", "depiler": "pop",
        
        # Système
        "interruption": "int", "appel_systeme": "syscall",
    },
    
    "de": {
        # Datenbewegung
        "bewegen": "mov", "tauschen": "xchg", "effektiv_laden": "lea",
        "null_erweitern": "movzx", "vorzeichen_erweitern": "movsx",
        
        # Arithmetik
        "addieren": "add", "subtrahieren": "sub", "multiplizieren": "mul",
        "multiplizieren_vorzeichen": "imul", "dividieren": "div",
        "dividieren_vorzeichen": "idiv", "inkrementieren": "inc",
        "dekrementieren": "dec", "negieren": "neg",
        
        # Logik
        "und": "and", "oder": "or", "nicht": "not", "exklusiv_oder": "xor",
        
        # Ablaufsteuerung
        "springen": "jmp", "rufen": "call", "zurueckkehren": "ret",
        
        # System
        "interruption": "int", "unterbrechung": "int",
    },
    
    "it": {
        # Movimento
        "spostare": "mov", "copiare": "mov", "scambiare": "xchg",
        "caricare_effettivo": "lea", "estendere_zero": "movzx",
        "estendere_segno": "movsx",
        
        # Aritmetica
        "sommare": "add", "aggiungere": "add", "sottrarre": "sub",
        "moltiplicare": "mul", "moltiplicare_segno": "imul",
        "dividere": "div", "dividere_segno": "idiv",
        "incrementare": "inc", "decrementare": "dec", "negare": "neg",
        
        # Logica
        "e": "and", "o": "or", "non": "not", "esclusivo": "xor",
        
        # Flusso
        "saltare": "jmp", "chiamare": "call", "ritornare": "ret",
        "se_uguale": "je", "se_non_uguale": "jne",
        
        # Sistema
        "interruzione": "int", "chiamata_sistema": "syscall",
    },
    
    "ar": {
        # نقل البيانات
        "نقل": "mov", "تبديل": "xchg", "تحميل_فعال": "lea",
        "توسيع_صفر": "movzx", "توسيع_إشارة": "movsx",
        
        # العمليات الحسابية
        "جمع": "add", "إضافة": "add", "طرح": "sub",
        "ضرب": "mul", "ضرب_إشارة": "imul",
        "قسمة": "div", "قسمة_إشارة": "idiv",
        "زيادة": "inc", "نقص": "dec", "نفي": "neg",
        
        # العمليات المنطقية
        "و": "and", "أو": "or", "ليس": "not", "أو_حصري": "xor",
        
        # التحكم في التدفق
        "اقفز": "jmp", "اتصل": "call", "استدعاء": "call",
        "عد": "ret", "رجوع": "ret",
        "إذا_يساوي": "je", "إذا_لا_يساوي": "jne",
        
        # المكدس
        "ادفع": "push", "اسحب": "pop",
        
        # النظام
        "مقاطعة": "int", "استدعاء_النظام": "syscall",
    },
    
    "ru": {
        # Перемещение
        "перенести": "mov", "обменять": "xchg", "загрузить_эффективный": "lea",
        "расширить_нулями": "movzx", "расширить_знаком": "movsx",
        
        # Арифметика
        "добавить": "add", "сложить": "add", "вычесть": "sub",
        "умножить": "mul", "умножить_знак": "imul",
        "разделить": "div", "разделить_знак": "idiv",
        "увеличить": "inc", "уменьшить": "dec", "отрицание": "neg",
        
        # Логика
        "и": "and", "или": "or", "не": "not", "исключающее": "xor",
        
        # Управление потоком
        "прыгнуть": "jmp", "вызвать": "call", "вернуться": "ret",
        "если_равно": "je", "если_не_равно": "jne",
        
        # Стек
        "положить": "push", "извлечь": "pop",
        
        # Система
        "прерывание": "int", "системный_вызов": "syscall",
    },
    
    "ko": {
        # 데이터 이동
        "이동": "mov", "교환": "xchg", "주소로드": "lea",
        "영확장": "movzx", "부호확장": "movsx",
        
        # 산술 연산
        "더하기": "add", "합": "add", "빼기": "sub",
        "곱하기": "mul", "부호곱하기": "imul",
        "나누기": "div", "부호나누기": "idiv",
        "증가": "inc", "감소": "dec", "부정": "neg",
        
        # 논리 연산
        "그리고": "and", "또는": "or", "배타적": "xor",
        
        # 흐름 제어
        "점프": "jmp", "호출": "call", "돌아가기": "ret",
        "같으면": "je", "다르면": "jne",
        
        # 스택
        "넣기": "push", "빼기": "pop",
        
        # 시스템
        "인터럽트": "int", "시스템호출": "syscall",
    },
    
    "id": {
        # Perpindahan Data
        "pindah": "mov", "salin": "mov", "tukar": "xchg",
        "muat_efektif": "lea", "perpanjang_nol": "movzx",
        "perpanjang_tanda": "movsx",
        
        # Aritmatika
        "tambah": "add", "jumlah": "add", "kurang": "sub",
        "kali": "mul", "kali_tanda": "imul",
        "bagi": "div", "bagi_tanda": "idiv",
        "tambah_satu": "inc", "kurang_satu": "dec", "negatif": "neg",
        
        # Logika
        "dan": "and", "atau": "or", "tidak": "not", "eksklusif": "xor",
        
        # Kontrol Alur
        "lompat": "jmp", "panggil": "call", "kembali": "ret",
        "jika_sama": "je", "jika_beda": "jne",
        
        # Tumpukan
        "masukkan": "push", "keluarkan": "pop",
        
        # Sistem
        "interupsi": "int", "panggilan_sistem": "syscall",
    },
    
    "zh": {
        # 資料移動
        "移動": "mov", "複製": "mov", "交換": "xchg",
        "載入有效位址": "lea", "零擴充": "movzx", "符號擴充": "movsx",
        
        # 算術
        "加": "add", "相加": "add", "減": "sub", "相減": "sub",
        "乘": "mul", "有符號乘": "imul",
        "除": "div", "有符號除": "idiv",
        "遞增": "inc", "遞減": "dec", "取負": "neg",
        
        # 邏輯運算
        "且": "and", "或": "or", "非": "not", "互斥或": "xor",
        
        # 流程控制
        "跳躍": "jmp", "呼叫": "call", "返回": "ret",
        "若相等": "je", "若不等": "jne",
        
        # 堆疊
        "推入": "push", "彈出": "pop",
        
        # 系統
        "中斷": "int", "系統呼叫": "syscall",
    },
    
    "ja": {
        # データ移動
        "移動": "mov", "コピー": "mov", "交換": "xchg",
        "実効アドレス読込": "lea", "ゼロ拡張": "movzx", "符号拡張": "movsx",
        
        # 算術演算
        "加算": "add", "足す": "add", "減算": "sub", "引く": "sub",
        "乗算": "mul", "符号付乗算": "imul",
        "除算": "div", "符号付除算": "idiv",
        "インクリメント": "inc", "デクリメント": "dec", "否定": "neg",
        
        # 論理演算
        "論理積": "and", "論理和": "or", "排他的論理和": "xor",
        
        # 制御フロー
        "ジャンプ": "jmp", "呼出": "call", "戻る": "ret",
        "等しければ": "je", "等しくなければ": "jne",
        
        # スタック
        "プッシュ": "push", "ポップ": "pop",
        
        # システム
        "割込": "int", "システムコール": "syscall",
    },

    "pt": {
        # Movimentação
        "mover": "mov", "copiar": "mov", "trocar": "xchg",
        "carregar_efetivo": "lea", "estender_zero": "movzx", "estender_sinal": "movsx",

        # Aritmética
        "somar": "add", "adicionar": "add", "subtrair": "sub",
        "multiplicar": "mul", "multiplicar_sinal": "imul",
        "dividir": "div", "dividir_sinal": "idiv",
        "incrementar": "inc", "decrementar": "dec", "negar": "neg",

        # Lógica
        "e": "and", "ou": "or", "nao": "not", "exclusivo": "xor",
        "deslocar_esq": "shl", "deslocar_dir": "shr",
        "rotacionar_esq": "rol", "rotacionar_dir": "ror",

        # Comparação
        "comparar": "cmp", "testar": "test",

        # Fluxo
        "desviar": "jmp", "saltar": "jmp", "chamar": "call",
        "retornar": "ret", "voltar": "ret",
        "se_igual": "je", "se_cero": "jz", "se_nao_igual": "jne", "se_nao_cero": "jnz",
        "se_maior": "jg", "se_maior_igual": "jge", "si_menor": "jl", "si_menor_igual": "jle",
        "se_acima": "ja", "se_abaixo": "jb", "se_acima_igual": "jae", "se_abaixo_igual": "jbe",
        "se_sinal": "js", "se_nao_sinal": "jns", "se_transbordo": "jo", "se_nao_transbordo": "jno",
        "se_paridade": "jp", "se_nao_paridade": "jnp",

        # Pilha
        "empilhar": "push", "desempilhar": "pop",
        "empilhar_flags": "pushf", "desempilhar_flags": "popf",

        # Sequências
        "mover_byte": "movsb", "mover_palavra": "movsw", "mover_dupla": "movsd",
        "armazenar_byte": "stosb", "cargar_byte": "lodsb", "escanear_byte": "scasb",
        "repetir": "rep", "repetir_enquanto": "repne",

        # Repetições
        "repetir_ciclo": "loop", "repetir_se_zero": "loopz", "repetir_se_nao_zero": "loopnz",

        # Sistema
        "interrupcao": "int", "chamada_sistema": "syscall",
        "retorno_sistema": "sysret", "retorno_interrupcao": "iret",

        # Miscelânea
        "nada": "nop", "parar": "hlt",
        "limpar_interrupcoes": "cli", "activar_interrupcoes": "sti",
        "limpar_direcao": "cld", "fixar_direcao": "std", "esperar": "wait",

        # Conversão
        "converter_byte_palavra": "cbw", "converter_palavra_dupla": "cwd",
        "converter_dupla_quadrupla": "cdq", "converter_quadrupla_octupla": "cqo",
    },

    "hi": {
        "bhejo": "mov", "rakho": "mov", "sthan": "mov",
        "joro": "add", "ghatao": "sub", "guna": "mul", "bhag": "div",
        "badhao": "inc", "ghatao_ek": "dec", "na": "neg",
        "aur": "and", "ya": "or", "nahi": "not", "alag": "xor",
        "tulna": "cmp", "pariksha": "test",
        "pata_load": "lea",
        "kudo": "jmp", "bulao": "call", "wapas": "ret",
        "daalo": "push", "nikalo": "pop",
        "rok": "int",
    },
    
    "tr": {
        "taşı": "mov", "kopyala": "mov", "yukle": "lea",
        "ekle": "add", "çıkar": "sub", "çarp": "mul", "böl": "div",
        "artir": "inc", "azalt": "dec", "tersle": "neg",
        "ve": "and", "veya": "or", "degil": "not", "ozel_veya": "xor",
        "karsilastir": "cmp", "sina": "test",
        "atla": "jmp", "çağır": "call", "dön": "ret",
        "it": "push", "çek": "pop",
        "kesme": "int",
    },
    
    "pl": {
        "przesun": "mov", "kopiuj": "mov", "adres": "lea",
        "dodaj": "add", "odejmij": "sub", "pomnoz": "mul", "podziel": "div",
        "zwieksz": "inc", "zmniejsz": "dec", "neguj": "neg",
        "oraz": "and", "lub": "or", "nie": "not", "xor": "xor",
        "porownaj": "cmp", "testuj": "test",
        "skocz": "jmp", "wywolaj": "call", "wroc": "ret",
        "wepchnij": "push", "zdejmij": "pop",
        "przerwanie": "int",
    },
    
    "sv": {
        "flytta": "mov", "ladda": "lea",
        "addera": "add", "subtrahera": "sub", "multiplicera": "mul", "dividera": "div",
        "oka": "inc", "minska": "dec", "negera": "neg",
        "och": "and", "eller": "or", "inte": "not", "xor": "xor",
        "jamfor": "cmp", "testa": "test",
        "hoppa": "jmp", "kalla": "call", "returnera": "ret",
        "tryck": "push", "pop": "pop",
        "avbrott": "int",
    },
    
    "nl": {
        "verplaats": "mov", "laad": "lea", "wissel": "xchg",
        "optellen": "add", "aftrekken": "sub", "vermenigvuldig": "mul", "delen": "div",
        "verhoog": "inc", "verlaag": "dec", "negeer": "neg",
        "en": "and", "of": "or", "niet": "not", "exclusief": "xor",
        "vergelijk": "cmp", "test": "test",
        "spring": "jmp", "roep": "call", "terug": "ret",
        "duw": "push", "plop": "pop",
        "onderbreking": "int",
    },
}

# ============================================================================
# MAPA INVERSO (Mnemónico Estándar -> Palabra Canónica por Idioma)
# Para modo reversible
# ============================================================================
PRETTY = {
    "es": {
        "mov": "mover", "xchg": "intercambiar", "lea": "cargar_efectivo",
        "movzx": "extender_cero", "movsx": "extender_signo",
        "add": "sumar", "sub": "restar", "mul": "multiplicar",
        "imul": "multiplicar_signado", "div": "dividir", "idiv": "dividir_signado",
        "inc": "incrementar", "dec": "decrementar", "neg": "negar",
        "and": "y", "or": "o", "not": "no", "xor": "exclusivo",
        "shl": "desplazar_izq", "shr": "desplazar_der",
        "sal": "desplazar_arit_izq", "sar": "desplazar_arit_der",
        "rol": "rotar_izq", "ror": "rotar_der",
        "cmp": "comparar", "test": "probar",
        "jmp": "saltar", "call": "llamar", "ret": "retornar",
        "je": "si_igual", "jz": "si_cero", "jne": "si_no_igual", "jnz": "si_no_cero",
        "jg": "si_mayor", "jge": "si_mayor_igual", "jl": "si_menor", "jle": "si_menor_igual",
        "ja": "si_arriba", "jb": "si_abajo", "jae": "si_arriba_igual", "jbe": "si_abajo_igual",
        "js": "si_signo", "jns": "si_no_signo", "jo": "si_desborde", "jno": "si_no_desborde",
        "jp": "si_paridad", "jnp": "si_no_paridad",
        "push": "meter", "pop": "sacar", "pushf": "meter_banderas", "popf": "sacar_banderas",
        "movsb": "mover_byte", "movsw": "mover_palabra", "movsd": "mover_doble",
        "stosb": "almacenar_byte", "lodsb": "cargar_byte", "scasb": "escanear_byte",
        "rep": "repetir", "repne": "repetir_mientras",
        "loop": "ciclo", "loopz": "ciclo_si_cero", "loopnz": "ciclo_si_no_cero",
        "int": "interrupcion", "syscall": "llamada_sistema",
        "sysret": "retorno_sistema", "iret": "retorno_interrupcion",
        "nop": "nada", "hlt": "detener",
        "cli": "limpiar_interrupciones", "sti": "activar_interrupciones",
        "cld": "limpiar_direccion", "std": "fijar_direccion", "wait": "esperar",
        "cbw": "convertir_byte_palabra", "cwd": "convertir_palabra_doble",
        "cdq": "convertir_doble_cuadruple", "cqo": "convertir_cuadruple_octo",
    },
    
    "fr": {
        "mov": "deplacer", "xchg": "echanger", "lea": "charger_effectif",
        "movzx": "etendre_zero", "movsx": "etendre_signe",
        "add": "ajouter", "sub": "soustraire", "mul": "multiplier",
        "imul": "multiplier_signe", "div": "diviser", "idiv": "diviser_signe",
        "inc": "incrementer", "dec": "decrementer", "neg": "negativer",
        "and": "et", "or": "ou", "not": "non", "xor": "ou_exclusif",
        "cmp": "comparer", "test": "tester",
        "jmp": "sauter", "call": "appeler", "ret": "retourner",
        "je": "si_egal", "jne": "si_pas_egal",
        "push": "empiler", "pop": "depiler",
        "int": "interruption", "syscall": "appel_systeme",
    },

    "pt": {
        "mov": "mover", "xchg": "trocar", "lea": "carregar_efetivo",
        "movzx": "estender_zero", "movsx": "estender_sinal",
        "add": "somar", "sub": "subtrair", "mul": "multiplicar",
        "imul": "multiplicar_sinal", "div": "dividir", "idiv": "dividir_sinal",
        "inc": "incrementar", "dec": "decrementar", "neg": "negar",
        "and": "e", "or": "ou", "not": "nao", "xor": "exclusivo",
        "shl": "deslocar_esq", "shr": "deslocar_dir",
        "rol": "rotacionar_esq", "ror": "rotacionar_dir",
        "cmp": "comparar", "test": "testar",
        "jmp": "desviar", "call": "chamar", "ret": "retornar",
        "je": "se_igual", "jz": "se_zero", "jne": "se_nao_igual", "jnz": "se_nao_zero",
        "jg": "se_maior", "jge": "se_maior_igual", "jl": "se_menor", "jle": "se_menor_igual",
        "ja": "se_acima", "jb": "se_abaixo", "jae": "se_acima_igual", "jbe": "se_abaixo_igual",
        "js": "se_sinal", "jns": "se_nao_sinal", "jo": "se_transbordo", "jno": "se_nao_transbordo",
        "jp": "se_paridade", "jnp": "se_nao_paridade",
        "push": "empilhar", "pop": "desempilhar", "pushf": "empilhar_flags", "popf": "desempilhar_flags",
        "movsb": "mover_byte", "movsw": "mover_palavra", "movsd": "mover_dupla",
        "stosb": "armazenar_byte", "lodsb": "cargar_byte", "scasb": "escanear_byte",
        "rep": "repetir", "repne": "repetir_enquanto",
        "loop": "repetir_ciclo", "loopz": "repetir_se_zero", "loopnz": "repetir_se_nao_zero",
        "int": "interrupcao", "syscall": "chamada_sistema",
        "sysret": "retorno_sistema", "iret": "retorno_interrupcao",
        "nop": "nada", "hlt": "parar",
        "cli": "limpar_interrupcoes", "sti": "ativar_interrupcoes",
        "cld": "limpar_direcao", "std": "fixar_direcao", "wait": "esperar",
        "cbw": "converter_byte_palavra", "cwd": "converter_palavra_dupla",
        "cdq": "converter_dupla_quadrupla", "cqo": "converter_quadrupla_octupla",
    },
    
    "de": {
        "mov": "bewegen", "xchg": "tauschen", "lea": "effektiv_laden",
        "movzx": "null_erweitern", "movsx": "vorzeichen_erweitern",
        "add": "addieren", "sub": "subtrahieren", "mul": "multiplizieren",
        "imul": "multiplizieren_vorzeichen", "div": "dividieren", "idiv": "dividieren_vorzeichen",
        "inc": "inkrementieren", "dec": "dekrementieren", "neg": "negieren",
        "and": "und", "or": "oder", "not": "nicht", "xor": "exklusiv_oder",
        "jmp": "springen", "call": "rufen", "ret": "zurueckkehren",
        "int": "unterbrechung",
    },
    
    "it": {
        "mov": "spostare", "xchg": "scambiare", "lea": "caricare_effettivo",
        "movzx": "estendere_zero", "movsx": "estendere_segno",
        "add": "sommare", "sub": "sottrarre", "mul": "moltiplicare",
        "imul": "moltiplicare_segno", "div": "dividere", "idiv": "dividere_segno",
        "inc": "incrementare", "dec": "decrementare", "neg": "negare",
        "and": "e", "or": "o", "not": "non", "xor": "esclusivo",
        "jmp": "saltare", "call": "chiamare", "ret": "ritornare",
        "je": "se_uguale", "jne": "se_non_uguale",
        "push": "spingere", "pop": "estrarre",
        "int": "interruzione", "syscall": "chiamata_sistema",
    },
    
    "ar": {
        "mov": "نقل", "xchg": "تبديل", "lea": "تحميل_فعال",
        "movzx": "توسيع_صفر", "movsx": "توسيع_إشارة",
        "add": "جمع", "sub": "طرح", "mul": "ضرب",
        "imul": "ضرب_إشارة", "div": "قسمة", "idiv": "قسمة_إشارة",
        "inc": "زيادة", "dec": "نقص", "neg": "نفي",
        "and": "و", "or": "أو", "not": "ليس", "xor": "أو_حصري",
        "jmp": "اقفز", "call": "استدعاء", "ret": "رجوع",
        "je": "إذا_يساوي", "jne": "إذا_لا_يساوي",
        "push": "ادفع", "pop": "اسحب",
        "int": "مقاطعة", "syscall": "استدعاء_النظام",
    },
    
    "ru": {
        "mov": "перенести", "xchg": "обменять", "lea": "загрузить_эффективный",
        "movzx": "расширить_нулями", "movsx": "расширить_знаком",
        "add": "добавить", "sub": "вычесть", "mul": "умножить",
        "imul": "умножить_знак", "div": "разделить", "idiv": "разделить_знак",
        "inc": "увеличить", "dec": "уменьшить", "neg": "отрицание",
        "and": "и", "or": "или", "not": "не", "xor": "исключающее",
        "jmp": "прыгнуть", "call": "вызвать", "ret": "вернуться",
        "je": "если_равно", "jne": "если_не_равно",
        "push": "положить", "pop": "извлечь",
        "int": "прерывание", "syscall": "системный_вызов",
    },
    
    "ko": {
        "mov": "이동", "xchg": "교환", "lea": "주소로드",
        "movzx": "영확장", "movsx": "부호확장",
        "add": "더하기", "sub": "빼기", "mul": "곱하기",
        "imul": "부호곱하기", "div": "나누기", "idiv": "부호나누기",
        "inc": "증가", "dec": "감소", "neg": "부정",
        "and": "그리고", "or": "또는", "xor": "배타적",
        "jmp": "점프", "call": "호출", "ret": "돌아가기",
        "je": "같으면", "jne": "다르면",
        "push": "넣기", "pop": "빼기",
        "int": "인터럽트", "syscall": "시스템호출",
    },
    
    "id": {
        "mov": "pindah", "xchg": "tukar", "lea": "muat_efektif",
        "movzx": "perpanjang_nol", "movsx": "perpanjang_tanda",
        "add": "tambah", "sub": "kurang", "mul": "kali",
        "imul": "kali_tanda", "div": "bagi", "idiv": "bagi_tanda",
        "inc": "tambah_satu", "dec": "kurang_satu", "neg": "negatif",
        "and": "dan", "or": "atau", "not": "tidak", "xor": "eksklusif",
        "jmp": "lompat", "call": "panggil", "ret": "kembali",
        "je": "jika_sama", "jne": "jika_beda",
        "push": "masukkan", "pop": "keluarkan",
        "int": "interupsi", "syscall": "panggilan_sistem",
    },
    
    "zh": {
        "mov": "移動", "xchg": "交換", "lea": "載入有效位址",
        "movzx": "零擴充", "movsx": "符號擴充",
        "add": "加", "sub": "減", "mul": "乘",
        "imul": "有符號乘", "div": "除", "idiv": "有符號除",
        "inc": "遞增", "dec": "遞減", "neg": "取負",
        "and": "且", "or": "或", "not": "非", "xor": "互斥或",
        "jmp": "跳躍", "call": "呼叫", "ret": "返回",
        "je": "若相等", "jne": "若不等",
        "push": "推入", "pop": "彈出",
        "int": "中斷", "syscall": "系統呼叫",
    },
    
    "ja": {
        "mov": "移動", "xchg": "交換", "lea": "実効アドレス読込",
        "movzx": "ゼロ拡張", "movsx": "符号拡張",
        "add": "加算", "sub": "減算", "mul": "乗算",
        "imul": "符号付乗算", "div": "除算", "idiv": "符号付除算",
        "inc": "インクリメント", "dec": "デクリメント", "neg": "否定",
        "and": "論理積", "or": "論理和", "xor": "排他的論理和",
        "jmp": "ジャンプ", "call": "呼出", "ret": "戻る",
        "je": "等しければ", "jne": "等しくなければ",
        "push": "プッシュ", "pop": "ポップ",
        "int": "割込", "syscall": "システムコール",
    },

    "pt": {
        "mov": "mover", "xchg": "trocar", "lea": "carregar_efetivo",
        "movzx": "estender_zero", "movsx": "estender_sinal",
        "add": "somar", "sub": "subtrair", "mul": "multiplicar",
        "imul": "multiplicar_sinal", "div": "dividir", "idiv": "dividir_sinal",
        "inc": "incrementar", "dec": "decrementar", "neg": "negar",
        "and": "e", "or": "ou", "not": "nao", "xor": "exclusivo",
        "shl": "deslocar_esq", "shr": "deslocar_dir",
        "rol": "rotacionar_esq", "ror": "rotacionar_dir",
        "cmp": "comparar", "test": "testar",
        "jmp": "desviar", "call": "chamar", "ret": "retornar",
        "je": "se_igual", "jne": "se_nao_igual",
        "jg": "se_maior", "jge": "se_maior_igual",
        "jl": "se_menor", "jle": "se_menor_igual",
        "ja": "se_acima", "jb": "se_abaixo",
        "jae": "se_acima_igual", "jbe": "se_abaixo_igual",
        "js": "se_sinal", "jns": "se_nao_sinal",
        "jo": "se_transbordo", "jno": "se_nao_transbordo",
        "jp": "se_paridade", "jnp": "se_nao_paridade",
        "push": "empilhar", "pop": "desempilhar",
        "pushf": "empilhar_flags", "popf": "desempilhar_flags",
        "movsb": "mover_byte", "movsw": "mover_palavra", "movsd": "mover_dupla",
        "stosb": "armazenar_byte", "lodsb": "cargar_byte", "scasb": "escanear_byte",
        "rep": "repetir", "repne": "repetir_enquanto",
        "loop": "repetir_ciclo", "loopz": "repetir_se_zero",
        "loopnz": "repetir_se_nao_zero",
        "int": "interrupcao", "syscall": "chamada_sistema",
        "sysret": "retorno_sistema", "iret": "retorno_interrupcao",
        "nop": "nada", "hlt": "parar",
        "cli": "limpar_interrupcoes", "sti": "activar_interrupcoes",
        "cld": "limpiar_direcao", "std": "fixar_direcao", "wait": "esperar",
        "cbw": "converter_byte_palavra", "cwd": "converter_palavra_dupla",
        "cdq": "converter_dupla_quadrupla", "cqo": "converter_quadrupla_octupla",
    },

    "hi": {
        "mov": "bhejo", "add": "joro", "sub": "ghatao",
        "jmp": "kudo", "call": "bulao", "ret": "wapas",
        "and": "aur", "or": "ya", "not": "nahi",
        "cmp": "tulna", "test": "pariksha",
        "inc": "badhao", "dec": "ghatao_ek",
    },
    
    "tr": {
        "mov": "taşı", "add": "ekle", "sub": "çıkar",
        "jmp": "atla", "call": "çağır", "ret": "dön",
        "and": "ve", "or": "veya", "not": "degil",
        "cmp": "karsilastir", "test": "sina",
        "inc": "artir", "dec": "azalt",
    },
    
    "pl": {
        "mov": "przesun", "add": "dodaj", "sub": "odejmij",
        "jmp": "skocz", "call": "wywolaj", "ret": "wroc",
        "and": "oraz", "or": "lub", "not": "nie",
        "cmp": "porownaj", "test": "testuj",
        "inc": "zwieksz", "dec": "zmniejsz",
    },
    
    "sv": {
        "mov": "flytta", "add": "addera", "sub": "subtrahera",
        "jmp": "hoppa", "call": "kalla", "ret": "returnera",
        "and": "och", "or": "eller", "not": "inte",
        "cmp": "jamfor", "test": "testa",
        "inc": "oka", "dec": "minska",
    },
    
    "nl": {
        "mov": "verplaats", "add": "optellen", "sub": "aftrekken",
        "jmp": "spring", "call": "roep", "ret": "terug",
        "and": "en", "or": "of", "not": "niet",
        "cmp": "vergelijk", "test": "test",
        "inc": "verhoog", "dec": "verlaag",
    },
}

ERRORS = {
    "en": {
        "file_not_found": "❌ Error: File '{}' not found",
        "io_error": "❌ Unexpected Error: {}",
        "auto_detect_ok": "🔍 Auto-Detect: Identified Language -> {}",
        "auto_detect_fail": "⚠️ Auto-Detect: Could not identify language. Defaulting to 'en'.",
        "success": "   Status: ✅ OK",
        "mode_native": "Native (View)",
        "mode_standard": "Standard (NASM)"
    },
    "es": {
        "file_not_found": "❌ Error: No se encontró el archivo '{}'",
        "io_error": "❌ Error inesperado: {}",
        "auto_detect_ok": "🔍 Auto-Detect: Idioma identificado -> {}",
        "auto_detect_fail": "⚠️ Auto-Detect: No se pudo identificar el idioma. Usando 'en' (Standard).",
        "success": "   Estado: ✅ OK",
        "mode_native": "Natificado (Vista)",
        "mode_standard": "Estándar (NASM)"
    }
}
# Default to English for other languages for now
for l in TABLE:
    if l not in ERRORS:
        ERRORS[l] = ERRORS["en"]

def get_msg(key, lang, *args):
    """Retrieve localized message"""
    # Fallback to English if language not supported in ERRORS
    msgs = ERRORS.get(lang, ERRORS["en"])
    msg = msgs.get(key, ERRORS["en"][key])
    msg = msgs.get(key, ERRORS["en"][key])
    return msg.format(*args)

def process_macros(code):
    """
    Procesa macros simples (%define CLAVE VALOR)
    Retorna el código con las sustituciones aplicadas.
    """
    lines = code.split('\n')
    processed_lines = []
    macros = {}
    
    # 1. Scanner de definiciones
    for line in lines:
        line_strip = line.strip()
        
        # Detectar %define
        if line_strip.lower().startswith('%define'):
            parts = line_strip.split(None, 2)
            if len(parts) >= 3:
                key = parts[1]
                val = parts[2]
                macros[key] = val
            continue # No añadir la línea de definición al output final
            
        processed_lines.append(line)
        
    # 2. Reemplazo (naive string replacement)
    final_code = '\n'.join(processed_lines)
    
    if not macros:
        return final_code
        
    for key, val in macros.items():
        # Usar regex para reemplazar solo palabras completas
        pattern = r'(?<!\w)' + re.escape(key) + r'(?!\w)'
        final_code = re.sub(pattern, val, final_code)
        
    return final_code

def translate_token(token, lang):
    """
    Traduce un token del idioma nativo al mnemónico estándar.
    
    Fallback:
    1. Si está en TABLE[lang] -> traduce
    2. Si es mnemónico estándar en INSTRUCTIONS -> deja tal cual
    3. Si no, devuelve tal cual (etiquetas, registros, números, etc.)
    """
    # Intentar traducción desde tabla de idioma
    if lang in TABLE and token in TABLE[lang]:
        return TABLE[lang][token]
    
    # Si ya es un mnemónico estándar, dejarlo tal cual
    if token in INSTRUCTIONS:
        return token
    
    # Cualquier otro caso (etiquetas, registros, números)
    return token

def pretty_mnemonic(mnemonic, lang):
    """
    Convierte un mnemónico estándar a su forma nativa para visualización.
    
    Fallback:
    - Si existe en PRETTY[lang] -> usa la forma nativa
    - Si no, devuelve el mnemónico estándar
    """
    if lang in PRETTY and mnemonic in PRETTY[lang]:
        return PRETTY[lang][mnemonic]
    return mnemonic

def translate(code, lang, to_standard=True):
    """Traduce código entre mnemónicos nativos y estándar"""
    
    # PROCESAR MACROS (Si estamos traduciendo código fuente)
    if to_standard:
        code = process_macros(code)
        
    lines = code.split('\n')
    translated_lines = []
    
    for line in lines:
        # Preservar comentarios
        comment = ""
        if ';' in line:
            line, comment = line.split(';', 1)
            comment = ';' + comment
        
        # Regex robusto: soporta etiquetas, puntos, guiones, símbolos Unicode
        match = re.match(r'^(\s*)([A-Za-zÀ-ÿ_\.0-9À-ỹ가-힣一-龯ぁ-ゔァ-ヴー々〆〤]+)(.*)', line)
        if match:
            indent, token, rest = match.groups()
            token_lower = token.lower()
            
            if to_standard:
                # Modo: Nativo -> Estándar
                translated_token = translate_token(token_lower, lang)
            else:
                # Modo: Estándar -> Nativo (reversible)
                translated_token = pretty_mnemonic(token_lower, lang)
            
            translated_lines.append(f"{indent}{translated_token}{rest}{comment}")
        else:
            translated_lines.append(line + comment)
            
    return '\n'.join(translated_lines)



def detect_language(code):
    """
    Detecta automáticamente el idioma del código fuente basándose en la frecuencia de palabras clave.
    """
    scores = {lang: 0 for lang in TABLE.keys()}
    
    # Tokenizar todo el código (palabras simples)
    tokens = re.findall(r'[A-Za-zÀ-ÿ_\.0-9]+', code.lower())
    
    for token in tokens:
        for lang, keywords in TABLE.items():
            if token in keywords:
                scores[lang] += 1
                
    # Encontrar el idioma con más coincidencias
    best_lang = max(scores, key=scores.get)
    
    # Si no hay coincidencias claras (score 0), asumir 'es' o error?
    if scores[best_lang] == 0:
        return None
        
    return best_lang

def main():
    if len(sys.argv) < 4:
        print("🛡️ MultiLang-ASM v0.3")
        print("Uso: python mlasm.py <idioma> <entrada> <salida> [--reverse]")
        print("\nIdiomas: es, fr, it, ar, de, ru, ko, id, zh, ja, pt")
        return

    lang = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    reverse = "--reverse" in sys.argv

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # LOGICA AUTO-DETECT
        if lang == 'auto':
            detected = detect_language(content)
            if detected:
                lang = detected
                print(get_msg("auto_detect_ok", lang, lang.upper()))
            else:
                print(get_msg("auto_detect_fail", "en"))
                lang = 'en'

        # MACROS (Ahora se procesan dentro de translate)
        translated = translate(content, lang, to_standard=not reverse)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated)

        # Mensajes humanos mejorados
        mode = get_msg("mode_native" if reverse else "mode_standard", lang)
        
        print(f"🛡️ MultiLang-ASM v0.4-dev")
        print(f"   Idioma: {lang.upper()}")
        print(f"   Modo: {mode}")
        print(f"   Entrada: {input_file}")
        print(f"   Salida: {output_file}")
        print(f"{get_msg('success', lang)}")

    except FileNotFoundError:
        # Try to use 'lang' if set, else 'en'
        print(get_msg("file_not_found", lang if lang != 'auto' else 'en', input_file))
    except Exception as e:
        print(get_msg("io_error", lang if lang != 'auto' else 'en', e))

if __name__ == "__main__":
    main()
