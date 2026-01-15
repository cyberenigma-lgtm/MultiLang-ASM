# 🧸 Kids Mode (Modo Niños)

**Kids Mode** is a revolutionary feature in MultiLang-ASM v0.5 designed to teach low-level logic to children (ages 7-12) without the complexity of cryptic mnemonics.

It uses simplified, natural language verbs (like "put", "give", "show") instead of technical opcodes (`mov`, `add`, `syscall`).

---

## 🚀 How it Works

In **Kids Mode**:
1.  **Direct Commands:** Use `put` instead of `mov`.
2.  **Simple Math:** Use `add` instead of `add`.
3.  **Visual Output:** Use `show` (aliased to specific system calls) to see results.

### Example (English):
```masm
put rax 5       ; Set box 'rax' to 5
put rbx 3       ; Set box 'rbx' to 3
add rax rbx     ; Add 3 to 5
look rax        ; Show result!
```

---

## 🌍 The Universal Kids Dictionary

Here is the complete reference for **Kids Mode** in all 27 supported languages.

| Language | 📦 PUT (mov) | ➕ ADD (add) | ➖ SUB (sub) | 👀 SHOW (syscall) |
| :--- | :--- | :--- | :--- | :--- |
| **🇺🇸 English** | `put` | `add` | `take` | `look` |
| **🇪🇸 Español** | `pon` | `suma` | `resta` | `enseña` |
| **🇫🇷 Français** | `mets` | `ajoute` | `enleve` | `montre` |
| **🇩🇪 Deutsch** | `setze` | `addiere` | `ziehe_ab` | `zeige` |
| **🇮🇹 Italiano** | `metti` | `aggiungi` | `togli` | `mostra` |
| **🇵🇹 Português** | `coloca` | `soma` | `tira` | `mostra` |
| **🇷🇺 Русский** | `положи` | `добавь` | `отними` | `покажи` |
| **🇯🇵 Japanese** | `irete` | `tashite` | `hiite` | `misete` |
| **🇨🇳 Chinese** | `fang` | `jia` | `jian` | `kan` |
| **🇰🇷 Korean** | `neoh` | `deohae` | `ppaera` | `boyeo` |
| **🇸🇦 Arabic** | `da` | `ijma` | `itrah` | `anzur` |
| **🇮🇳 Hindi** | `rakho` | `jodo` | `ghatao` | `dikhao` |
| **🇹🇷 Turkish** | `koy` | `ekle` | `cikar` | `goster` |
| **🇵🇱 Polish** | `wsadz` | `dodaj` | `odejmij` | `pokaz` |
| **🇸🇪 Swedish** | `stall` | `addera` | `dra_av` | `visa` |
| **🇳🇱 Dutch** | `zet` | `tel_op` | `trek_af` | `toon` |
| **🇬🇷 Greek** | `bale` | `prosthese` | `afairese` | `diekse` |
| **🇮🇱 Hebrew** | `sim` | `hosef` | `haser` | `hare` |
| **🇹🇭 Thai** | `sai` | `buak` | `lop` | `sadang` |
| **🇻🇳 Vietnamese** | `dat` | `them` | `tru` | `hien` |
| **🇰🇪 Swahili** | `weka` | `ongeza` | `toa` | `onyesha` |
| **🇵🇭 Tagalog** | `lagay` | `dagdag` | `bawas` | `pakita` |
| **🇲🇾 Malay** | `letak` | `tambah` | `tolak` | `tunjuk` |
| **🇮🇷 Persian** | `bezor` | `jam` | `kam` | `neshon` |
| **🇺🇦 Ukrainian** | `polozhy` | `dodaty` | `vidnyaty` | `pokazhy` |
| **🇷🇴 Romanian** | `pune` | `adauga` | `scade` | `arata` |
| **🇮🇩 Indonesian** | `taruh` | `tambah` | `kurang` | `tampil` |

---

## 🎭 Regional Dialects (Fun Mode)

MultiLang-ASM also supports regional flavors for kids to learn with their local slang!

### 🇬🇧 English Dialects
*   **Cockney:** `stash` (mov), `lob` (add), `nick` (sub), `gawk` (show)
*   **Aussie:** `chuck` (mov), `reckon` (add), `nix` (sub), `squiz` (show)
*   **Texan:** `hitch` (mov), `roundup` (add), `cut` (sub), `spy` (show)

### 🇪🇸 Spanish Dialects
*   **Andalusian:** `pon` (mov), `suma` (add), `resta` (sub), `mira` (show) *(Standardized)*
*   **Madrileño:** `apanca` (mov), `suma` (add), `pilla` (sub), `lipa` (show)

---

## 👩‍🏫 For Teachers

Kids Mode is designed to be:
*   **Forgiving:** Auto-correction of common typos.
*   **Visual:** Focus on seeing values change in registers.
*   **Safe:** Restricted set of instructions to prevent crashes.

[Return to Home](Home)
