import requests
from openai import OpenAI
# get control of our keyboard
from pynput.keyboard import Listener, Key, Controller
# time variables


def fetch_game_stats():
    """Fetch game stats from the provided URL."""
    try:
        # Bypass SSL verification for HTTPS - use with caution and consider security implications.
        response = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify=False)
        data = response.json()
        reformatted_data = ""
        for player in data:
                        # Extract the required information for each player
                        player_info = player["championName"] + "Team" + player["team"]+ "IsDead" + str(player["isDead"]) + "RespawnTimer" + str(player["respawnTimer"])

                        for item in player.get("items", []):
                            player_info += item["displayName"]+ ""
                        player_info += player["summonerSpells"]["summonerSpellOne"]["displayName"]
                        player_info += player["summonerSpells"]["summonerSpellTwo"]["displayName"]
                        
                        # Add the reformatted player information to the list
                        reformatted_data+=player_info+"\n"
        return reformatted_data
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def fetch_ative_player():
    """Fetch game stats from the provided URL."""
    try:
        # Bypass SSL verification for HTTPS - use with caution and consider security implications.
        response = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayer', verify=False)
        return str(response.json())

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None
    
def chatgpt_analyse(player,content):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a league of ledgends coach, provide recommendation for the following player." + player},
        {"role": "user", "content": content}
    ]
    )
    return completion.choices[0].message.content

def yxcMethod():
    active_player = fetch_ative_player()
    response = fetch_game_stats()
    anlysis = chatgpt_analyse(active_player,response)
    print(anlysis)
    return anlysis




