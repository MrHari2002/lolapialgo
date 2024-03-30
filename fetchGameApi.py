import requests
import time
import json

def fetch_game_stats():
    """Fetch game stats from the provided URL."""
    try:
        # Bypass SSL verification for HTTPS - use with caution and consider security implications.
        response = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify=False)
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def fetch_ative_player():
    """Fetch game stats from the provided URL."""
    try:
        # Bypass SSL verification for HTTPS - use with caution and consider security implications.
        response = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayer', verify=False)
        reformatted_data = ""
        for player in response:
                        # Extract the required information for each player
                        player_info = player["championName"] + "Team" +player["team"]+ "IsDead" + str(player["isDead"]) + "RespawnTimer"+  str(player["respawnTimer"])
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
    
def write_stats_to_file(game_stats):
    """Append the fetched game stats to a file."""
    with open("game_stats.txt", "a") as file:  # 'a' mode for appending data
        file.write(json.dumps(game_stats, indent=4))
        file.write("\n\n New Data")  # Add some space between entries for readability


def main():
    active_player = fetch_ative_player

    while True:
        response = fetch_game_stats()
        
        if response and response.status_code == 200:
            game_stats = response.json()
            write_stats_to_file(game_stats)
            # Wait for about 2 minutes before the next fetch
            time.sleep(120)
            print('Data Fetched')
        else:
            print("Game over or unable to fetch data.")
            break

if __name__ == "__main__":
    main()
