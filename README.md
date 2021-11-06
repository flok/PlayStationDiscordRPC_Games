# PlayStationDiscordRPC_Games
Supported PS5 games used by PlayStationDiscordRPC

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

If i merge the changes the game will be automatically added to the discord application and should available a short time after that.

## Supported Games

|                                                Icon                                                 |  TitleID   |                    Name                    |
|-----------------------------------------------------------------------------------------------------|------------|--------------------------------------------|
|<img src="https://image.api.playstation.com/vulcan/ap/rnd/202010/2012/T3h5aafdjR8k7GJAG82832De.png"> |PPSA01325_00|ASTRO's PLAYROOM                            |
|<img src="https://image.api.playstation.com/vulcan/ap/rnd/202008/1020/T45iRN1bhiWcJUzST6UFGBvO.png"> |PPSA01411_00|Marvel's Spider-Man: Miles Morales PS4 & PS5|
|<img src="https://image.api.playstation.com/vulcan/img/rnd/202010/1908/35Fq1N8ZBaOsh2odxMBGvjUj.png">|CUSA16283_00|F1 2020                                     |

