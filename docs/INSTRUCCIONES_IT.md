# 📚 Riferimento Completo delle Istruzioni — Italiano (MultiLang-ASM)

Questa guida raccoglie tutte le istruzioni supportate in Italiano per l'assemblatore multilingue **MultiLang-ASM**, parte dell'ecosistema **Neuro-OS.es**.

> MultiLang-ASM permette di scrivere codice assembly nella propria lingua madre e generare codice ASM standard compatibile con NASM/FASM/GAS.

---

## 📦 Movimento Dati

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `muovere`, `muovi` | `mov` | Spostare dati tra registri/memoria |
| `scambiare` | `xchg` | Scambiare valori tra operandi |
| `caricare_effettivo` | `lea` | Caricare indirizzo effettivo |
| `estendere_zero` | `movzx` | Spostare con estensione di zeri |
| `estendere_segno` | `movsx` | Spostare con estensione del segno |

---

## ➕ Aritmetica

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `sommare`, `aggiungere` | `add` | Sommare due operandi |
| `sottrarre` | `sub` | Sottrarre due operandi |
| `moltiplicare` | `mul` | Moltiplicazione senza segno |
| `moltiplicare_segno` | `imul` | Moltiplicazione con segno |
| `dividere` | `div` | Divisione senza segno |
| `dividere_segno` | `idiv` | Divisione con segno |
| `incrementare` | `inc` | Incrementare di 1 |
| `decrementare` | `dec` | Decrementare di 1 |
| `negare` | `neg` | Negare (complemento a 2) |

---

## 🔢 Operazioni Logiche

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `e` | `and` | AND logico bit a bit |
| `o` | `or` | OR logico bit a bit |
| `non` | `not` | NOT logico (complemento a 1) |
| `esclusivo` | `xor` | XOR logico bit a bit |
| `spostare_sinistra` | `shl`, `sal` | Spostamento logico/aritmetico sinistra |
| `spostare_destra` | `shr`, `sar` | Spostamento logico/aritmetico destra |
| `ruotare_sinistra` | `rol` | Rotazione a sinistra |
| `ruotare_destra` | `ror` | Rotazione a destra |

---

## 🔍 Confronto e Test

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `confrontare` | `cmp` | Confrontare due operandi |
| `testare` | `test` | AND logico senza salvare il risultato |

---

## 🎯 Controllo del Flusso

### Salti Incondizionati

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `saltare`, `salta` | `jmp` | Salto incondizionato |
| `chiamare`, `chiama` | `call` | Chiamare una subroutine |
| `tornare`, `torna` | `ret` | Tornare dalla subroutine |

### Salti Condizionati

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `se_uguale` | `je`, `jz` | Saltare se uguale / se zero |
| `se_diverso` | `jne`, `jnz` | Saltare se diverso / se non zero |
| `se_maggiore` | `jg` | Saltare se maggiore (con segno) |
| `se_maggiore_uguale` | `jge` | Saltare se maggiore o uguale |
| `se_minore` | `jl` | Saltare se minore (con segno) |
| `se_minore_uguale` | `jle` | Saltare se minore o uguale |
| `se_sopra` | `ja` | Saltare se sopra (senza segno) |
| `se_sotto` | `jb` | Saltare se sotto (senza segno) |

---

## 📚 Pila (Stack)

| Italiano | ASM | Descrizione |
|---------|-----|-------------|
| `mettere`, `metti` | `push` | Inserire valore nello stack |
| `togliere`, `togli` | `pop` | Estrarre valore dallo stack |
| `mettere_bandiere` | `pushf` | Inserire registro bandiere |
| `togliere_bandiere` | `popf` | Estrarre registro bandiere |

---

## 📝 Esempio di Utilizzo

```asm
; Funzione che somma due numeri
funzione_somma:
    mettere rbp             ; push rbp
    muovere rbp, rsp        ; mov rbp, rsp
    
    sommare rdi, rsi        ; add rdi, rsi
    muovere rax, rdi        ; mov rax, rdi
    
    togliere rbp            ; pop rbp
    tornare                 ; ret
```

> [!TIP]
> Tutte le istruzioni standard in inglese (mov, add, jmp, ecc.) funzionano anche direttamente senza traduzione.

---

**Totale:** 80+ istruzioni x86_64 supportate in Italiano.  
**MultiLang-ASM** — Parte dell'ecosistema **Neuro-OS.es**.
