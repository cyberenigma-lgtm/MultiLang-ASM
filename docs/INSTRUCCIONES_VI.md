# MultiLang-ASM: Hướng dẫn (Tiếng Việt - vi)

Chào mừng bạn đến với hỗ trợ Tiếng Việt cho MultiLang-ASM.

## 🛠 Các lệnh cơ bản

| MultiLang-ASM | NASM (x86_64) | Mô tả |
| :--- | :--- | :--- |
| `chuyen` | `mov` | Di chuyển dữ liệu |
| `cong` | `add` | Cộng |
| `tru` | `sub` | Trừ |
| `so_sanh` | `cmp` | So sánh giá trị |
| `nhay` | `jmp` | Nhảy đến địa chỉ |
| `goi` | `call` | Gọi hàm |
| `tra_ve` | `ret` | Trở về từ hàm |
| `ngat` | `int` | Ngắt phần mềm |
| `goi_he_thong` | `syscall` | Gọi hệ thống |

## 📝 Ví dụ mã nguồn

```asm
; Hello World bằng Tiếng Việt
phan .du_lieu
    thong_bao: db "Xin chào thế giới!", 10

phan .van_ban
    toan_cuc _bat_dau

_bat_dau:
    chuyen rax, 1          ; syscall: write
    chuyen rdi, 1          ; fd: stdout
    chuyen rsi, thong_bao  ; buffer
    chuyen rdx, 19         ; length
    goi_he_thong

    chuyen rax, 60         ; syscall: exit
    chuyen rdi, 0          ; mã lỗi
    goi_he_thong
```

## 🚀 Sử dụng

```bash
python mlasm.py vi program.masm
```
