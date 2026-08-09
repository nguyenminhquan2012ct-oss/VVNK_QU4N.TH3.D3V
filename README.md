# VVNK v1.0

Discord Self-Bot voi nhieu tinh nang: spam, raid, nhac, giai tri, quan ly, tien ich.

> ⚠️ Self-bot vi pham Discord ToS. Su dung tai khoan alt. Chu nhan chap nhan moi rui ro.

---

## Cach tai

### Cach 1: Tai file ZIP
1. Vao: https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V
2. Nut **Code** (mau xanh) → **Download ZIP**
3. Giai nen thu muc `VVNK-main`

### Cach 2: Clone (can Git)
```bash
git clone https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V.git
```

---

## Cach chay

1. Mo thu muc `VVNK`
2. Double-click **`Run.bat`**
3. Lan dau hoi **Discord Token** → nhap vao
4. Bot tu dong cai thu vien va khoi dong
5. Bot tu dong restart neu crash

Hoac chay thu cong:
```bash
python -m pip install -r requirements.txt
python bot.py
```

---

## Cau hinh

File `config/config.json` (tu tao boi Run.bat):
```json
{
    "token": "DISCORD_TOKEN_CUA_BAN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

---

## Danh sach lenh

### Menu chinh
| Lenh | Mo ta |
|------|-------|
| `.menu` | Hien thi menu chinh |
| `.botinfo` | Thong tin bot |
| `.restart` | Khoi dong lai bot |
| `.shutdown` | Tat bot |

### War / Spam
| Lenh | Mo ta |
|------|-------|
| `.spam [delay] [text]` | Spam tin nhan |
| `.nhay [delay]` | Spam tu nhay.txt |
| `.webhook [url] [text]` | Spam qua Webhook |
| `.nuke [ten] [text]` | Pha server |
| `.bomb` | Xoa toan bo kenh |
| `.massreact [so] [emoji]` | Reaction hang loat |
| `.tokenspam [delay] [text]` | Spam da token |
| `.tokenvc [ID voice]` | Treo voice da token |
| `.vcspam [ID voice]` | Spam join/leave voice |
| `.stop` / `.stopspam` / `.stopnhay` / `.stopwebhook` / `.stopvcspam` / `.stoptokenspam` | Dung tat ca thuat thuc dang chay |

### Nhac
| Lenh | Mo ta |
|------|-------|
| `.xanhac [ID] [ten file]` | Phat nhac trong voice |
| `.vcjoin [ID] [Y/N] [Y/N] [Y/N]` | Join voice (mute/deafen/camera) |
| `.vcleave` | Roi voice |
| `.forcedisconnect [@user]` | Ngat nguoi dung khoi voice |
| `.stopforcedisconnect` | Dung forcedisconnect |

### Tien ich
| Lenh | Mo ta |
|------|-------|
| `.tienich` | Danh sach tien ich |
| `.clear [so]` | Xoa tin nhan |
| `.hackclear` | Xoa chat bang tin nhan trong |
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |
| `.serverinfo` | Thong tin server |
| `.iplookup [IP]` | Tra cuu IP |
| `.insta [ten]` | Xem Instagram |
| `.math [phep tinh]` | May tinh |
| `.cloneemoji [emoji]` | Sao chep emoji |
| `.clone_channels [ID cu] [ID moi]` | Sao chep kenh |
| `.clone_roles [ID cu] [ID moi]` | Sao chep role |
| `.deleteallroles` | Xoa tat ca role |
| `.closealldms` | Dong tat ca DM |
| `.delfriends` | Xoa tat ca ban be |
| `.tokencheck [token]` | Kiem tra token |
| `.checkpromo [link]` | Kiem tra Nitro promo |
| `.cyclestatus` | Tu dong chuyen status |
| `.addstatus [text]` | Them status |
| `.clearstatus` | Xoa tat ca status |
| `.setstatus [text]` | Dat status |

### Quan ly
| Lenh | Mo ta |
|------|-------|
| `.kick @user` | Kick thanh vien |
| `.ban @user` | Ban thanh vien |
| `.unban ID` | Unban |

### Troll / Giai tri
| Lenh | Mo ta |
|------|-------|
| `.troll` | Danh sach lenh troll |
| `.nsfw [loai]` | NSFW (anal/hanal/4k/gif/pussy/boobs/ass/hboobs/thighs) |
| `.succac` | Hieu ung |
| `.rainbowrole [@role]` | Role 7 mau |
| `.rizz [@user]` | Random cau tan tinh |
| `.roast [@user]` | Random cau roast |
| `.cat` | Anh meo ngau nhien |
| `.phc [@user] [text]` | PornHub comment |
| `.rpc playing [ten]` | Dang choi game |
| `.rpc streaming [ten]` | Dang stream |
| `.rpc listening [ten]` | Dang nghe |
| `.rpc watching [ten]` | Dang xem |
| `.stoprpc` | Dung RPC |
| `.autoreact on/off` | Bat/tat tu reaction |
| `.afk [ly do]` | AFK |
| `.unafk` | Bo AFK |

---

## Cau truc thu muc

```
VVNK/
├── bot.py              # Entry point
├── Run.bat             # Launcher tu dong
├── install.bat         # Cai thu vien
├── install.py          # Script cai tu dong
├── config/
│   └── config.json     # Token + prefix + webhook (bi gitignore)
├── requirements.txt    # Thu vien
├── .gitignore
│
├── cogs/
│   ├── cycstatus.txt   # Status tu dong chuyen
│   └── nhay.txt        # Noi dung spam .nhay
├── music/              # File nhac (.mp3, .wav, .ogg)
├── ffmpeg/             # FFmpeg (Windows)
└── datoken.txt         # Token phu (cho tokenspam)
```

---

## Fix loi

- **Bot khong phan hoi**: Kiem tra token trong `config/config.json` dung chua
- **Loi play nhac**: Can FFmpeg - tai https://ffmpeg.org/download.html
- **Bi rate limit**: Bot xu ly tu dong, doi vai phut roi thu lai
- **Bot bi kick/khoa**: Dung tai khoan alt, khong phai tai khoan chinh

---

**QU4N.TH3.D3V** | VVNK Bot v1.0
