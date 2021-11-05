import base64, requests, os
import sys
import json
import urllib3


http = urllib3.PoolManager()


def get_game(titleID: str, search_term: str):
    search_term = search_term.replace("\'", "") # replace \' for Astro's Playground for example
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term
    r = http.request('GET', url)

    data = json.loads(r.data.decode('utf-8'))

    if data is None:
        return None, None

    if "message" in data.values():
        if data['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None, None

    all_games = data['data']['universalSearch']['results']
    searched_game = next((item for item in all_games if titleID in item["id"].lower()), None)

    # if we didnt find the specific game we just want to use the first one which is generally the right one
    # from this we get the picture but use the other one
    if searched_game is None:
        searched_game = all_games[0]


    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    pic_dl = http.request('GET', url=picture['url'])

    return searched_game, pic_dl.data

def get_game_with_url(titleID: str, search_term: str):
    search_term = search_term.replace("\'", "") # replace \' for Astro's Playground for example
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term
    r = http.request('GET', url)

    data = json.loads(r.data.decode('utf-8'))

    if data is None:
        return None, None

    if "message" in data.values():
        if data['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None, None

    all_games = data['data']['universalSearch']['results']

    searched_game = next((item for item in all_games if titleID in item["id"].lower()), None)

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    return searched_game, picture['url']

def get_game_picture_url(titleID: str, search_term: str):
    search_term = search_term.replace("\'", "") # replace \' for Astro's Playground for example
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term
    r = http.request('GET', url)

    data = json.loads(r.data.decode('utf-8'))

    if data is None:
        return None, None

    if "message" in data.values():
        if data['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None, None

    all_games = data['data']['universalSearch']['results']

    searched_game = next((item for item in all_games if titleID in item["id"].lower()), None)

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    return picture['url']

def get_game_picture_data(titleID: str, search_term: str):
    search_term = search_term.replace("\'", "") # replace \' for Astro's Playground for example
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term
    r = http.request('GET', url)

    data = json.loads(r.data.decode('utf-8'))

    if data is None:
        return None, None

    if "message" in data.values():
        if data['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None, None

    all_games =  data['data']['universalSearch']['results']

    searched_game = next((item for item in all_games if titleID in item["id"].lower()), None)

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")
    pic_dl = http.request('GET', url=picture['url'])

    return pic_dl.data
