# VVNK - QU4N.TH3.D3V

Discord Self-Bot cho personal use.

---

## Cài đặt

### 1. Tải source code
- Vào https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V
- Nhấn nút **Code** -> **Download ZIP**
- Giải nén vào thư mục bất kỳ

### 2. Cài Python
Tải Python tại https://python.org (chọn bản 3.9+)
- **Windows**: Chọn "Add Python to PATH" khi cài
- **Mac/Linux**: Terminal chạy `python3 --version` để kiểm tra

### 3. Chạy bot

**Windows:**
- double-click `Run.bat`
- Hoặc mở terminal: `python index.py`

**Mac/Linux:**
```bash
python3 index.py
```

### 4. Nhập Token
- Lần đầu chạy, bot sẽ mở file `config\config.json`
- Nhập token Discord vào `"token": "DAN_TOKEN_VAO_DAY"`
- Lưu file -> chạy lại bot

---

## Cấu trúc thư mục

```
VVNK/
├── bot.py           ← File chính
├── index.py         ← Cài đặt + chạy
├── Run.bat          ← Chạy nhanh (Windows)
├── config/
│   └── config.json  ← Token + prefix
├── cogs/
│   ├── cycstatus.txt  ← Status tự động chuyển
│   └── nhay.txt       ← Nội dung lệnh .nhay
├── music/           ← File nhạc (.mp3, .wav, .ogg)
├── ffmpeg/          ← Đặt ffmpeg.exe vào đây (Windows)
├── ngon.txt         ← Nội dung lệnh .thuong
├── datoken.txt      ← Token phụ (cho lệnh tokenspam)
└── requirements.txt
```

---

## Danh sách lệnh

### Lệnh chính
| Lệnh | Mô tả |
|------|-------|
| `.menu` | Mở bảng điều khiển |
| `.botinfo` | Thông tin bot |
| `.restart` | Khởi động lại bot |
| `.shutdown` | Tắt bot |

### Quản lý server
| Lệnh | Mô tả |
|------|-------|
| `.kick @user` | Kick thành viên |
| `.ban @user` | Ban thành viên |
| `.unban ID` | Unban |

### Spam / Raid
| Lệnh | Mô tả |
|------|-------|
| `.spam [delay] [nội dung]` | Spam tin nhắn |
| `.nhay [delay]` | Spam từ nhay.txt |
| `.webhook [url] [nội dung]` | Spam qua webhook |
| `.nuke [tên] [nội dung]` | Phá server |
| `.bomb` | Xóa toàn bộ kênh |
| `.massreact [số] [emoji]` | Thêm reaction hàng loạt |
| `.tokenspam [delay] [nội dung]` | Spam đa token |
| `.tokenvc [ID voice]` | Treo voice đa token |
| `.vcspam [ID voice]` | Spam join/leave voice |
| `.stop` / `.stopspam` / `.stopnhay` / `.stopwebhook` / `.stopvcspam` / `.stoptokenspam` | Dừng các lệnh đang chạy |

### Tiện ích
| Lệnh | Mô tả |
|------|-------|
| `.tienich` | Danh sách tiện ích |
| `.clear [số]` | Xóa tin nhắn |
| `.hackclear` | Xóa chat bằng tin nhắn trống |
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |
| `.serverinfo` | Thông tin server |
| `.iplookup [IP]` | Tra cứu IP |
| `.insta [tên]` | Xem Instagram |
| `.math [phep tính]` | Máy tính |
| `.cloneemoji [emoji]` | Sao chép emoji |
| `.clone_channels [ID cũ] [ID mới]` | Sao chép kênh |
| `.clone_roles [ID cũ] [ID mới]` | Sao chép role |
| `.deleteallroles` | Xóa tất cả role |
| `.closealldms` | Đóng tất cả DM |
| `.delfriends` | Xóa tất cả bạn bè |
| `.tokencheck [token]` | Kiểm tra token |
| `.checkpromo [link]` | Kiểm tra Nitro promo |
| `.cyclestatus` | Tự động chuyển status |
| `.addstatus [text]` | Thêm status |
| `.clearstatus` | Xóa tất cả status |
| `.setstatus [text]` | Đặt status |

### Voice
| Lệnh | Mô tả |
|------|-------|
| `.vcjoin [ID] [Y/N] [Y/N] [Y/N]` | Join voice (mute/deafen/camera) |
| `.vcleave` | Rời voice |
| `.xanhac [ID] [tên file]` | Phát nhạc trong voice |
| `.forcedisconnect [@user]` | Ngắt người dùng khỏi voice |
| `.stopforcedisconnect` | Dừng forcedisconnect |

### Troll / Giải trí
| Lệnh | Mô tả |
|------|-------|
| `.troll` | Danh sách lệnh troll |
| `.nsfw [loại]` | NSFW (anal/hanal/4k/gif/pussy/boobs/ass/hboobs/thighs) |
| `.succac` | Hiệu ứng |
| `.rainbowrole [@role]` | Role 7 màu |
| `.rizz [@user]` | Random câu tán tỉnh |
| `.roast [@user] | Random câu roast |
| `.cat` | Ảnh mèo ngẫu nhiên |
| `.phc [@user] [nội dung]` | PornHub comment |
| `.rpc playing [tên]` | Đang chơi game |
| `.rpc streaming [tên]` | Đang stream |
| `.rpc listening [tên]` | Đang nghe |
| `.rpc watching [tên]` | Đang xem |
| `.stoprpc` | Dừng RPC |
| `.autoreact on/off` | Bật/tắt tự reaction |
| `.afk [lý do]` | AFK |
| `.unafk` | Bỏ AFK |

---

## Miễn trừ trách nhiệm

- Bot này là **self-bot** (chạy trên tài khoản người dùng), vi phạm Discord Terms of Service
- Sử dụng trên **tài khoản phụ (alt)** để tránh bị ban
- Tác giả không chịu trách nhiệm về任何hậu quả khi sử dụng
- Chỉ dùng cho mục đích học tập, thử nghiệm

---

## Hỗ trợ

- **Windows** ✅
- **Mac** ✅ (dùng `python3` thay `python`)
- **Linux** ✅ (dùng `python3` thay `python`)

---

**Author: QU4N.TH3.D3V**
