# KK-Bot

A Discord bot that automatically fixes Instagram and TikTok video embeds by converting links to `kkclip.com`.

## Features

- Converts Instagram and TikTok links (including short links like `vm.tiktok.com`) to `www.kkclip.com`.
- Removes tracking query parameters (`?igsh=...`, `?_t=...`).
- Replies with a clean `[Fixed Embed](https://...)` link without pinging users.
- Ignores bot accounts to prevent message loops.

## Discord Setup

1. Create an app in the [Discord Developer Portal](https://discord.com/developers/applications).
2. In the **Bot** tab:
   - Reset and copy your bot **Token**.
   - Enable **Message Content Intent**.
3. In **OAuth2** -> **URL Generator**:
   - Scopes: `bot`
   - Permissions: `Read Messages/View Channels`, `Send Messages`, `Read Message History`
   - Invite the bot using the generated URL.

## Configuration

Copy the example file and add your bot token:

```bash
cp .env.example .env
```

```env
DISCORD_TOKEN=your_bot_token_here
```

## Usage

### Run with Python
```bash
pip install -r requirements.txt
python bot.py
```

### Run with Docker
```bash
docker compose up -d --build
```

### Run Tests
```bash
python -m pytest test_link_transformer.py -v
```
