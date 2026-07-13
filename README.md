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
   ```

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

### High-Energy Pop

```text
Profile: High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
========================================================================

1. Sunrise City
   Final Score: 7.76
   Reasons:
   - genre match (+3.00)
   - mood match (+2.00)
   - energy closeness (+2.76)

2. Gym Hero
   Final Score: 5.91
   Reasons:
   - genre match (+3.00)
   - energy closeness (+2.91)

3. Rooftop Lights
   Final Score: 4.58
   Reasons:
   - mood match (+2.00)
   - energy closeness (+2.58)

4. Storm Runner
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

5. Tunnel Pulse
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

========================================================================
```

### Chill Lofi

```text
Profile: Chill Lofi
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}
========================================================================

1. Library Rain
   Final Score: 8.00
   Reasons:
   - genre match (+3.00)
   - mood match (+2.00)
   - energy closeness (+3.00)

2. Midnight Coding
   Final Score: 7.79
   Reasons:
   - genre match (+3.00)
   - mood match (+2.00)
   - energy closeness (+2.79)

3. Focus Flow
   Final Score: 5.85
   Reasons:
   - genre match (+3.00)
   - energy closeness (+2.85)

4. Spacewalk Thoughts
   Final Score: 4.79
   Reasons:
   - mood match (+2.00)
   - energy closeness (+2.79)

5. Midtown Blue
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

========================================================================
```

### Deep Intense Rock

```text
Profile: Deep Intense Rock
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.95}
========================================================================

1. Storm Runner
   Final Score: 7.88
   Reasons:
   - genre match (+3.00)
   - mood match (+2.00)
   - energy closeness (+2.88)

2. Gym Hero
   Final Score: 4.94
   Reasons:
   - mood match (+2.00)
   - energy closeness (+2.94)

3. Iron Horizon
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

4. Rushline Zero
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

5. Tunnel Pulse
   Final Score: 2.88
   Reasons:
   - energy closeness (+2.88)

========================================================================
```

### Adversarial: Sad but Max Energy

```text
Profile: Adversarial: Sad but Max Energy
Preferences: {'genre': 'pop', 'mood': 'sad', 'energy': 0.9}
========================================================================

1. Gym Hero
   Final Score: 5.91
   Reasons:
   - genre match (+3.00)
   - energy closeness (+2.91)

2. Sunrise City
   Final Score: 5.76
   Reasons:
   - genre match (+3.00)
   - energy closeness (+2.76)

3. Storm Runner
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

4. Tunnel Pulse
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

5. Concrete Anthem
   Final Score: 2.97
   Reasons:
   - energy closeness (+2.97)

========================================================================
```

### Adversarial: Hyped but Highly Acoustic

```text
Profile: Adversarial: Hyped but Highly Acoustic
Preferences: {'genre': 'techno', 'mood': 'euphoric', 'energy': 0.95, 'likes_acoustic': True}
========================================================================

1. Tunnel Pulse
   Final Score: 6.02
   Reasons:
   - genre match (+3.00)
   - energy closeness (+2.88)
   - acousticness closeness (+0.14)

2. Neon Rooftop
   Final Score: 5.01
   Reasons:
   - mood match (+2.00)
   - energy closeness (+2.79)
   - acousticness closeness (+0.22)

3. Ruby Steps
   Final Score: 3.18
   Reasons:
   - energy closeness (+2.22)
   - acousticness closeness (+0.96)

4. Rooftop Lights
   Final Score: 3.13
   Reasons:
   - energy closeness (+2.43)
   - acousticness closeness (+0.70)

5. Storm Runner
   Final Score: 3.08
   Reasons:
   - energy closeness (+2.88)
   - acousticness closeness (+0.20)

