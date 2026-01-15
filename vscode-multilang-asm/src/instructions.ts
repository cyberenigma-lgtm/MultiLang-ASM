export interface SystemInstruction {
    name: string;
    standard: string;
    description: string;
    snippet: string;
}

export const INSTRUCTIONS: { [key: string]: { [key: string]: SystemInstruction } } = {
    // 1. ESPAÑOL (ES)
    "es": {
        "mover": { name: "mover", standard: "mov", description: "Mover datos (mov)", snippet: "mover ${1:rax}, ${2:valeur}" },
        "copiar": { name: "copiar", standard: "mov", description: "Copiar datos (mov)", snippet: "copiar ${1:rax}, ${2:valeur}" },
        "sumar": { name: "sumar", standard: "add", description: "Sumar (add)", snippet: "sumar ${1:rax}, ${2:valeur}" },
        "restar": { name: "restar", standard: "sub", description: "Restar (sub)", snippet: "restar ${1:rax}, ${2:valeur}" },
        "multiplicar": { name: "multiplicar", standard: "mul", description: "Multiplicar (mul)", snippet: "multiplicar ${1:rax}" },
        "dividir": { name: "dividir", standard: "div", description: "Dividir (div)", snippet: "dividir ${1:rax}" },
        "saltar": { name: "saltar", standard: "jmp", description: "Saltar incondicionalmente (jmp)", snippet: "saltar ${1:etiqueta}" },
        "llamar": { name: "llamar", standard: "call", description: "Llamar subrutina (call)", snippet: "llamar ${1:funcion}" },
        "retornar": { name: "retornar", standard: "ret", description: "Retornar de subrutina (ret)", snippet: "retornar" },
        "comparar": { name: "comparar", standard: "cmp", description: "Comparar (cmp)", snippet: "comparar ${1:rax}, ${2:rbx}" },
        // Stack
        "empujar": { name: "empujar", standard: "push", description: "Empujar a pila (push)", snippet: "empujar ${1:rax}" },
        "sacar": { name: "sacar", standard: "pop", description: "Sacar de pila (pop)", snippet: "sacar ${1:rax}" },
        // Logic
        "y": { name: "y", standard: "and", description: "Lógica Y (and)", snippet: "y ${1:rax}, ${2:rbx}" },
        "o": { name: "o", standard: "or", description: "Lógica O (or)", snippet: "o ${1:rax}, ${2:rbx}" },
        "xor": { name: "xor", standard: "xor", description: "Lógica XOR (xor)", snippet: "xor ${1:rax}, ${2:rbx}" },
        "no": { name: "no", standard: "not", description: "Lógica NO (not)", snippet: "no ${1:rax}" },
        // Arithmetic
        "incrementar": { name: "incrementar", standard: "inc", description: "Incrementar (inc)", snippet: "incrementar ${1:rax}" },
        "decrementar": { name: "decrementar", standard: "dec", description: "Decrementar (dec)", snippet: "decrementar ${1:rax}" },
        // Control Flow
        "si_igual": { name: "si_igual", standard: "je", description: "Saltar si igual (je)", snippet: "si_igual ${1:etiqueta}" },
        "si_distinto": { name: "si_distinto", standard: "jne", description: "Saltar si distinto (jne)", snippet: "si_distinto ${1:etiqueta}" },
        "si_mayor": { name: "si_mayor", standard: "jg", description: "Saltar si mayor (jg)", snippet: "si_mayor ${1:etiqueta}" },
        "si_menor": { name: "si_menor", standard: "jl", description: "Saltar si menor (jl)", snippet: "si_menor ${1:etiqueta}" },
        "bucle": { name: "bucle", standard: "loop", description: "Bucle (loop)", snippet: "bucle ${1:etiqueta}" }
    },
    // 2. ENGLISH (Standard fallback)
    "en": {
        "mov": { name: "mov", standard: "mov", description: "Move data", snippet: "mov ${1:rax}, ${2:valeur}" },
        "add": { name: "add", standard: "add", description: "Add", snippet: "add ${1:rax}, ${2:valeur}" },
        "sub": { name: "sub", standard: "sub", description: "Subtract", snippet: "sub ${1:rax}, ${2:valeur}" },
        "mul": { name: "mul", standard: "mul", description: "Multiply", snippet: "mul ${1:rax}" },
        "div": { name: "div", standard: "div", description: "Divide", snippet: "div ${1:rax}" },
        "jmp": { name: "jmp", standard: "jmp", description: "Jump", snippet: "jmp ${1:label}" },
        "cmp": { name: "cmp", standard: "cmp", description: "Compare", snippet: "cmp ${1:rax}, ${2:rbx}" },
        "push": { name: "push", standard: "push", description: "Push to Stack", snippet: "push ${1:rax}" },
        "pop": { name: "pop", standard: "pop", description: "Pop from Stack", snippet: "pop ${1:rax}" },
        "inc": { name: "inc", standard: "inc", description: "Increment", snippet: "inc ${1:rax}" },
        "dec": { name: "dec", standard: "dec", description: "Decrement", snippet: "dec ${1:rax}" },
        "and": { name: "and", standard: "and", description: "Logical AND", snippet: "and ${1:rax}, ${2:rbx}" },
        "or": { name: "or", standard: "or", description: "Logical OR", snippet: "or ${1:rax}, ${2:rbx}" },
        "xor": { name: "xor", standard: "xor", description: "Logical XOR", snippet: "xor ${1:rax}, ${2:rbx}" },
        "not": { name: "not", standard: "not", description: "Logical NOT", snippet: "not ${1:rax}" },
        "je": { name: "je", standard: "je", description: "Jump if Equal", snippet: "je ${1:label}" },
        "jne": { name: "jne", standard: "jne", description: "Jump if Not Equal", snippet: "jne ${1:label}" },
        "jg": { name: "jg", standard: "jg", description: "Jump if Greater", snippet: "jg ${1:label}" },
        "jl": { name: "jl", standard: "jl", description: "Jump if Less", snippet: "jl ${1:label}" },
        "loop": { name: "loop", standard: "loop", description: "Loop", snippet: "loop ${1:label}" },
        "call": { name: "call", standard: "call", description: "Call Function", snippet: "call ${1:func}" },
        "ret": { name: "ret", standard: "ret", description: "Return", snippet: "ret" }
    },
    // 3. FRANÇAIS (FR)
    "fr": {
        "deplacer": { name: "deplacer", standard: "mov", description: "Déplacer (mov)", snippet: "deplacer ${1:rax}, ${2:valeur}" },
        "ajouter": { name: "ajouter", standard: "add", description: "Ajouter (add)", snippet: "ajouter ${1:rax}, ${2:valeur}" },
        "soustraire": { name: "soustraire", standard: "sub", description: "Soustraire (sub)", snippet: "soustraire ${1:rax}, ${2:valeur}" },
        "sauter": { name: "sauter", standard: "jmp", description: "Sauter (jmp)", snippet: "sauter ${1:etiquette}" }
    },
    // 4. DEUTSCH (DE)
    "de": {
        "bewegen": { name: "bewegen", standard: "mov", description: "Bewegen (mov)", snippet: "bewegen ${1:rax}, ${2:wert}" },
        "addieren": { name: "addieren", standard: "add", description: "Addieren (add)", snippet: "addieren ${1:rax}, ${2:wert}" },
        "subtrahieren": { name: "subtrahieren", standard: "sub", description: "Subtrahieren (sub)", snippet: "subtrahieren ${1:rax}, ${2:wert}" },
        "springen": { name: "springen", standard: "jmp", description: "Springen (jmp)", snippet: "springen ${1:label}" }
    },
    // 5. ITALIANO (IT)
    "it": {
        "spostare": { name: "spostare", standard: "mov", description: "Spostare (mov)", snippet: "spostare ${1:rax}, ${2:valore}" },
        "sommare": { name: "sommare", standard: "add", description: "Sommare (add)", snippet: "sommare ${1:rax}, ${2:valore}" },
        "saltare": { name: "saltare", standard: "jmp", description: "Saltare (jmp)", snippet: "saltare ${1:etichetta}" }
    },
    // 6. PORTUGUÊS (PT)
    "pt": {
        "mover": { name: "mover", standard: "mov", description: "Mover (mov)", snippet: "mover ${1:rax}, ${2:valor}" },
        "somar": { name: "somar", standard: "add", description: "Somar (add)", snippet: "somar ${1:rax}, ${2:valor}" },
        "desviar": { name: "desviar", standard: "jmp", description: "Desviar (jmp)", snippet: "desviar ${1:rotulo}" }
    },
    // 7. RUSSIAN (RU)
    "ru": {
        "перенести": { name: "перенести", standard: "mov", description: "Перенести (mov)", snippet: "перенести ${1:rax}, ${2:val}" },
        "добавить": { name: "добавить", standard: "add", description: "Добавить (add)", snippet: "добавить ${1:rax}, ${2:val}" },
        "прыгнуть": { name: "прыгнуть", standard: "jmp", description: "Прыгнуть (jmp)", snippet: "прыгнуть ${1:label}" }
    },
    // 8. ARABIC (AR)
    "ar": {
        "نقل": { name: "نقل", standard: "mov", description: "Move (mov)", snippet: "نقل ${1:rax}, ${2:val}" },
        "جمع": { name: "جمع", standard: "add", description: "Add (add)", snippet: "جمع ${1:rax}, ${2:val}" }
    },
    // 9. JAPANESE (JA)
    "ja": {
        "移動": { name: "移動", standard: "mov", description: "移動 (mov)", snippet: "移動 ${1:rax}, ${2:val}" },
        "加算": { name: "加算", standard: "add", description: "加算 (add)", snippet: "加算 ${1:rax}, ${2:val}" },
        "ジャンプ": { name: "ジャンプ", standard: "jmp", description: "ジャンプ (jmp)", snippet: "ジャンプ ${1:label}" }
    },
    // 10. CHINESE (ZH)
    "zh": {
        "移動": { name: "移動", standard: "mov", description: "移動 (mov)", snippet: "移動 ${1:rax}, ${2:val}" },
        "加": { name: "加", standard: "add", description: "加 (add)", snippet: "加 ${1:rax}, ${2:val}" }
    },
    // 11. KOREAN (KO)
    "ko": {
        "이동": { name: "이동", standard: "mov", description: "이동 (mov)", snippet: "이동 ${1:rax}, ${2:val}" },
        "더하기": { name: "더하기", standard: "add", description: "더하기 (add)", snippet: "더하기 ${1:rax}, ${2:val}" }
    },
    // 12. INDONESIAN (ID)
    "id": {
        "pindah": { name: "pindah", standard: "mov", description: "Pindah (mov)", snippet: "pindah ${1:rax}, ${2:val}" },
        "tambah": { name: "tambah", standard: "add", description: "Tambah (add)", snippet: "tambah ${1:rax}, ${2:val}" }
    },
    // 13. HINDI (HI)
    "hi": {
        "bhejo": { name: "bhejo", standard: "mov", description: "Bhejo (mov)", snippet: "bhejo ${1:rax}, ${2:val}" },
        "joro": { name: "joro", standard: "add", description: "Joro (add)", snippet: "joro ${1:rax}, ${2:val}" }
    },
    // 14. TURKISH (TR)
    "tr": {
        "taşı": { name: "taşı", standard: "mov", description: "Taşı (mov)", snippet: "taşı ${1:rax}, ${2:val}" },
        "ekle": { name: "ekle", standard: "add", description: "Ekle (add)", snippet: "ekle ${1:rax}, ${2:val}" }
    },
    // 15. POLISH (PL)
    "pl": {
        "przesun": { name: "przesun", standard: "mov", description: "Przesuń (mov)", snippet: "przesun ${1:rax}, ${2:val}" },
        "dodaj": { name: "dodaj", standard: "add", description: "Dodaj (add)", snippet: "dodaj ${1:rax}, ${2:val}" }
    },
    // 16. SWEDISH (SV)
    "sv": {
        "flytta": { name: "flytta", standard: "mov", description: "Flytta (mov)", snippet: "flytta ${1:rax}, ${2:val}" },
        "addera": { name: "addera", standard: "add", description: "Addera (add)", snippet: "addera ${1:rax}, ${2:val}" }
    },
    // 17. DUTCH (NL)
    "nl": {
        "verplaats": { name: "verplaats", standard: "mov", description: "Verplaats (mov)", snippet: "verplaats ${1:rax}, ${2:val}" },
        "optellen": { name: "optellen", standard: "add", description: "Optellen (add)", snippet: "optellen ${1:rax}, ${2:val}" }
    },
    // 18. GREEK (EL)
    "el": {
        "kounise": { name: "kounise", standard: "mov", description: "Μετακίνηση (mov)", snippet: "kounise ${1:rax}, ${2:timi}" },
        "prosthese": { name: "prosthese", standard: "add", description: "Πρόσθεση (add)", snippet: "prosthese ${1:rax}, ${2:timi}" }
    },
    // 19. HEBREW (HE)
    "he": {
        "hazez": { name: "hazez", standard: "mov", description: "הזז (mov)", snippet: "hazez ${1:rax}, ${2:val}" },
        "hosef": { name: "hosef", standard: "add", description: "הוסף (add)", snippet: "hosef ${1:rax}, ${2:val}" }
    },
    // 20. THAI (TH)
    "th": {
        "yayi": { name: "yayi", standard: "mov", description: "ย้าย (mov)", snippet: "yayi ${1:rax}, ${2:val}" },
        "buak": { name: "buak", standard: "add", description: "บวก (add)", snippet: "buak ${1:rax}, ${2:val}" }
    },
    // 21. VIETNAMESE (VI)
    "vi": {
        "dic_chuyen": { name: "dic_chuyen", standard: "mov", description: "Di chuyển (mov)", snippet: "dic_chuyen ${1:rax}, ${2:val}" },
        "cong": { name: "cong", standard: "add", description: "Cộng (add)", snippet: "cong ${1:rax}, ${2:val}" }
    },
    // 22. SWAHILI (SW) - Africa
    "sw": {
        "songa": { name: "songa", standard: "mov", description: "Songa (mov)", snippet: "songa ${1:rax}, ${2:thamani}" },
        "ongeza": { name: "ongeza", standard: "add", description: "Ongeza (add)", snippet: "ongeza ${1:rax}, ${2:thamani}" }
    },
    // 23. TAGALOG (TL) - Philippines
    "tl": {
        "lipat": { name: "lipat", standard: "mov", description: "Lipat (mov)", snippet: "lipat ${1:rax}, ${2:halaga}" },
        "dagdag": { name: "dagdag", standard: "add", description: "Dagdag (add)", snippet: "dagdag ${1:rax}, ${2:halaga}" }
    },
    // 24. MALAY (MS)
    "ms": {
        "gerak": { name: "gerak", standard: "mov", description: "Gerak (mov)", snippet: "gerak ${1:rax}, ${2:nilai}" },
        "tambah": { name: "tambah", standard: "add", description: "Tambah (add)", snippet: "tambah ${1:rax}, ${2:nilai}" }
    },
    // 25. PERSIAN (FA)
    "fa": {
        "harekat": { name: "harekat", standard: "mov", description: "حرکت (mov)", snippet: "harekat ${1:rax}, ${2:val}" },
        "ezafe": { name: "ezafe", standard: "add", description: "اضافه (add)", snippet: "ezafe ${1:rax}, ${2:val}" }
    },
    // 26. UKRAINIAN (UK)
    "uk": {
        "peremisty": { name: "peremisty", standard: "mov", description: "Перемістити (mov)", snippet: "peremisty ${1:rax}, ${2:val}" },
        "doday": { name: "doday", standard: "add", description: "Додати (add)", snippet: "doday ${1:rax}, ${2:val}" }
    },
    // 27. ROMANIAN (RO)
    "ro": {
        "muta": { name: "muta", standard: "mov", description: "Mută (mov)", snippet: "muta ${1:rax}, ${2:val}" },
        "adauga": { name: "adauga", standard: "add", description: "Adaugă (add)", snippet: "adauga ${1:rax}, ${2:val}" }
    }
};

