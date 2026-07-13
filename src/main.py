"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from typing import Dict, List, Tuple

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def print_profile_recommendations(
    profile_name: str,
    user_prefs: Dict,
    recommendations: List[Tuple[Dict, float, List[str]]],
) -> None:
    """Print top recommendations for one named user profile."""
    print(f"\nProfile: {profile_name}")
    print(f"Preferences: {user_prefs}")
    print("=" * 72)

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")

    print("\n" + "=" * 72)


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        # Adversarial profile: conflicting mood and very high energy
        "Adversarial: Sad but Max Energy": {"genre": "pop", "mood": "sad", "energy": 0.9},
        # Adversarial profile: acoustic preference fights high-energy dance genres
        "Adversarial: Hyped but Highly Acoustic": {
            "genre": "techno",
            "mood": "euphoric",
            "energy": 0.95,
            "likes_acoustic": True,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_profile_recommendations(profile_name, user_prefs, recommendations)


if __name__ == "__main__":
    main()