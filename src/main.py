"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from .recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv")

    # Default profile (pop / happy) — verifies the recommender against
    # an obvious, easy-to-check case
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 72)

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")

    print("\n" + "=" * 72)


if __name__ == "__main__":
    main()