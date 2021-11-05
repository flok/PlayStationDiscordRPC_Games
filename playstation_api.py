import base64, requests, os
import sys

API_SEARCH = 'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"Marvel%27s%20Spider-Man:%20Miles%20Morales%20Ultimate%20Edition"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}'


def get_game(titleID: str, search_term: str):
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term

    r = requests.get(url=url)
    r.raise_for_status()
    if "message" in r.json().values():
        if r.json()['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None

    all_games =  r.json()['data']['universalSearch']['results']

    searched_game = next(item for item in all_games if titleID in item["id"].lower())

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    pic_dl = requests.get(url=picture['url'])
    pic_dl.raise_for_status()

    return searched_game, pic_dl.content

def get_game_with_url(titleID: str, search_term: str):
    search_term = search_term.replace("\'", "") # replace \' for Astro's Playground for example

    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term

    r = requests.get(url=url)
    print(f"Status Code : {r.status_code}")

    if r.json() is None:
        return None, None
    #r.raise_for_status()
    if "message" in r.json().values():
        if r.json()['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None, None

    all_games =  r.json()['data']['universalSearch']['results']

    searched_game = next(item for item in all_games if titleID in item["id"].lower())

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    return searched_game, picture['url']

def get_game_picture_url(titleID: str, search_term: str):
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term

    r = requests.get(url=url)
    r.raise_for_status()
    if "message" in r.json().values():
        if r.json()['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None

    all_games = r.json()['data']['universalSearch']['results']

    searched_game = next(item for item in all_games if titleID in item["id"].lower())

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")
    return picture['url']

def get_game_picture_data(titleID: str, search_term: str):
    url = r'https://web.np.playstation.com/api/graphql/v1//op?operationName=getSearchResults&variables={"countryCode":"US","languageCode":"en","searchTerm":"%s"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"d77d9a513595db8d75fc26019f01066d54c8d0de035a77a559bd687fa1010418"}}' % search_term
    print(url)
    r = requests.get(url=url)
    r.raise_for_status()
    if "message" in r.json().values():
        if r.json()['message'] == "Query not whitelisted":
            print("query whitelist error")
            return None

    all_games = r.json()['data']['universalSearch']['results']
    
    searched_game = next(item for item in all_games if titleID in item["id"].lower())

    picture = next(item for item in searched_game['media'] if item["role"] == "MASTER")

    pic_dl = requests.get(url=picture['url'])
    pic_dl.raise_for_status()

    return pic_dl.content
