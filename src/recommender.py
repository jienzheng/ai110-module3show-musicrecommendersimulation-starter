from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's total score and reason list based on user preferences."""
    total = 0.0
    reasons: List[str] = []

    # Helpers to accept multiple possible key names
    user_genre = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    user_mood = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    # energy target may be named 'energy' or 'target_energy'
    target_energy = None
    if "energy" in user_prefs:
        target_energy = user_prefs.get("energy")
    else:
        target_energy = user_prefs.get("target_energy")

    # acoustic preference: either an explicit target or a boolean like likes_acoustic
    target_acoustic = None
    if "target_acousticness" in user_prefs:
        target_acoustic = user_prefs.get("target_acousticness")
    elif user_prefs.get("likes_acoustic"):
        # assume preference for high acousticness
        target_acoustic = 1.0

    # 1) Genre exact match -> +1.5 (experimental: halved genre importance)
    if user_genre and song.get("genre") and user_genre.lower() == song.get("genre").lower():
        pts = 1.5
        total += pts
        reasons.append(f"genre match (+{pts:.2f})")

    # 2) Mood exact match -> +2.0
    if user_mood and song.get("mood") and user_mood.lower() == song.get("mood").lower():
        pts = 2.0
        total += pts
        reasons.append(f"mood match (+{pts:.2f})")

    # 3) Energy closeness -> up to +6.0 (experimental: doubled energy importance)
    if target_energy is not None and song.get("energy") is not None:
        dist = abs(float(song["energy"]) - float(target_energy))
        sim = max(0.0, 1.0 - dist)  # 1.0 for exact match, 0 at distance >=1
        pts = 6.0 * sim
        if pts > 0:
            total += pts
            reasons.append(f"energy closeness (+{pts:.2f})")

    # 4) Acousticness closeness -> up to +2.0, only if user specified an acoustic preference
    if target_acoustic is not None and song.get("acousticness") is not None:
        dist = abs(float(song["acousticness"]) - float(target_acoustic))
        sim = max(0.0, 1.0 - dist)
        pts = 2.0 * sim
        if pts > 0:
            total += pts
            reasons.append(f"acousticness closeness (+{pts:.2f})")

    return total, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by score for the given user preferences."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