export const KIDS_INSTRUCTIONS: { [key: string]: SystemInstruction[] } = {
    // KIDS MODE - ESPAÑOL
    "es": [
        { name: "pon", standard: "mov", description: "🧸 Pon un valor (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita un valor (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma un valor (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta un valor (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "enseña", standard: "print", description: "🧸 Enseña el valor (print)", snippet: "enseña ${1:rax}" },
        { name: "mueve", standard: "jmp", description: "🧸 Mueve a otro sitio (jmp)", snippet: "mueve ${1:sitio}" }
    ],
    // KIDS MODE - CATALAN
    "ca": [
        { name: "posa", standard: "mov", description: "🧸 Posa un valor (mov)", snippet: "posa ${1:rax} a ${2:5}" },
        { name: "treu", standard: "sub", description: "🧸 Treu un valor (sub)", snippet: "treu ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma un valor (add)", snippet: "suma ${1:rax} amb ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta un valor (sub)", snippet: "resta ${1:rax} amb ${2:2}" },
        { name: "mostra", standard: "print", description: "🧸 Mostra el valor (print)", snippet: "mostra ${1:rax}" },
        { name: "mou", standard: "jmp", description: "🧸 Mou a un altre lloc (jmp)", snippet: "mou ${1:lloc}" }
    ],
    // KIDS MODE - EUSKERA
    "eu": [
        { name: "jarri", standard: "mov", description: "🧸 Jarri balio bat (mov)", snippet: "jarri ${1:rax} ${2:5}era" },
        { name: "kendu", standard: "sub", description: "🧸 Kendu balio bat (sub)", snippet: "kendu ${1:rax} ${2:10}etik" },
        { name: "gehitu", standard: "add", description: "🧸 Gehitu balio bat (add)", snippet: "gehitu ${1:rax} ${2:3}rekin" },
        { name: "erakutsi", standard: "print", description: "🧸 Erakutsi balioa (print)", snippet: "erakutsi ${1:rax}" },
        { name: "mugitu", standard: "jmp", description: "🧸 Mugitu beste leku batera (jmp)", snippet: "mugitu ${1:lekua}" }
    ],
    // KIDS MODE - GALLEGO
    "gl": [
        { name: "pon", standard: "mov", description: "🧸 Pon un valor (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita un valor (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma un valor (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta un valor (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "mostra", standard: "print", description: "🧸 Mostra o valor (print)", snippet: "mostra ${1:rax}" },
        { name: "move", standard: "jmp", description: "🧸 Move a outro sitio (jmp)", snippet: "move ${1:sitio}" }
    ],
    // KIDS MODE - ASTURIANU (AST)
    "ast": [
        { name: "pon", standard: "mov", description: "🧸 Pon un valor (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita un valor (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma un valor (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta un valor (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "amuesa", standard: "print", description: "🧸 Amuesa'l valor (print)", snippet: "amuesa ${1:rax}" },
        { name: "mueve", standard: "jmp", description: "🧸 Mueve a otru sitiu (jmp)", snippet: "mueve ${1:sitiu}" }
    ],
    // KIDS MODE - VALENCIÀ (VAL)
    "val": [
        { name: "posa", standard: "mov", description: "🧸 Posa un valor (mov)", snippet: "posa ${1:rax} a ${2:5}" },
        { name: "lleva", standard: "sub", description: "🧸 Lleva un valor (sub)", snippet: "lleva ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma un valor (add)", snippet: "suma ${1:rax} amb ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta un valor (sub)", snippet: "resta ${1:rax} amb ${2:2}" },
        { name: "ensenyat", standard: "print", description: "🧸 Ensenya el valor (print)", snippet: "ensenyat ${1:rax}" },
        { name: "mou", standard: "jmp", description: "🧸 Mou a un altre lloc (jmp)", snippet: "mou ${1:lloc}" }
    ],
    // KIDS MODE - ANDALÚ (AND - Estándar Técnico)
    "and": [
        { name: "pon", standard: "mov", description: "🧸 Pon (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "enseña", standard: "print", description: "🧸 Enseña (print)", snippet: "enseña ${1:rax}" },
        { name: "mueve", standard: "jmp", description: "🧸 Mueve (jmp)", snippet: "mueve ${1:sitio}" }
    ],
    // KIDS MODE - MADRILEÑO (MAD - Slang)
    "mad": [
        { name: "pon_mazo", standard: "mov", description: "🧸 Pon mazo valor (mov)", snippet: "pon_mazo ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita valor (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma valor (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta valor (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "farda", standard: "print", description: "🧸 Farda del valor (print)", snippet: "farda ${1:rax}" },
        { name: "pirate", standard: "jmp", description: "🧸 Pírate a otro lado (jmp)", snippet: "pirate ${1:lado}" }
    ],
    // KIDS MODE - SEVILLANO (SEV - Estándar Técnico)
    "sev": [
        { name: "pon", standard: "mov", description: "🧸 Pon (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "enseña", standard: "print", description: "🧸 Enseña (print)", snippet: "enseña ${1:rax}" },
        { name: "mueve", standard: "jmp", description: "🧸 Mueve (jmp)", snippet: "mueve ${1:sitio}" }
    ],
    // KIDS MODE - GADITANO (GAD - Estándar Técnico)
    "gad": [
        { name: "pon", standard: "mov", description: "🧸 Pon (mov)", snippet: "pon ${1:rax} a ${2:5}" },
        { name: "quita", standard: "sub", description: "🧸 Quita (sub)", snippet: "quita ${1:rax} de ${2:10}" },
        { name: "suma", standard: "add", description: "🧸 Suma (add)", snippet: "suma ${1:rax} con ${2:3}" },
        { name: "resta", standard: "sub", description: "🧸 Resta (sub)", snippet: "resta ${1:rax} con ${2:2}" },
        { name: "enseña", standard: "print", description: "🧸 Enseña (print)", snippet: "enseña ${1:rax}" },
        { name: "mueve", standard: "jmp", description: "🧸 Mueve (jmp)", snippet: "mueve ${1:sitio}" }
    ],
    // --- ENGLISH DIALECTS ---
    // COCKNEY (London rhyming slang / street)
    "en_cockney": [
        { name: "stash", standard: "mov", description: "🧸 Stash it (mov)", snippet: "stash ${1:rax} with ${2:5}" },
        { name: "pinch", standard: "sub", description: "🧸 Pinch some (sub)", snippet: "pinch ${1:rax} from ${2:10}" },
        { name: "add_up", standard: "add", description: "🧸 Add up (add)", snippet: "add_up ${1:rax} with ${2:3}" },
        { name: "butchers", standard: "print", description: "🧸 Have a butchers (look/print)", snippet: "butchers ${1:rax}" },
        { name: "scarper", standard: "jmp", description: "🧸 Scarper to (jmp)", snippet: "scarper ${1:place}" }
    ],
    // AUSTRALIAN (Aussie)
    "en_aus": [
        { name: "chuck", standard: "mov", description: "🧸 Chuck it in (mov)", snippet: "chuck ${1:rax} in ${2:5}" },
        { name: "nick", standard: "sub", description: "🧸 Nick some (sub)", snippet: "nick ${1:rax} off ${2:10}" },
        { name: "reckon", standard: "cmp", description: "🧸 Reckon? (cmp)", snippet: "reckon ${1:rax} with ${2:3}" },
        { name: "show_us", standard: "print", description: "🧸 Show us (print)", snippet: "show_us ${1:rax}" },
        { name: "walkabout", standard: "jmp", description: "🧸 Go walkabout (jmp)", snippet: "walkabout ${1:place}" }
    ],
    // TEXAN (Southern US)
    "en_tx": [
        { name: "put_yall", standard: "mov", description: "🧸 Put y'all (mov)", snippet: "put_yall ${1:rax} ${2:5}" },
        { name: "take", standard: "sub", description: "🧸 Take (sub)", snippet: "take ${1:rax} from ${2:10}" },
        { name: "add", standard: "add", description: "🧸 Add (add)", snippet: "add ${1:rax} and ${2:3}" },
        { name: "hollar", standard: "print", description: "🧸 Hollar (print)", snippet: "hollar ${1:rax}" },
        { name: "giddyup", standard: "jmp", description: "🧸 Giddyup to (jmp)", snippet: "giddyup ${1:place}" }
    ],
    // --- FRENCH DIALECTS ---
    // QUEBECOIS (QC)
    "fr_qc": [
        { name: "sacrer", standard: "mov", description: "🧸 Sacrer dedans (mov)", snippet: "sacrer ${1:rax} a ${2:5}" },
        { name: "oter", standard: "sub", description: "🧸 Ôter (sub)", snippet: "oter ${1:rax} de ${2:10}" },
        { name: "ajouter", standard: "add", description: "🧸 Ajouter (add)", snippet: "ajouter ${1:rax} avec ${2:3}" },
        { name: "checker", standard: "print", description: "🧸 Checker ça (print)", snippet: "checker ${1:rax}" },
        { name: "envoye", standard: "jmp", description: "🧸 Envoye à (jmp)", snippet: "envoye ${1:place}" }
    ],
    // --- GERMAN DIALECTS ---
    // BAVARIAN (Bayrisch)
    "de_bay": [
        { name: "pack", standard: "mov", description: "🧸 Pack's nei (mov)", snippet: "pack ${1:rax} ${2:5}" },
        { name: "nimm", standard: "sub", description: "🧸 Nimm weg (sub)", snippet: "nimm ${1:rax} von ${2:10}" },
        { name: "dazua", standard: "add", description: "🧸 Dazua (add)", snippet: "dazua ${1:rax} mit ${2:3}" },
        { name: "guck", standard: "print", description: "🧸 Guck (print)", snippet: "guck ${1:rax}" },
        { name: "hupf", standard: "jmp", description: "🧸 Hupf (jmp)", snippet: "hupf ${1:platz}" }
    ],
    // --- ITALIAN DIALECTS ---
    // NEAPOLITAN (Napulitano)
    "it_nap": [
        { name: "miett", standard: "mov", description: "🧸 Miett (mov)", snippet: "miett ${1:rax} a ${2:5}" },
        { name: "liva", standard: "sub", description: "🧸 Liva (sub)", snippet: "liva ${1:rax} a ${2:10}" },
        { name: "auciellia", standard: "add", description: "🧸 Auciellia (add)", snippet: "auciellia ${1:rax} co ${2:3}" },
        { name: "vide", standard: "print", description: "🧸 Vide (print)", snippet: "vide ${1:rax}" },
        { name: "fuije", standard: "jmp", description: "🧸 Fuije a (jmp)", snippet: "fuije ${1:ddu}" }
    ],
    // --- JAPANESE DIALECTS ---
    // KANSAI-BEN (Osaka/Kyoto)
    "ja_kan": [
        { name: "irete", standard: "mov", description: "🧸 Irete-ya (mov)", snippet: "irete ${1:rax} ${2:5}" },
        { name: "hiite", standard: "sub", description: "🧸 Hiite-ya (sub)", snippet: "hiite ${1:rax} ${2:10}" },
        { name: "tashite", standard: "add", description: "🧸 Tashite-ya (add)", snippet: "tashite ${1:rax} ${2:3}" },
        { name: "misete", standard: "print", description: "🧸 Misete-ya (print)", snippet: "misete ${1:rax}" },
        { name: "tonde", standard: "jmp", description: "🧸 Tonde-ya (jmp)", snippet: "tonde ${1:basyo}" }
    ],
    // --- CHINESE DIALECTS ---
    // CANTONESE (Hong Kong)
    "zh_yue": [
        { name: "bai", standard: "mov", description: "🧸 Bai (put - 摆)", snippet: "bai ${1:rax} hai ${2:5}" },
        { name: "ling", standard: "sub", description: "🧸 Ling (take - 拿)", snippet: "ling ${1:rax} ${2:10}" },
        { name: "ga", standard: "add", description: "🧸 Ga (add - 加)", snippet: "ga ${1:rax} tung ${2:3}" },
        { name: "tai", standard: "print", description: "🧸 Tai (show - 睇)", snippet: "tai ${1:rax}" },
        { name: "hui", standard: "jmp", description: "🧸 Hui (go - 去)", snippet: "hui ${1:place}" }
    ],
    // --- ARABIC DIALECTS ---
    // EGYPTIAN ARABIC (Masri)
    "ar_eg": [
        { name: "hot", standard: "mov", description: "🧸 Hot (put - حط)", snippet: "hot ${1:rax} ${2:5}" },
        { name: "sheel", standard: "sub", description: "🧸 Sheel (remove - شيل)", snippet: "sheel ${1:rax} min ${2:10}" },
        { name: "z زود", standard: "add", description: "🧸 Zawwed (increase - زود)", snippet: "zawwed ${1:rax} ${2:3}" },
        { name: "warri", standard: "print", description: "🧸 Warri (show - وري)", snippet: "warri ${1:rax}" },
        { name: "roh", standard: "jmp", description: "🧸 Roh (go - روح)", snippet: "roh ${1:place}" }
    ],
    // --- PORTUGUESE DIALECTS ---
    // BRAZILIAN (PT-BR - Informal)
    "pt_br": [
        { name: "bota", standard: "mov", description: "🧸 Bota (mov)", snippet: "bota ${1:rax} ${2:5}" },
        { name: "tira", standard: "sub", description: "🧸 Tira (sub)", snippet: "tira ${1:rax} de ${2:10}" },
        { name: "junta", standard: "add", description: "🧸 Junta (add)", snippet: "junta ${1:rax} com ${2:3}" },
        { name: "mostra", standard: "print", description: "🧸 Mostra aí (print)", snippet: "mostra ${1:rax}" },
        { name: "vai", standard: "jmp", description: "🧸 Vai pular (jmp)", snippet: "vai ${1:lugar}" }
    ],
    // --- GERMAN DIALECTS ---
    // SWISS GERMAN (Schwiizerdütsch)
    "de_sw": [
        { name: "tue", standard: "mov", description: "🧸 Tue (mov)", snippet: "tue ${1:rax} ${2:5}" },
        { name: "nimm", standard: "sub", description: "🧸 Nimm (sub)", snippet: "nimm ${1:rax} vo ${2:10}" },
        { name: "zelle", standard: "add", description: "🧸 Zelle (add)", snippet: "zelle ${1:rax} mit ${2:3}" },
        { name: "zeig", standard: "print", description: "🧸 Zeig (print)", snippet: "zeig ${1:rax}" },
        { name: "gang", standard: "jmp", description: "🧸 Gang (jmp)", snippet: "gang ${1:ort}" }
    ],
    // AUSTRIAN (Österreichisch)
    "de_at": [
        { name: "gib", standard: "mov", description: "🧸 Gib (mov)", snippet: "gib ${1:rax} ${2:5}" },
        { name: "nimm", standard: "sub", description: "🧸 Nimm (sub)", snippet: "nimm ${1:rax} weg ${2:10}" },
        { name: "dazua", standard: "add", description: "🧸 Tua dazua (add)", snippet: "dazua ${1:rax} ${2:3}" },
        { name: "schau", standard: "print", description: "🧸 Schau (print)", snippet: "schau ${1:rax}" },
        { name: "hupf", standard: "jmp", description: "🧸 Hupf (jmp)", snippet: "hupf ${1:ort}" }
    ],
    // --- ITALIAN DIALECTS ---
    // SICILIAN (Siciliano)
    "it_sic": [
        { name: "metti", standard: "mov", description: "🧸 Metti (mov)", snippet: "metti ${1:rax} ${2:5}" },
        { name: "leva", standard: "sub", description: "🧸 Leva (sub)", snippet: "leva ${1:rax} ${2:10}" },
        { name: "junci", standard: "add", description: "🧸 Junci (add)", snippet: "junci ${1:rax} ${2:3}" },
        { name: "talìa", standard: "print", description: "🧸 Talìa (look/print)", snippet: "talìa ${1:rax}" },
        { name: "va", standard: "jmp", description: "🧸 Va (jmp)", snippet: "va ${1:postu}" }
    ],
    // ROMAN (Romanesco)
    "it_rom": [
        { name: "schiaffa", standard: "mov", description: "🧸 Schiaffa (mov)", snippet: "schiaffa ${1:rax} ${2:5}" },
        { name: "leva", standard: "sub", description: "🧸 Leva (sub)", snippet: "leva ${1:rax} da ${2:10}" },
        { name: "più", standard: "add", description: "🧸 Famo più (add)", snippet: "più ${1:rax} co ${2:3}" },
        { name: "guarda", standard: "print", description: "🧸 Guarda'npo (print)", snippet: "guarda ${1:rax}" },
        { name: "nnamo", standard: "jmp", description: "🧸 Nnamo (jmp)", snippet: "nnamo ${1:do}" }
    ],
    // --- DUTCH DIALECTS ---
    // FLEMISH (Vlaams)
    "nl_be": [
        { name: "steek", standard: "mov", description: "🧸 Steek (mov)", snippet: "steek ${1:rax} in ${2:5}" },
        { name: "pak", standard: "sub", description: "🧸 Pak (sub)", snippet: "pak ${1:rax} van ${2:10}" },
        { name: "doe_erbij", standard: "add", description: "🧸 Doe erbij (add)", snippet: "doe_erbij ${1:rax} ${2:3}" },
        { name: "toog", standard: "print", description: "🧸 Toog (show/print)", snippet: "toog ${1:rax}" },
        { name: "ga", standard: "jmp", description: "🧸 Ga naar (jmp)", snippet: "ga ${1:plek}" }
    ],
    // --- POLISH DIALECTS ---
    // SILESIAN (Ślōnskŏ)
    "pl_sil": [
        { name: "wciep", standard: "mov", description: "🧸 Wciep (throw in/mov)", snippet: "wciep ${1:rax} ${2:5}" },
        { name: "wez", standard: "sub", description: "🧸 Weź (take/sub)", snippet: "wez ${1:rax} ${2:10}" },
        { name: "dodaj", standard: "add", description: "🧸 Dodaj (add)", snippet: "dodaj ${1:rax} ${2:3}" },
        { name: "pokoz", standard: "print", description: "🧸 Pokŏż (show/print)", snippet: "pokoz ${1:rax}" },
        { name: "idź", standard: "jmp", description: "🧸 Idź (go/jmp)", snippet: "idź ${1:plac}" }
    ],
    // --- ENGLISH MORE ---
    // SCOTS
    "en_scots": [
        { name: "pit", standard: "mov", description: "🧸 Pit (put/mov)", snippet: "pit ${1:rax} ${2:5}" },
        { name: "tak", standard: "sub", description: "🧸 Tak (take/sub)", snippet: "tak ${1:rax} frae ${2:10}" },
        { name: "add", standard: "add", description: "🧸 Add (add)", snippet: "add ${1:rax} an ${2:3}" },
        { name: "keek", standard: "print", description: "🧸 Keek (look/print)", snippet: "keek ${1:rax}" },
        { name: "gang", standard: "jmp", description: "🧸 Gang (go/jmp)", snippet: "gang ${1:place}" }
    ],
    // IRISH (Hiberno-English slang)
    "en_ie": [
        { name: "bung", standard: "mov", description: "🧸 Bung (put/mov)", snippet: "bung ${1:rax} ${2:5}" },
        { name: "take", standard: "sub", description: "🧸 Take (sub)", snippet: "take ${1:rax} off ${2:10}" },
        { name: "add", standard: "add", description: "🧸 Add (add)", snippet: "add ${1:rax} and ${2:3}" },
        { name: "look", standard: "print", description: "🧸 Have a look (print)", snippet: "look ${1:rax}" },
        { name: "feck_off", standard: "jmp", description: "🧸 Feck off to (jmp)", snippet: "feck_off ${1:place}" }
    ],
    // --- ADDITIONAL GLOBAL LANGUAGES ---
    // GREEK (EL)
    "el": [
        { name: "bale", standard: "mov", description: "🧸 Bale (put - Βάλε)", snippet: "bale ${1:rax} ${2:5}" },
        { name: "bgale", standard: "sub", description: "🧸 Bgale (remove - Βγάλε)", snippet: "bgale ${1:rax} ${2:10}" },
        { name: "prosthese", standard: "add", description: "🧸 Prosthese (add - Πρόσθεσε)", snippet: "prosthese ${1:rax} ${2:3}" },
        { name: "diekse", standard: "print", description: "🧸 Diekse (show - Δείξε)", snippet: "diekse ${1:rax}" },
        { name: "pigen", standard: "jmp", description: "🧸 Pigen (go - Πήγαινε)", snippet: "pigen ${1:place}" }
    ],
    // HEBREW (HE)
    "he": [
        { name: "sim", standard: "mov", description: "🧸 Sim (put - שים)", snippet: "sim ${1:rax} ${2:5}" },
        { name: "kakh", standard: "sub", description: "🧸 Kakh (take - קח)", snippet: "kakh ${1:rax} ${2:10}" },
        { name: "hosef", standard: "add", description: "🧸 Hosef (add - הוסף)", snippet: "hosef ${1:rax} ${2:3}" },
        { name: "hare", standard: "print", description: "🧸 Hare (show - הראה)", snippet: "hare ${1:rax}" },
        { name: "lekh", standard: "jmp", description: "🧸 Lekh (go - לך)", snippet: "lekh ${1:place}" }
    ],
    // THAI (TH)
    "th": [
        { name: "sai", standard: "mov", description: "🧸 Sai (put - ใส่)", snippet: "sai ${1:rax} ${2:5}" },
        { name: "ao_ok", standard: "sub", description: "🧸 Ao ok (take out - เอาออก)", snippet: "ao_ok ${1:rax} ${2:10}" },
        { name: "buak", standard: "add", description: "🧸 Buak (add - บวก)", snippet: "buak ${1:rax} ${2:3}" },
        { name: "sadang", standard: "print", description: "🧸 Sadang (show - แสดง)", snippet: "sadang ${1:rax}" },
        { name: "pai", standard: "jmp", description: "🧸 Pai (go - ไป)", snippet: "pai ${1:place}" }
    ],
    // VIETNAMESE (VI)
    "vi": [
        { name: "dat", standard: "mov", description: "🧸 Dat (put - Đặt)", snippet: "dat ${1:rax} ${2:5}" },
        { name: "lay", standard: "sub", description: "🧸 Lay (take - Lấy)", snippet: "lay ${1:rax} ${2:10}" },
        { name: "them", standard: "add", description: "🧸 Them (add - Thêm)", snippet: "them ${1:rax} ${2:3}" },
        { name: "hien", standard: "print", description: "🧸 Hien (show - Hiện)", snippet: "hien ${1:rax}" },
        { name: "di", standard: "jmp", description: "🧸 Di (go - Đi)", snippet: "di ${1:place}" }
    ],
    // SWAHILI (SW)
    "sw": [
        { name: "weka", standard: "mov", description: "🧸 Weka (put)", snippet: "weka ${1:rax} ${2:5}" },
        { name: "toa", standard: "sub", description: "🧸 Toa (remove)", snippet: "toa ${1:rax} ${2:10}" },
        { name: "ongeza", standard: "add", description: "🧸 Ongeza (add)", snippet: "ongeza ${1:rax} ${2:3}" },
        { name: "onyesha", standard: "print", description: "🧸 Onyesha (show)", snippet: "onyesha ${1:rax}" },
        { name: "nenda", standard: "jmp", description: "🧸 Nenda (go)", snippet: "nenda ${1:place}" }
    ],
    // TAGALOG (TL)
    "tl": [
        { name: "lagay", standard: "mov", description: "🧸 Lagay (put)", snippet: "lagay ${1:rax} ${2:5}" },
        { name: "kuna", standard: "sub", description: "🧸 Kuna (take)", snippet: "kuna ${1:rax} ${2:10}" },
        { name: "dagdag", standard: "add", description: "🧸 Dagdag (add)", snippet: "dagdag ${1:rax} ${2:3}" },
        { name: "pakita", standard: "print", description: "🧸 Pakita (show)", snippet: "pakita ${1:rax}" },
        { name: "unta", standard: "jmp", description: "🧸 Unta (go)", snippet: "unta ${1:place}" }
    ],
    // MALAY (MS)
    "ms": [
        { name: "letak", standard: "mov", description: "🧸 Letak (put)", snippet: "letak ${1:rax} ${2:5}" },
        { name: "ambil", standard: "sub", description: "🧸 Ambil (take)", snippet: "ambil ${1:rax} ${2:10}" },
        { name: "tambah", standard: "add", description: "🧸 Tambah (add)", snippet: "tambah ${1:rax} ${2:3}" },
        { name: "tunjuk", standard: "print", description: "🧸 Tunjuk (show)", snippet: "tunjuk ${1:rax}" },
        { name: "pergi", standard: "jmp", description: "🧸 Pergi (go)", snippet: "pergi ${1:place}" }
    ],
    // PERSIAN (FA)
    "fa": [
        { name: "bezor", standard: "mov", description: "🧸 Bezor (put - بگذار)", snippet: "bezor ${1:rax} ${2:5}" },
        { name: "bardar", standard: "sub", description: "🧸 Bardar (take - بردار)", snippet: "bardar ${1:rax} ${2:10}" },
        { name: "jam", standard: "add", description: "🧸 Jam (add - جمع)", snippet: "jam ${1:rax} ${2:3}" },
        { name: "neshon", standard: "print", description: "🧸 Neshon (show - نشان)", snippet: "neshon ${1:rax}" },
        { name: "boro", standard: "jmp", description: "🧸 Boro (go - برو)", snippet: "boro ${1:place}" }
    ],
    // UKRAINIAN (UK)
    "uk": [
        { name: "polozhy", standard: "mov", description: "🧸 Polozhy (put - Поклади)", snippet: "polozhy ${1:rax} ${2:5}" },
        { name: "vizmy", standard: "sub", description: "🧸 Vizmy (take - Візьми)", snippet: "vizmy ${1:rax} ${2:10}" },
        { name: "dodaty", standard: "add", description: "🧸 Dodaty (add - Додати)", snippet: "dodaty ${1:rax} ${2:3}" },
        { name: "pokazhy", standard: "print", description: "🧸 Pokazhy (show - Покажи)", snippet: "pokazhy ${1:rax}" },
        { name: "ydy", standard: "jmp", description: "🧸 Ydy (go - Йди)", snippet: "ydy ${1:place}" }
    ],
    // ROMANIAN (RO)
    "ro": [
        { name: "pune", standard: "mov", description: "🧸 Pune (put)", snippet: "pune ${1:rax} ${2:5}" },
        { name: "ia", standard: "sub", description: "🧸 Ia (take)", snippet: "ia ${1:rax} ${2:10}" },
        { name: "adauga", standard: "add", description: "🧸 Adaugă (add)", snippet: "adauga ${1:rax} ${2:3}" },
        { name: "arata", standard: "print", description: "🧸 Arată (show)", snippet: "arata ${1:rax}" },
        { name: "du-te", standard: "jmp", description: "🧸 Du-te (go)", snippet: "du-te ${1:place}" }
    ]
};
