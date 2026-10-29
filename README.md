# KK-Bot

A Discord bot that monitors messages for Instagram and TikTok links. It replies to the message with embed-friendly `kkinstagram.com` and `kktiktok.com` links.

## Features

- Converts Instagram links (`instagram.com`) to `www.kkinstagram.com`.
- Converts standard TikTok links (`tiktok.com`) to `www.kktiktok.com`.
- Converts short TikTok links (`vm.tiktok.com`, `vt.tiktok.com`) to `vm.kktiktok.com`.
- Strips URL tracking parameters (e.g., `?igsh=...`, `?_t=...`).
- Replies directly to the original message without pinging the author (`mention_author=False`).
- Deduplicates identical links sent in the same message.
- Ignores messages from other bots to prevent loops.

---

## Discord Developer Portal Configuration

1. Open the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give your bot a name (for example, `KK-Bot`).
3. Navigate to **Bot** in the left sidebar:
   - Click **Reset Token** and copy the bot token.
   - Scroll down to **Privileged Gateway Intents**.
   - Enable **Message Content Intent**.
4. Navigate to **OAuth2** -> **URL Generator**:
   - Under **Scopes**, select `bot`.
   - Under **Bot Permissions**, select:
     - `Read Messages/View Channels`
     - `Send Messages`
     - `Send Messages in Threads`
     - `Read Message History`
   - Copy the generated URL and open it in your browser to invite the bot to your server.

---

## Local Setup

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.12)
- Git

### 2. Installation
Clone the repository and create a virtual environment:

```bash
git clone <repository-url>
cd KK-Bot
python -m venv .venv
```

Activate the virtual environment:
- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Copy the example environment file:
```bash
cp .env.example .env
```
Edit `.env` and set your token:
```env
DISCORD_TOKEN=your_bot_token_here
```

### 4. Run Tests
```bash
python -m pytest test_link_transformer.py -v
```

### 5. Start the Bot Locally
```bash
python bot.py
```

---

## Deployment (Oracle Cloud / Docker)

### 1. Prerequisites on the Server
- Docker
- Docker Compose

### 2. Run with Docker Compose
1. Copy project files to your server.
2. Create `.env` file on the server with your `DISCORD_TOKEN`.
3. Start the container in detached mode:
   ```bash
   docker compose up -d --build
   ```

### 3. View Logs
```bash
docker compose logs -f
```

### 4. Stop the Bot
```bash
docker compose down
```

