# 📚 Référence Complète des Instructions — Français (MultiLang-ASM)

Ce guide regroupe toutes les instructions supportées en Français pour l'assembleur multilingue **MultiLang-ASM**, partie de l'écosystème **Neuro-OS.es**.

> MultiLang-ASM permet d'écrire du code assembleur dans votre langue maternelle et de générer du code ASM standard compatible avec NASM/FASM/GAS.

---

## 📦 Mouvement de Données

| Français | ASM | Description |
|---------|-----|-------------|
| `deplacer`, `depl` | `mov` | Déplacer des données entre registres/mémoire |
| `echanger` | `xchg` | Échanger les valeurs entre opérandes |
| `charger_effectif` | `lea` | Charger l'adresse effective |
| `etendre_zero` | `movzx` | Déplacer avec extension de zéros |
| `etendre_signe` | `movsx` | Déplacer avec extension de signe |

---

## ➕ Arithmétique

| Français | ASM | Description |
|---------|-----|-------------|
| `ajouter`, `additionner` | `add` | Additionner deux opérandes |
| `soustraire` | `sub` | Soustraire deux opérandes |
| `multiplier` | `mul` | Multiplication non signée |
| `multiplier_signe` | `imul` | Multiplication signée |
| `diviser` | `div` | Division non signée |
| `diviser_signe` | `idiv` | Division signée |
| `incrementer` | `inc` | Incrémenter de 1 |
| `decrementer` | `dec` | Décrémenter de 1 |
| `negation` | `neg` | Négation (complément à 2) |

---

## 🔢 Opérations Logiques

| Français | ASM | Description |
|---------|-----|-------------|
| `et` | `and` | ET logique bit à bit |
| `ou` | `or` | OU logique bit à bit |
| `non` | `not` | NON logique (complément à 1) |
| `ou_exclusif` | `xor` | OU exclusif bit à bit |
| `decaler_gauche` | `shl`, `sal` | Décalage logique/arithmétique gauche |
| `decaler_droite` | `shr`, `sar` | Décalage logique/arithmétique droite |
| `rotation_gauche` | `rol` | Rotation à gauche |
| `rotation_droite` | `ror` | Rotation à droite |

---

## 🔍 Comparaison et Test

| Français | ASM | Description |
|---------|-----|-------------|
| `comparer` | `cmp` | Comparer deux opérandes |
| `tester` | `test` | ET logique sans sauvegarder le résultat |

---

## 🎯 Contrôle de Flux

### Sauts Inconditionnels

| Français | ASM | Description |
|---------|-----|-------------|
| `sauter`, `saut` | `jmp` | Saut inconditionnel |
| `appeler`, `appel` | `call` | Appeler une sous-routine |
| `retourner`, `retour` | `ret` | Retourner de la sous-routine |

### Sauts Conditionnels

| Français | ASM | Description |
|---------|-----|-------------|
| `si_egal` | `je`, `jz` | Sauter si égal / si zéro |
| `si_different` | `jne`, `jnz` | Sauter si différent / si non zéro |
| `si_superieur` | `jg` | Sauter si supérieur (signé) |
| `si_superieur_egal` | `jge` | Sauter si supérieur ou égal (signé) |
| `si_inferieur` | `jl` | Sauter si inférieur (signé) |
| `si_inferieur_egal` | `jle` | Sauter si inférieur ou égal (signé) |
| `si_au_dessus` | `ja` | Sauter si au-dessus (non signé) |
| `si_en_dessous` | `jb` | Sauter si en-dessous (non signé) |

---

## 📚 Pile (Stack)

| Français | ASM | Description |
|---------|-----|-------------|
| `pousser`, `pousse` | `push` | Insérer une valeur dans la pile |
| `tirer`, `tire` | `pop` | Extraire une valeur de la pile |
| `pousser_drapeaux` | `pushf` | Insérer le registre de drapeaux |
| `tirer_drapeaux` | `popf` | Extraire le registre de drapeaux |

---

## 📝 Exemple d'Utilisation

```asm
; Fonction qui additionne deux nombres
fonction_somme:
    pousser rbp             ; push rbp
    deplacer rbp, rsp       ; mov rbp, rsp
    
    ajouter rdi, rsi        ; add rdi, rsi
    deplacer rax, rdi       ; mov rax, rdi
    
    tirer rbp               ; pop rbp
    retourner               ; ret
```

> [!TIP]
> Toutes les instructions standard en anglais (mov, add, jmp, etc.) fonctionnent également directement sans traduction.

---

**Total:** 80+ instructions x86_64 supportées en Français.  
**MultiLang-ASM** — Partie de l'écosystème **Neuro-OS.es**.
