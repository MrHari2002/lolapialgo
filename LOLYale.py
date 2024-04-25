import json
import requests
from openai import OpenAI
# get control of our keyboard
from pynput.keyboard import Listener, Key, Controller
# time variables
import time
# use to mimic human typing
import numpy as np
# initially we use this to retrive text from textboard, but the access of clipboard is banned by LOL,
# Thus, we decide to mimic human typing and type our retrived text to the chatbox in LOL.
# import win32clipboard as w  (no linger needed)


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
        {"role": "system", "content": "You are a league of ledgends coach, provide recommendation for the following player:" + player +"in 25 words or less."},
        {"role": "user", "content": content}
    ]
    )
    return completion.choices[0].message.content


def press(k):
    try :
        # print(k)
        if k == Key.f8 :
            print('Loading result from gpt......')
            # retriving text from ChatGPT           
            cheerText = yxcMethod()
            # wait for gpt to generate texts
            time.sleep(5)
            
            keyboard = Controller()            
            keyboard.press(Key.enter)
            time.sleep(0.5)
            keyboard.release(Key.enter)
            # type texts into chatbox
            for x in range(len(cheerText)):
                for y in cheerText[x]:
                    keyboard.press(y)
                    time.sleep(np.random.uniform(low=0.02, high=0.05))
                    keyboard.release(y)
                    time.sleep(np.random.uniform(low=0.03, high=0.07))

            keyboard.press(Key.enter)
            time.sleep(0.23)
            keyboard.release(Key.enter)
            
            
    # diagnose
    except Exception as e:
        print("The following error occurred: ", e)

def yxcMethod():
    active_player = fetch_ative_player()
    response = fetch_game_stats()
    anlysis = chatgpt_analyse(active_player,response)
    return anlysis

with Listener(on_press=press) as listener:
    listener.join()