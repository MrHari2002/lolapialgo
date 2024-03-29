import requests
import time
import json

def fetch_game_stats():
    """Fetch game stats from the provided URL."""
    try:
        # Bypass SSL verification for HTTPS - use with caution and consider security implications.
        response = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayer', verify=False)
        return response
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def write_stats_to_file(game_stats):
    """Append the fetched game stats to a file."""
    with open("game_stats.txt", "a") as file:  # 'a' mode for appending data
        file.write(json.dumps(game_stats, indent=4))
        file.write("\n\n New Data")  # Add some space between entries for readability

def main():
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
