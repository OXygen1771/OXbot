import discord

from core.config import cfg


class OXbot(discord.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Получаем доступ к событиям Дискорда и содержимому сообщений

        self.config = cfg

        super().__init__(intents=intents)

    async def on_ready(self):
        print('Bot\'s up and running!')


def main():
    bot = OXbot()
    bot.run(bot.config.token)


if __name__ == '__main__':
    main()
