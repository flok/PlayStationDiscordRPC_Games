import json, os, sys, base64
import yaml
from requests.models import HTTPError
from discord_assets import get_assets, add_asset, delete_asset
from playstation_api import get_game, get_game_picture_data

# parse DC token to global variable
TOKEN = sys.argv[1]

registered_games = [game['name'] for game in get_assets()]
supported_games = yaml.load(open('supported_games.yaml'), Loader=yaml.FullLoader)

for game in supported_games:
    titleID = game['ID'].lower()
    search_term = game['SEARCH_TERM']
    if titleID in registered_games:
        print(f"{titleID} already an asset")
        continue

    game_info, picture = get_game(titleID ,search_term)

    if game_info is None or picture is None:
        continue

    picture_encoded = base64.b64encode(picture)

    status_asset = add_asset(titleID, 'data:image/png;base64,%s' % picture_encoded.decode('utf-8'))

    print(f"Status Asset {status_asset}")
    print(f"Added Game {game_info['npTitleId']} with Name : {game_info['name']}")