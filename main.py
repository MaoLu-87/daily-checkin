import asyncio
import os

from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
TG_SESSION = os.environ["TG_SESSION"]
TG_TARGET = os.environ["TG_TARGET"]
TG_COMMAND = os.environ.get("TG_COMMAND", "/sign")


async def main():
    async with TelegramClient(StringSession(TG_SESSION), API_ID, API_HASH) as client:
        if not await client.is_user_authorized():
            raise SystemExit("TG_SESSION 已失效，请重新导出 StringSession 并更新 Secret")
        await client.send_message(TG_TARGET, TG_COMMAND)
        print("签到指令已发送")


if __name__ == "__main__":
    asyncio.run(main())
