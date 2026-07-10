# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
  - Genre, mood tag, valence, energy, and acousticness. These are the core inputs to scoring: genre/mood are exact-label checks, while valence/energy/acousticness are continuous similarity features.

- What information does your `UserProfile` store
  - A mix of labels and target audio values: preferred genre, preferred mood, and ideal values for valence, energy, and acousticness (for sad pop: low valence, low-to-moderate energy, higher acousticness).

- How does your `Recommender` compute a score for each song
  - **Finalized Algorithm Recipe:**  
    `genre_match = 1 if song.genre == user.genre else 0`  
    `mood_match = 1 if song.mood == user.mood else 0`  
    `energy_sim = max(0, 1 - abs(song.energy - user.energy))`  
    `valence_sim = max(0, 1 - abs(song.valence - user.valence))`  
    `acousticness_sim = max(0, 1 - abs(song.acousticness - user.acousticness))`  
    `score = 2.0*genre_match + 1.0*mood_match + 2.0*energy_sim + 1.5*valence_sim + 1.0*acousticness_sim`  
    This keeps genre important, gives mood a smaller bonus, and still lets strong feature similarity outrank a weak label-only match.

- How do you choose which songs to recommend
  - Score every song in the CSV, store `(song, score, explanation)`, sort from highest to lowest score, and return the top `k`. This separates per-song judgment from final ranking.

- Real-world recommendations
  - Real-world systems (Spotify/YouTube) combine collaborative filtering with content features. My version is content-based only: it compares song attributes to a fixed target profile, so it can work without user-history data but cannot learn from crowd behavior or personal listening patterns over time.

- Specific features used by `Song` and `UserProfile` objects
  - **`Song` object features:** `title`, `artist`, `genre`, `mood` (label), `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
  - **`UserProfile` object features:** preferred `genre`, preferred `mood`, target `valence` (ideal mood positivity/negativity), target `energy` (ideal intensity level), and target `acousticness` (ideal acoustic-vs-produced texture)
  - **Potential bias note:** this system may over-prioritize genre labels and miss cross-genre songs that match the mood/audio target; it can also inherit noisy mood/genre tags from the dataset.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


