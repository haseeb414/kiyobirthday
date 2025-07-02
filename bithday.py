import time
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_cake():
    cake = f"""
       {Fore.YELLOW},   ,   ,   ,   ,{Style.RESET_ALL}
      {Fore.YELLOW}|)|_|)|_|)|_|)|_|{Style.RESET_ALL}
     {Fore.MAGENTA}\\ | | | | | | | | /{Style.RESET_ALL}
      {Fore.MAGENTA}\\| | | | | | | |/{Style.RESET_ALL}
       {Fore.CYAN}|~.~.~.~.~.~.~|{Style.RESET_ALL}
       {Fore.RED}|  H A P P Y  |{Style.RESET_ALL}
       {Fore.RED}|  B I R T H  |{Style.RESET_ALL}
       {Fore.RED}|  D A Y 💖   |{Style.RESET_ALL}
       {Fore.GREEN}| K I Y O 💐 |{Style.RESET_ALL}
       {Fore.CYAN}|_____________|{Style.RESET_ALL}
         {Fore.YELLOW}|||||||||{Style.RESET_ALL}
         {Fore.YELLOW}|||||||||{Style.RESET_ALL}
        {Fore.MAGENTA}(o)(o)(o){Style.RESET_ALL}
    """
    print(cake)

# 🎯 Set your target birthday date
target = datetime(2025, 9, 21, 0, 0, 0)

while True:
    now = datetime.now()
    diff = target - now

    if diff.total_seconds() <= 0:
        print(f"\n{Fore.GREEN}🎉🎂 Happy Birthday to Kiyo (Nidharsana)! 🎂🎉{Style.RESET_ALL}\n")
        print_cake()
        print(f"{Fore.MAGENTA}Dear Kiyo, you are so special to me. Wishing you love, light, and laughter always! 💕{Style.RESET_ALL}")
        break

    days = diff.days
    hours, rem = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    print("\033c", end="")  # clear screen

    print_cake()
    print(f"\n{Fore.YELLOW}⏳ Time Left for Kiyo's Birthday: {days} days, {hours:02d}:{minutes:02d}:{seconds:02d}{Style.RESET_ALL}")
    time.sleep(1)
