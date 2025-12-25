# 📚 Referensi Lengkap Instruksi — Bahasa Indonesia (MultiLang-ASM)

Panduan ini berisi semua instruksi yang didukung dalam Bahasa Indonesia untuk assembler multibahasa **MultiLang-ASM**, bagian dari ekosistem **Neuro-OS.es**.

> MultiLang-ASM memungkinkan Anda menulis kode assembly dalam bahasa ibu Anda dan menghasilkan kode ASM standar yang kompatibel dengan NASM/FASM/GAS.

---

## 📦 Perpindahan Data

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `pindah`, `salin` | `mov` | Memindahkan data antar register/memori |
| `tukar` | `xchg` | Menukar nilai antar operand |
| `muat_efektif` | `lea` | Memuat alamat efektif |
| `perpanjang_nol` | `movzx` | Pindah dengan ekstensi nol |
| `perpanjang_tanda` | `movsx` | Pindah dengan ekstensi tanda |

---

## ➕ Aritmatika

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `tambah`, `jumlah` | `add` | Menambahkan dua operand |
| `kurang` | `sub` | Mengurangkan dua operand |
| `kali` | `mul` | Perkalian tanpa tanda |
| `kali_tanda` | `imul` | Perkalian dengan tanda |
| `bagi` | `div` | Pembagian tanpa tanda |
| `bagi_tanda` | `idiv` | Pembagian dengan tanda |
| `tambah_satu` | `inc` | Menambah 1 |
| `kurang_satu` | `dec` | Mengurangi 1 |
| `negatif` | `neg` | Negasi (komplemen 2) |

---

## 🔢 Operasi Logika

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `dan` | `and` | AND logika bit demi bit |
| `atau` | `or` | OR logika bit demi bit |
| `tidak` | `not` | NOT logika (komplemen 1) |
| `eksklusif` | `xor` | XOR logika bit demi bit |
| `geser_kiri` | `shl`, `sal` | Geser logika/aritmatika kiri |
| `geser_kanan` | `shr`, `sar` | Geser logika/aritmatika kanan |
| `putar_kiri` | `rol` | Rotasi ke kiri |
| `putar_kanan` | `ror` | Rotasi ke kanan |

---

## 🔍 Perbandingan dan Tes

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `bandingkan` | `cmp` | Membandingkan dua operand |
| `uji` | `test` | AND logika tanpa menyimpan hasil |

---

## 🎯 Kontrol Alur

### Lompatan Tanpa Syarat

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `lompat` | `jmp` | Lompatan tanpa syarat |
| `panggil` | `call` | Memanggil subrutin |
| `kembali` | `ret` | Kembali dari subrutin |

### Lompatan Bersyarat

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `jika_sama` | `je`, `jz` | Lompat jika sama / jika nol |
| `jika_beda` | `jne`, `jnz` | Lompat jika beda / jika bukan nol |
| `jika_lebih` | `jg` | Lompat jika lebih besar (bertanda) |
| `jika_lebih_sama` | `jge` | Lompat jika lebih besar atau sama |
| `jika_kurang` | `jl` | Lompat jika lebih kecil (bertanda) |
| `jika_kurang_sama` | `jle` | Lompat jika lebih kecil atau sama |
| `jika_atas` | `ja` | Lompat jika di atas (tanpa tanda) |
| `jika_bawah` | `jb` | Lompat jika di bawah (tanpa tanda) |

---

## 📚 Tumpukan (Stack)

| Bahasa Indonesia | ASM | Deskripsi |
|---------|-----|-----------|
| `masukkan` | `push` | Masukkan nilai ke stack |
| `keluarkan` | `pop` | Keluarkan nilai dari stack |
| `masukkan_bendera` | `pushf` | Masukkan register bendera |
| `keluarkan_bendera` | `popf` | Keluarkan register bendera |

---

## 📝 Contoh Penggunaan

```asm
; Fungsi yang menjumlahkan dua angka
fungsi_jumlah:
    masukkan rbp            ; push rbp
    pindah rbp, rsp         ; mov rbp, rsp
    
    tambah rdi, rsi         ; add rdi, rsi
    pindah rax, rdi         ; mov rax, rdi
    
    keluarkan rbp           ; pop rbp
    kembali                 ; ret
```

> [!TIP]
> Semua instruksi standar dalam bahasa Inggris (mov, add, jmp, dll.) juga berfungsi langsung tanpa terjemahan.

---

**Total:** 80+ instruksi x86_64 didukung dalam Bahasa Indonesia.  
**MultiLang-ASM** — Bagian dari ekosistem **Neuro-OS.es**.
