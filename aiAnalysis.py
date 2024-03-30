import openai
from openai import OpenAI


def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(content, file_path):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def analyze_with_chatgpt(content):
    """Send content to ChatGPT for analysis and return the response."""
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a LOL analysis you need to provide an analysis for the following game play"},
        {"role": "user", "content": content}
    ]
    )
    return completion.choices[0].message.content


def main():
    # Path to the input file and the output file
    input_file_path = 'game_stats.txt'
    output_file_path = 'analyzed_game_stats.txt'
    
    # Read the game stats from the file
    game_stats = read_file(input_file_path)
    
    # Send the game stats to ChatGPT for analysis
    analyzed_stats = analyze_with_chatgpt(game_stats)
    
    # Write the analyzed stats to another file
    write_file(analyzed_stats, output_file_path)
    
    print("Analysis complete. Check the analyzed_game_stats.txt file.")

if __name__ == "__main__":
    main()
