# PlayStationDiscordRPC_Games
Supported PS5 games used by [PlayStationDiscordRPC](https://github.com/flok/PlayStationDiscordRPC)

## Support new game

The tool automatically downloads the asset of the wanted game if the right titleID and search term is defined. With the seach term you should be able to find the game on [PlayStation Store](https://store.playstation.com/en-us/pages/latest) at the top right corner.

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

If I merge the changes the game will be automatically added to the Discord application and should available a short time after that. A restart of [PlayStationDiscordRPC](https://github.com/flok/PlayStationDiscordRPC) maybe necessary to see the image inside Discord.

## Supported Games

|                                                Icon                                                |  TitleID   |                    Name                    |
|----------------------------------------------------------------------------------------------------|------------|--------------------------------------------|
|<img src="https://image.api.playstation.com/vulcan/ap/rnd/202010/2012/T3h5aafdjR8k7GJAG82832De.png">|PPSA01325_00|ASTRO's PLAYROOM                            |
|<img src="https://image.api.playstation.com/vulcan/ap/rnd/202008/1020/T45iRN1bhiWcJUzST6UFGBvO.png">|PPSA01411_00|Marvel's Spider-Man: Miles Morales PS4 & PS5|

