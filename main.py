import requests
import json
import yaml

with open("settings.yaml", 'r') as file:
    settings = yaml.safe_load(file)

nickname = settings['settings']['nickname']
headersStr = {
    'Authorization': f'Bearer {settings['settings']['faceit_api_key']}',
}

with open('player_info.json', 'w') as file:
    urlStr = f"https://open.faceit.com/data/v4/players?nickname={nickname}"
    response = requests.get(url=urlStr, headers=headersStr)
    player_id = response.json()["player_id"]
    json.dump(response.json(),file, indent=2)

with open('stats.json', 'w') as file:
    count_for_estimation = 10 
    urlStr = f"https://open.faceit.com/data/v4/players/{player_id}/games/cs2/stats?limit={count_for_estimation}"
    response = requests.get(url=urlStr, headers=headersStr)
    json.dump(response.json(), file,indent=2)