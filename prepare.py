"""
Create needed files for every day from beginning to current
"""

import requests
from bs4 import BeautifulSoup as soup
from markdownify import markdownify
import os
from datetime import date
import shutil
import tomllib

today = date.today().day
year = str(date.today().year)

files = os.listdir(".")
sessioncookie = {}

# read session cookie from separate file
with open("session.toml", "rb") as toml:
    sessioncookie.update({"session": tomllib.load(toml).get("session")}) 

for d in range(1, today + 1):
    d = str(d)
    if d not in files:
        try:
            os.mkdir(d)
            print(f"Created folder for {d}")
        except FileExistsError:
            pass 

    
    if "info.md" not in os.listdir(f"./{d}"):
        dailytask = requests.get(f"https://adventofcode.com/{year}/day/{d}", cookies=sessioncookie)
        content = str(soup(dailytask.content, 'html.parser').find('article'))
        md = markdownify(content)

        try:
            with open(f"{d}/info.md", "x") as f:
                f.write(md)
                print(f"Created task info for {d} (part 1)")
        except:
            print(f"Couldn't create new info file for day {d}")

    if "main.py" not in os.listdir(f"./{d}"):
        shutil.copyfile("skeleton.py", f"./{d}/main.py")
        print(f"Created main.py for day {d}")

    if "input" not in os.listdir(f"./{d}"):
        input = requests.get(f"https://adventofcode.com/{year}/day/{d}/input", cookies=sessioncookie).text
        try:
            with open(f"{d}/input", "x") as f:
                f.write(input)
                print(f"Created input file for {d}")
        except:
            print(f"Couldn't create new input file for day {d}")