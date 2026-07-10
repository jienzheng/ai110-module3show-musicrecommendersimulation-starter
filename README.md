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
  - Genre, mood tag, valence, energy, acousticness. Genre and mood exist as labels, but scoring leans on the three audio features since not every sad-sounding song is tagged "sad."

- What information does your `UserProfile` store
  - A target feature profile, not a list of favorite artists or genres. It stores ideal values for valence, energy, and acousticness representing the mood the user wants (low valence, low-to-moderate energy, high acousticness).

- How does your `Recommender` compute a score for each song
  - It measures how far each song's feature values are from the target values, then combines those closeness scores with weights. Valence counts most (clearest signal of sadness), energy counts somewhat less, acousticness counts least. A song only scores high by being close on the features that matter most, not just by having one extreme value.

- How do you choose which songs to recommend
  - Score every song first, then sort the full list from highest score to lowest. Scoring and ranking are separate steps: scoring judges one song at a time, ranking looks at the whole list and decides final order (and could add rules later, like limiting songs per artist).

- Real-world recommendations
  - Real-world recommenders like Spotify or YouTube blend collaborative filtering (what similar users listened to) with content-based filtering (a song's own attributes), since each covers the other's blind spots. My version only implements the content-based half — it has no concept of other users, so it can't say "people who liked this also liked that." Instead, it matches a song's audio features (valence, energy, acousticness) against a fixed target mood profile. This avoids the cold-start problem but can't learn from user behavior over time.

- Specific features used by `Song` and `UserProfile` objects
  - **`Song` object features:** `title`, `artist`, `genre`, `mood` (label), `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
  - **`UserProfile` object features:** target `valence` (ideal mood positivity/negativity), target `energy` (ideal intensity level), target `acousticness` (ideal acoustic-vs-produced texture), and a set of feature `weights` (how much each target matters relative to the others when computing a score)

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



