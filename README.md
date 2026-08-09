# VVNK - QU4N.TH3.D3V

**Self-bot Discord cho personal use - 1 click la chay!**

---

## Gioi thieu

VVNK la self-bot Discord duoc viet boi QU4N.TH3.D3V, ho tro rat nhau tinh nang tu spam, raid, troll, quan ly server, den cac tien ich hang ngay. Bot chay tren tai khoan nguoi dung (self-bot), giao dien don gian, de su dung.

---

## Cai dat

### Buoc 1: Tai source code
- Vao: https://github.com/nguyenminhquan2012ct-oss/VVNK_QU4N.TH3.D3V
- Nhan **Code** -> **Download ZIP**
- Giai nen vao thu muc bat ky

### Buoc 2: Cai Python 3.9+
Tai Python tai: https://python.org

**Windows:**
- Chon "Add Python to PATH" khi cai
- Sau do double-click `Run.bat` la xong!

**Mac / Linux:**
```bash
python3 --version   # kiem tra
python3 index.py    # chay bot
```

### Buoc 3: Nhap Token
- Lan dau chay, bot se tu dong mo notepad de nhap token
- Paste token vao giua 2 dau ngoac: `"token": "DAY_LA_TOKEN_CUA_BAN"`
- Save file -> bot se tu dong tiep tuc

**Lay token o dau?**
- Vao https://discord.com/developers/applications
- Tao Application moi -> di vao **Bot** -> **Copy Token**

---

## Cau truc thu muc

```
VVNK/
├── bot.py              ← File chinh (1952 dong code!)
├── Run.bat             ← 1 click chay (Windows)
├── install.bat         ← 1 click cai thu vien
├── install.py          ← Script cai tu dong
├── config/
│   └── config.json     ← Token + prefix + webhook
├── cogs/
│   ├── cycstatus.txt   ← Status tu dong chuyen
│   └── nhay.txt        ← Noi dung spam .nhay
├── music/              ← File nhac (.mp3, .wav, .ogg)
├── ffmpeg/             ← Dat ffmpeg.exe vao day (Windows)
├── datoken.txt         ← Token phu (cho lenh tokenspam)
└── requirements.txt    ← Danh sach thu vien
```

---

## Danh sach lenh

### Lenh chinh
| Lenh | Mo ta |
|------|-------|
| `.menu` | Mo bang dieu khien |
| `.botinfo` | Thong tin bot |
| `.restart` | Khoi dong lai bot |
| `.shutdown` | Tat bot |

### Quan ly server
| Lenh | Mo ta |
|------|-------|
| `.kick @user` | Kick thanh vien |
| `.ban @user` | Ban thanh vien |
| `.unban ID` | Unban |

### Spam / Raid
| Lenh | Mo ta |
|------|-------|
| `.spam [delay] [noi dung]` | Spam tin nhan |
| `.nhay [delay]` | Spam tu nhay.txt |
| `.webhook [url] [noi dung]` | Spam qua webhook |
| `.nuke [ten] [noi dung]` | Pha server |
| `.bomb` | Xoa toan bo kenh |
| `.massreact [so] [emoji]` | Them reaction hang loat |
| `.tokenspam [delay] [noi dung]` | Spam da token |
| `.tokenvc [ID voice]` | Treo voice da token |
| `.vcspam [ID voice]` | Spam join/leave voice |
| `.stop` / `.stopspam` / `.stopnhay` / `.stopwebhook` / `.stopvcspam` / `.stoptokenspam` | Dung cac lenh dang chay |

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

### Voice
| Lenh | Mo ta |
|------|-------|
| `.vcjoin [ID] [Y/N] [Y/N] [Y/N]` | Join voice (mute/deafen/camera) |
| `.vcleave` | Roi voice |
| `.xanhac [ID] [ten file]` | Phat nhac trong voice |
| `.forcedisconnect [@user]` | Ngat nguoi dung khoi voice |
| `.stopforcedisconnect` | Dung forcedisconnect |

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
| `.phc [@user] [noi dung]` | PornHub comment |
| `.rpc playing [ten]` | Dang choi game |
| `.rpc streaming [ten]` | Dang stream |
| `.rpc listening [ten]` | Dang nghe |
| `.rpc watching [ten]` | Dang xem |
| `.stoprpc` | Dung RPC |
| `.autoreact on/off` | Bat/tat tu reaction |
| `.afk [ly do]` | AFK |
| `.unafk` | Bo AFK |

---

## Ho tro nen tang

| Nen tang | Trang thai |
|----------|------------|
| Windows | Ho tro |
| Mac | Ho tro (dung `python3`) |
| Linux | Ho tro (dung `python3`) |

---

## Luu y quan trong

- Day la **self-bot** - chay tren tai khoan nguoi dung, vi Discord Terms of Service
- **Nhat thiet** dung tai khoan phu (alt) de tranh bi ban
- Chi dung cho muc dich hoc tap, thu nghiem
- Tac gia **khong chiu trach nhiem** ve bat ky hau qua nao khi su dung
- **KHONG** dung vao muc dich gay hai nguoi khac

---

**Author: QU4N.TH3.D3V**
