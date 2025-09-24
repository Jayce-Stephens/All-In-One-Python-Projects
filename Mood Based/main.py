
def main():
    print("Welcome to the Mood Based Playlist Generator!")

    mood = input("Enter your current mood (happy, sad, energetic, calm): ").lower()
    print(f"Here is a playlist for your {mood} mood:")

    playlist = generate_playlist(mood)
    for i, song in enumerate(playlist):
        print(f"{i + 1}: {song}")

def generate_playlist(mood):
    playlists = {
        "happy": ["Chicago - Micheal Jackson", "There Was This Girl - Riley Green", "The Days - CHRYSTAL & NOTION"],
        "sad": ["Pearls - Sade", "Distant Lover - Marvin Gaye", "Perfect Circle - Mac Miller"],
        "energetic": ["loud room - Lumisoun", "FOREGROUND - Lonown", "My Address Public - NBA YoungBoy"],
        "calm": ["Juna - Clairo", "Over and Over - The Altons", "Not You Too(feat. Chris Brown) - Drake"]
    }
    return playlists.get(mood, ["No playlist available for this mood. Try happy, sad, energetic, or calm."])



if __name__ == "__main__":
    main()