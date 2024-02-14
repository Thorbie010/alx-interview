import requests
import sys

def get_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        film_data = response.json()
        characters_urls = film_data['characters']
        characters = []
        for character_url in characters_urls:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                characters.append(character_data['name'])
            else:
                print(f"Failed to fetch character data for {character_url}")
        return characters
    else:
        print("Failed to fetch film data.")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    characters = get_characters(movie_id)
    if characters:
        for character in characters:
            print(character)