========================================================================
```

---

## Experiments You Tried

- **Changed the genre weight from 2.0 to 0.5.** With genre weighted low, energy closeness started to dominate almost every profile, and songs from the "wrong" genre but the right energy level (e.g., a rock track showing up in a pop profile) climbed into the top 5. This confirmed genre was doing more work in the original recipe than it looked like on paper — it was often the tie-breaker between songs with similar energy scores.

- **Doubled the energy weight.** High-energy tracks like *Gym Hero* and *Tunnel Pulse* started dominating across unrelated profiles, even ones with completely different genre/mood targets. This is the same pattern that shows up in the "Adversarial: Sad but Max Energy" test above — once one numeric feature is weighted heavily enough, it can override genre and mood matches almost entirely.

- **Added valence to the score (weight 1.5).** In theory this should have helped the sad-mood adversarial case, since valence is the clearest numeric signal for "sad." In practice, because the adversarial profile itself didn't specify a `valence` target (only `mood: 'sad'` as a label with no matching tag in the dataset), the valence term had nothing to compare against and contributed little — the mismatch wasn't caught by the score at all.

- **Tested five different user types** (High-Energy Pop, Chill Lofi, Deep Intense Rock, and two adversarial profiles). Consistent, single-preference profiles (Chill Lofi, Deep Intense Rock) produced results that matched intuition closely. Contradictory profiles (sad + high energy, acoustic + techno-euphoric) produced results that were technically the "best available" but not actually good matches to what a user asking for those terms would expect — the system optimized around the missing signal rather than flagging the contradiction.

---

## Limitations and Risks

- It only works on a tiny catalog (28 songs) — far too small to represent real musical diversity, especially for underrepresented targets like genuinely sad, low-valence tracks.
- It does not understand lyrics, language, or vocal content at all; scoring is based purely on genre/mood tags and three numeric audio features.
- It might over-favor one genre or mood, since genre/mood are all-or-nothing matches (1 or 0) while other features are continuous, so a single strong numeric feature (usually energy) can end up dominating when the label features don't match.
- It has no mechanism to penalize contradictory preferences, so a profile with self-conflicting inputs (e.g., "sad but max energy") won't be flagged as unusual, it'll just quietly recommend whatever scores highest on the features it *can* satisfy.
- It's purely content-based; it has no concept of other users, popularity, or real listening behavior, so it can't improve or personalize over time the way a real commercial recommender would.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

My biggest learning moment came from the two adversarial tests. I expected "Sad but Max Energy" to at least struggle to find a good match, but instead **Gym Hero** and **Sunrise City** — both cheerful, high-energy pop songs — came out on top with respectable scores (5.91 and 5.76), just from genre and energy matching alone. Nothing in the score ever penalized the fact that "sad" mood didn't match anything in the dataset. That's when it really clicked that my scoring recipe is purely additive: it rewards agreement but has no mechanism to punish contradiction. A profile that's internally inconsistent doesn't get flagged as inconsistent, it just quietly ignores the piece it can't satisfy and optimizes around what's left.

AI tools were most useful for the boring-but-error-prone parts: writing the closeness-scoring formula correctly (`max(0, 1 - abs(...))` is an easy off-by-one to get wrong), catching a duplicate `recommend_songs()` call, and debugging the `ModuleNotFoundError` that came from switching between running `python -m src.main` and running the file directly. Where I had to double-check the AI hardest was on anything involving *judgment calls* rather than syntax, like how much weight genre should carry versus mood, or whether "sad" should be inferred from valence or from an explicit tag. The AI could implement whichever choice I made competently, but it couldn't tell me which choice was right for how I actually wanted the system to feel. That was on me to test and decide, which is exactly what the adversarial profiles were for.

What surprised me most is how convincing a simple weighted-sum can feel from the outside. Looking at the Chill Lofi results, "Library Rain" and "Midnight Coding" landing at #1 and #2 genuinely *feels* like the system understands lofi as a mood, when really it's just a handful of numbers being subtracted and compared. There's no understanding happening, just arithmetic dressed up with readable reason strings. That's a little unsettling in a useful way — it made me much more skeptical of how "smart" real commercial recommenders might actually be under the hood, versus how smart they're designed to feel. It also made bias easier to see concretely: in a system this simple, bias isn't some abstract concept, it's literally just "which weight is biggest," and it shows up immediately once you run an adversarial test that exposes it.

If I extended this project, my first move would be adding a mismatch penalty, not just match rewards, since that's the single change that would have fixed both adversarial cases at once. After that, I'd want a real "sad" tag in the dataset instead of approximating it from valence, and some kind of diversity constraint on the ranking step so three near-identical lofi tracks can't all monopolize the top 5.