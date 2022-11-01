import discord


class OXbot(discord.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Получаем доступ к событиям дискорда и содержимому сообщений

        super().__init__(intents=intents)

    async def on_ready(self):
        print('Bot\'s up and running!')


def main():
    bot = OXbot()
    bot.run()


if __name__ == '__main__':
    main()
