

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from Bikashhalder.utils import load_plugins
import logging
from telethon import events
from . import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "BikashHalder/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("superfast Bgt Spam Bot Successfully Deployed superfast @BikashHalder @AdityaHalder")
print("Enjoy! Do visit @Bgt_Chat")

if __name__ == "__main__":
    BOT0.run_until_disconnected()
    
if __name__ == "__main__":
    BOT1.run_until_disconnected()

if __name__ == "__main__":
    BOT2.run_until_disconnected()
    
if __name__ == "__main__":
    BOT3.run_until_disconnected()

if __name__ == "__main__":
    BOT4.run_until_disconnected()
    
if __name__ == "__main__":
    BOT5.run_until_disconnected()
    
if __name__ == "__main__":
    BOT6.run_until_disconnected()

if __name__ == "__main__":
    BOT7.run_until_disconnected()
    
if __name__ == "__main__":
    BOT8.run_until_disconnected()

if __name__ == "__main__":
    BOT9.run_until_disconnected()    
