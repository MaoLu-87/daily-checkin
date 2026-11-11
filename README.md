# daily-checkin

通过 Telegram 定时发送签到指令。

## 配置

在 Settings → Secrets and variables → Actions 中添加：

| Secret | 说明 |
|---|---|
| `API_ID` | Telegram 应用标识 |
| `API_HASH` | 同上 |
| `TG_SESSION` | StringSession 登录态 |
| `TG_TARGET` | 接收指令的会话标识 |
| `TG_COMMAND` | 可选，默认 `/sign` |

## 运行

- 定时：`.github/workflows/cron.yml` 中配置（UTC 00:20）
- 手动：Actions → Auto Checkin → Run workflow

本地运行：

```bash
pip install telethon
API_ID=xxx API_HASH=xxx TG_SESSION=xxx TG_TARGET=xxx python main.py
```

## 更新登录态

`TG_SESSION` 失效时脚本以 `TG_SESSION 已失效` 退出。重新导出：

```python
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
```

完成交互式登录后，把输出写入 `TG_SESSION` Secret。
