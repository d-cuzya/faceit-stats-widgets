import requests
import json

nickname = "d_cuzya"

urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}"
headersStr = {
    'Authorization': 'Bearer e3411b15-6b74-4ae6-8a07-043120045f85',
}
paramsStr = {
    "game" :"cs2"
}
response = requests.get(url=urlStr, headers=headersStr, params=paramsStr)

print(json.dumps(response.json(), indent=2))

playerid = response.json()["player_id"]
# game_player_id = response.json()["games"]["cs2"]["game_player_id"]
# print(game_player_id)
response.close()
usrStr = f"https://open.faceit.com/data/v4/players/{playerid}/stats/cs2"
# urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}&game=cs2&game_player_id={game_player_id}"
# responseTwo = requests.get(url=urlStr, headers=headersStr, params=paramsStr)
# print(json.dumps(responseTwo.json(), indent=2))