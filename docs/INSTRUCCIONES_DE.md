# 📚 Vollständige Anweisungsreferenz — Deutsch (MultiLang-ASM)

Dieser Leitfaden enthält alle unterstützten Anweisungen auf Deutsch für den mehrsprachigen Assembler **MultiLang-ASM**, Teil des **Neuro-OS.es**-Ökosystems.

> MultiLang-ASM ermöglicht es, Assembler-Code in Ihrer Muttersprache zu schreiben und Standard-ASM-Code zu generieren, der mit NASM/FASM/GAS kompatibel ist.

---

## 📦 Datenbewegung

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `bewegen` | `mov` | Daten zwischen Registern/Speicher verschieben |
| `tauschen` | `xchg` | Werte zwischen Operanden austauschen |
| `effektiv_laden` | `lea` | Effektive Adresse laden |
| `null_erweitern` | `movzx` | Verschieben mit Nullerweiterung |
| `vorzeichen_erweitern` | `movsx` | Verschieben mit Vorzeichenerweiterung |

---

## ➕ Arithmetik

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `addieren`, `hinzufugen` | `add` | Zwei Operanden addieren |
| `subtrahieren` | `sub` | Zwei Operanden subtrahieren |
| `multiplizieren` | `mul` | Vorzeichenlose Multiplikation |
| `multiplizieren_vorzeichen` | `imul` | Vorzeichenbehaftete Multiplikation |
| `dividieren` | `div` | Vorzeichenlose Division |
| `dividieren_vorzeichen` | `idiv` | Vorzeichenbehaftete Division |
| `inkrementieren` | `inc` | Um 1 erhöhen |
| `dekrementieren` | `dec` | Um 1 verringern |
| `negieren` | `neg` | Negieren (Zweierkomplement) |

---

## 🔢 Logische Operationen

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `und` | `and` | Logisches UND bitweise |
| `oder` | `or` | Logisches ODER bitweise |
| `nicht` | `not` | Logisches NICHT (Einerkomplement) |
| `exklusiv_oder` | `xor` | Exklusives ODER bitweise |
| `verschieben_links` | `shl`, `sal` | Logische/arithmetische Verschiebung links |
| `verschieben_rechts` | `shr`, `sar` | Logische/arithmetische Verschiebung rechts |
| `rotieren_links` | `rol` | Rotation nach links |
| `rotieren_rechts` | `ror` | Rotation nach rechts |

---

## 🔍 Vergleich und Test

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `vergleichen` | `cmp` | Zwei Operanden vergleichen |
| `testen` | `test` | Logisches UND ohne Ergebnis speichern |

---

## 🎯 Ablaufsteuerung

### Unbedingte Sprünge

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `springen` | `jmp` | Unbedingter Sprung |
| `rufen` | `call` | Unterprogramm aufrufen |
| `zurueckkehren` | `ret` | Vom Unterprogramm zurückkehren |

### Bedingte Sprünge

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `wenn_gleich` | `je`, `jz` | Springen wenn gleich / wenn Null |
| `wenn_ungleich` | `jne`, `jnz` | Springen wenn ungleich / wenn nicht Null |
| `wenn_groesser` | `jg` | Springen wenn größer (vorzeichenbehaftet) |
| `wenn_groesser_gleich` | `jge` | Springen wenn größer oder gleich |
| `wenn_kleiner` | `jl` | Springen wenn kleiner (vorzeichenbehaftet) |
| `wenn_kleiner_gleich` | `jle` | Springen wenn kleiner oder gleich |

---

## 📚 Stack (Stapel)

| Deutsch | ASM | Beschreibung |
|---------|-----|-------------|
| `schieben` | `push` | Wert auf den Stack legen |
| `ziehen` | `pop` | Wert vom Stack nehmen |
| `schieben_flags` | `pushf` | Flags-Register auf Stack legen |
| `ziehen_flags` | `popf` | Flags-Register vom Stack nehmen |

---

## 📝 Verwendungsbeispiel

```asm
; Funktion, die zwei Zahlen addiert
funktion_summe:
    schieben rbp            ; push rbp
    bewegen rbp, rsp        ; mov rbp, rsp
    
    addieren rdi, rsi       ; add rdi, rsi
    bewegen rax, rdi        ; mov rax, rdi
    
    ziehen rbp              ; pop rbp
    zurueckkehren           ; ret
```

> [!TIP]
> Alle Standard-Anweisungen auf Englisch (mov, add, jmp, etc.) funktionieren ebenfalls direkt ohne Übersetzung.

---

**Gesamt:** 80+ x86_64-Anweisungen auf Deutsch unterstützt.  
**MultiLang-ASM** — Teil des **Neuro-OS.es**-Ökosystems.
