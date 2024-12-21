import requests
import json

nickname = "d_cuzya"
headersStr = {
    'Authorization': 'Bearer e3411b15-6b74-4ae6-8a07-043120045f85',
}

urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}"
response = requests.get(url=urlStr, headers=headersStr)
game_player_id = response.json()["games"]["cs2"]["game_player_id"]
print(json.dumps(response.json(), indent=2))

# urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}&game=cs2&game_player_id={game_player_id}"
# response = requests.get(url=urlStr, headers=headersStr)
# print(json.dumps(response.json(), indent=2))