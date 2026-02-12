# MultiLang-ASM: Yönergeler (Türkçe - tr)

MultiLang-ASM Türkçe desteğine hoş geldiniz.

## 🛠 Temel Komutlar

| MultiLang-ASM | NASM (x86_64) | Açıklama |
| :--- | :--- | :--- |
| `tasi` | `mov` | Veriyi taşı |
| `topla` | `add` | Topla |
| `cikar` | `sub` | Çıkar |
| `karsilastir` | `cmp` | Değerleri karşılaştır |
| `atla` | `jmp` | Adrese atla |
| `cagir` | `call` | Fonksiyonu çağır |
| `don` | `ret` | Fonksiyondan dön |
| `kesme` | `int` | Yazılım kesmesi |
| `sistem_cagrisi`| `syscall` | Çekirdek çağrısı |

## 📝 Kod Örneği

```asm
; Türkçe Hello World
bolum .veri
    mesaj: db "Merhaba Dunya!", 10

bolum .metin
    evrensel _basla

_basla:
    tasi rax, 1          ; syscall: write
    tasi rdi, 1          ; fd: stdout
    tasi rsi, mesaj      ; buffer
    tasi rdx, 15         ; length
    sistem_cagrisi

    tasi rax, 60         ; syscall: exit
    tasi rdi, 0          ; error code
    sistem_cagrisi
```

## 🚀 Kullanım

```bash
python mlasm.py tr program.masm
```
