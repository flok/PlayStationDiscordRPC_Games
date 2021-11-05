import sys, os

from requests.api import get
from discord_assets import get_assets
from playstation_api import get_game_with_url
import yaml

# parse DC token to global variable
TOKEN = sys.argv[1]

# get current assets
registered_games = [game['name'] for game in get_assets()]
supported_games = yaml.load(open('supported_games.yaml'), Loader=yaml.FullLoader)


table = ["| Picture | Name |", "|: ---------- :|: --------- :|"]

# loop over assets
for game in supported_games:
    
    title = game['ID'].lower()
    search_term = game['SEARCH_TERM']
    if title not in registered_games:
        continue

    game, url = get_game_with_url(titleID=title, search_term=search_term)
    table.append(f"| ![Alt Text]({url}) | {game['name']} |")


# replace readme parts

readme = open('README_template.md', 'r').read()
readme = readme.replace('*games*', '\n'.join(table))
open('README.md', 'w').write(readme)
