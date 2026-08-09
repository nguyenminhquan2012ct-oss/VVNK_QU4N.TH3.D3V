# VVNK v1.0

Discord Self-Bot với nhiều tính năng: spam, raid, nhạc, giải trí, quản lý, tiện ích.

> ⚠️ Self-bot vi phạm Discord ToS. Sử dụng tài khoản alt. Chủ nhân chấp nhận mọi rủi ro.

---

## Cách tải

### Cách 1: Tải file ZIP
1. Vào: https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V
2. Nút **Code** (màu xanh) → **Download ZIP**
3. Giải nén thư mục `VVNK-main`

### Cách 2: Clone (cần Git)
```bash
git clone https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V.git
```

---

## Cách chạy

1. Mở thư mục `VVNK`
2. Double-click **`Run.bat`**
3. Lần đầu hỏi **Discord Token** → nhập vào
4. Bot tự động cài thư viện và khởi động
5. Bot tự động restart nếu crash

Hoặc chạy thủ công:
```bash
python -m pip install -r requirements.txt
python bot.py
```

---

## Cấu hình

File `config/config.json` (tự tạo bởi Run.bat):
```json
{
    "token": "DISCORD_TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

---

## Danh sách lệnh

### Menu chính
| Lệnh | Mô tả |
|------|-------|
| `.menu` | Hiển thị menu chính |
| `.botinfo` | Thông tin bot |
| `.restart` | Khởi động lại bot |
| `.shutdown` | Tắt bot |

### War / Spam
| Lệnh | Mô tả |
|------|-------|
| `.spam [delay] [text]` | Spam tin nhắn |
| `.nhay [delay]` | Spam từ nhay.txt |
| `.webhook [url] [text]` | Spam qua Webhook |
| `.nuke [tên] [text]` | Phá server |
| `.bomb` | Xóa toàn bộ kênh |
| `.massreact [số] [emoji]` | Reaction hàng loạt |
| `.tokenspam [delay] [text]` | Spam đa token |
| `.tokenvc [ID voice]` | Treo voice đa token |
| `.vcspam [ID voice]` | Spam join/leave voice |
| `.stop` / `.stopspam` / `.stopnhay` / `.stopwebhook` / `.stopvcspam` / `.stoptokenspam` | Dừng tất cả thuật thức đang chạy |

### Nhạc
| Lệnh | Mô tả |
|------|-------|
| `.xanhac [ID] [tên file]` | Phát nhạc trong voice |
| `.vcjoin [ID] [Y/N] [Y/N] [Y/N]` | Join voice (mute/deafen/camera) |
| `.vcleave` | Rời voice |
| `.forcedisconnect [@user]` | Ngắt người dùng khỏi voice |
| `.stopforcedisconnect` | Dừng forcedisconnect |

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
| `.math [phép tính]` | Máy tính |
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

### Quản lý
| Lệnh | Mô tả |
|------|-------|
| `.kick @user` | Kick thành viên |
| `.ban @user` | Ban thành viên |
| `.unban ID` | Unban |

### Troll / Giải trí
| Lệnh | Mô tả |
|------|-------|
| `.troll` | Danh sách lệnh troll |
| `.nsfw [loại]` | NSFW (anal/hanal/4k/gif/pussy/boobs/ass/hboobs/thighs) |
| `.succac` | Hiệu ứng |
| `.rainbowrole [@role]` | Role 7 màu |
| `.rizz [@user]` | Random câu tán tỉnh |
| `.roast [@user]` | Random câu roast |
| `.cat` | Ảnh mèo ngẫu nhiên |
| `.phc [@user] [text]` | PornHub comment |
| `.rpc playing [tên]` | Đang chơi game |
| `.rpc streaming [tên]` | Đang stream |
| `.rpc listening [tên]` | Đang nghe |
| `.rpc watching [tên]` | Đang xem |
| `.stoprpc` | Dừng RPC |
| `.autoreact on/off` | Bật/tắt tự reaction |
| `.afk [lý do]` | AFK |
| `.unafk` | Bỏ AFK |

---

## Cấu trúc thư mục

```
VVNK/
├── bot.py              # Entry point
├── Run.bat             # Launcher tự động
├── install.bat         # Cài thư viện
├── install.py          # Script cài tự động
├── config/
│   └── config.json     # Token + prefix + webhook (bị gitignore)
├── requirements.txt    # Thư viện
├── .gitignore
│
├── cogs/
│   ├── cycstatus.txt   # Status tự động chuyển
│   └── nhay.txt        # Nội dung spam .nhay
├── music/              # File nhạc (.mp3, .wav, .ogg)
├── ffmpeg/             # FFmpeg (Windows)
└── datoken.txt         # Token phụ (cho tokenspam)
```

---

## Fix lỗi

- **Bot không phản hồi**: Kiểm tra token trong `config/config.json` đúng chưa
- **Lỗi play nhạc**: Cần FFmpeg - tải https://ffmpeg.org/download.html
- **Bị rate limit**: Bot xử lý tự động, đợi vài phút rồi thử lại
- **Bot bị kick/khóa**: Dùng tài khoản alt, không phải tài khoản chính

---

**QU4N.TH3.D3V** | VVNK Bot v1.0
