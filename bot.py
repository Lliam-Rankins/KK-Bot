import logging
import os
import sys
import discord
from dotenv import load_dotenv
from link_transformer import transform_urls

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("kk_bot")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    logger.error("DISCORD_TOKEN is not set. Add it to your .env file.")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    if client.user:
        logger.info("Bot connected as %s (ID: %s)", client.user.name, client.user.id)


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot:
        return

    links = transform_urls(message.content)
    if not links:
        return

    reply_content = "\n".join(links)
    try:
        await message.reply(reply_content, mention_author=False)
        logger.info(
            "Replied with %d link(s) to user %s in guild %s",
            len(links),
            message.author.id,
            message.guild.id if message.guild else "DM",
        )
    except discord.Forbidden:
        logger.warning(
            "Missing permissions to reply in channel %s (guild %s)",
            message.channel.id,
            message.guild.id if message.guild else "DM",
        )
    except discord.HTTPException as exc:
        logger.error("Failed to send message: %s", exc)


def main() -> None:
    client.run(TOKEN)


if __name__ == "__main__":
    main()
