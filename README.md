# PlayStationDiscordRPC_Games
Supported PS5 games used by PlayStationDiscordRPC 


## Support new game

The tool automatically downloads the asset the wanted game if the right titleID and search term is defined. The search should be the exact name thats is displayed on the RPC inside discord.
To support a new game simply add the game to the `supported_games.yaml` file like this:

From this:
```
-
  ID: PPSA01325_00
  SEARCH_TERM: ASTRO's PLAYROOM
-
  ID: PPSA01411_00
  SEARCH_TERM: "Marvel's Spider-Man: Miles Morales"
```

to this:

```
-
  ID: PPSA01325_00
  SEARCH_TERM: ASTRO's PLAYROOM
-
  ID: PPSA01411_00
  SEARCH_TERM: "Marvel's Spider-Man: Miles Morales"
-
  ID: PPSA09999_00
  SEARCH_TERM: "New Game Search Term that find it throught the Store"

```

If i merge the changes the game will be automatically added to the discord application and should available a short after that.
