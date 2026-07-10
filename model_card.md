# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  


**Sad Pop**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

**Sad Pop** is designed to surface melancholic, low-energy, acoustic-leaning tracks for users who want music that matches a subdued or reflective mood, rather than music that lifts them out of it.

Prompts:  

- What kind of recommendations does it generate  
-- It prioritizes songs with low valence, low-to-moderate energy, and high acousticness — regardless of whether the song is explicitly tagged "sad" in the metadata. It surfaces the closest available match rather than requiring an exact mood label.
- What assumptions does it make about the user  
-- It assumes the user is actively seeking music that matches (not contrasts with) a low mood — i.e., mood-congruent listening rather than mood-repair listening. This is a real behavioral pattern (people do sometimes want sad music when sad), but it's an assumption, not a guarantee: some users in a low mood want the opposite (upbeat music to shift their state).
- Is this for real users or classroom exploration  
-- This version is a classroom/prototype exploration built on a 10-song toy dataset. The scoring logic is realistic, but the catalog is far too small and narrow to serve real users reliably.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
    - Three audio characteristics: valence (how happy vs. sad a song sounds), energy (how intense or calm it is), and acousticness (how stripped-back vs. produced/electronic it sounds). Genre and mood tags exist in the data too, but this version scores on the audio features rather than the labels, since not every genuinely sad-sounding song is labeled "sad" in the metadata.
- What user preferences are considered  
    - Instead of "similar artist" or "similar genre," the model uses a target profile: low valence, low-to-moderate energy, and high acousticness. Think of it as a description of what a "sad song" typically sounds like, rather than a specific artist or genre to copy.
- How does the model turn those into a score  
    - For each feature, the model checks how far a song's value is from the ideal "sad song" value, closer means a higher score, farther away means a lower score. It's not a simple average of the raw numbers, it's an average of *how close* each number is to the target. Some features count more than others: valence matters most, since it's the clearest signal of sadness, energy matters somewhat less, and acousticness the least of the three. So a song only wins a high score by being close on the feature that matters most, not just by scoring high on the raw numbers.
- What changes did you make from the starter logic  
    - The starter idea would have just ranked songs by "lowest valence." Instead, this version blends three features together with different levels of importance, so a song with genuinely low valence but very high energy (like an angry or aggressive-sounding track) doesn't get mistaken for a genuinely sad, quiet song.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
    - 28 songs, up from the original 10.
- What genres or moods are represented  
    - 25 genres, spanning pop, lofi, rock, ambient, jazz, synthwave, hip-hop, classical, metal, reggae, country, blues, house, techno, drum and bass, folk, r&b, soul, punk, k-pop, afrobeat, flamenco, bossa nova, trance, and indie pop.
    - 24 distinct moods, including happy, chill, intense, melancholic, aggressive, sunny, nostalgic, euphoric, hypnotic, dreamy, defiant, playful, uplifting, passionate, serene, and expansive.
- Did you add or remove data  
    - Added 18 new songs, no removals. The expansion added genre and mood diversity that the original 10-song set lacked entirely (e.g., classical, metal, hip-hop, afrobeat, flamenco weren't represented before).
- Are there parts of musical taste missing in the dataset  
    - Yes — genuinely sad music is still nearly absent. Only one song ("Winter Nocturne," valence 0.28) sits in a truly low-valence range; everything else clusters at moderate-to-high valence. So a "sad song" recommender is still mostly approximating sadness from energy/acousticness rather than finding songs that are actually low-valence. The dataset also has no lyrical or vocal data, no cultural/contextual tags (era, language, popularity), and no user listening history — so collaborative filtering isn't possible with this data at all, only content-based matching.  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
