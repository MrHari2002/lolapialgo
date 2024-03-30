import json

with open('game_stats.json', 'r') as file:
    data = json.load(file)
    reformatted_data = ""
    for player in data:
                    # Extract the required information for each player
                    player_info = player["championName"] + "Team" +player["team"]+ "IsDead" + str(player["isDead"]) + "RespawnTimer"+  str(player["respawnTimer"])
                    for item in player.get("items", []):
                        player_info += item["displayName"]+ ""
                    player_info += player["summonerSpells"]["summonerSpellOne"]["displayName"]
                    player_info += player["summonerSpells"]["summonerSpellTwo"]["displayName"]
                    
                    # Add the reformatted player information to the list
                    reformatted_data+=player_info+"\n"

print(reformatted_data)