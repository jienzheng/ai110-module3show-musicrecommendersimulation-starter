"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "melancholic",
    "target_energy": 0.30,
    "target_valence": 0.25,
    "target_acousticness": 0.85,
    "weights": {
        "genre": 0.20,
        "mood": 0.15,
        "valence": 0.35,
        "energy": 0.20,
        "acousticness": 0.10
    }
}
    
    recommendations = recommend_songs(user_prefs, songs, k=5)
    recommendations = recommend_songs(user_prefs, songs, k=5)
    
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
