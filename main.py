import requests
import json

nickname = "d_cuzya"
headersStr = {
    'Authorization': 'Bearer e3411b15-6b74-4ae6-8a07-043120045f85',
}

urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}"
response = requests.get(url=urlStr, headers=headersStr)
player_id = response.json()["player_id"]
print(json.dumps(response.json(), indent=2))
# print(player_id)

# # Map statistics
# urlStr = f"https://open.faceit.com/data/v4/players/{player_id}/stats/cs2"
# response = requests.get(url=urlStr, headers=headersStr)
# print(json.dumps(response.json(), indent=2))

count_for_estimation = 10 

urlStr = f"https://open.faceit.com/data/v4/players/{player_id}/games/cs2/stats?limit={count_for_estimation}"
response = requests.get(url=urlStr, headers=headersStr)
print(json.dumps(response.json(), indent=2))