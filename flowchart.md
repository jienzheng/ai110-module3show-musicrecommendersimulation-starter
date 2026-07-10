```mermaid
flowchart LR
    A[Input: User Preferences\ngenre, mood, target energy/valence/acousticness, k]
    B[Load CSV songs.csv]
    C[Loop through each song]
    D[Score one song\n+2 genre match\n+1 mood match\n+ similarity points]
    E[Store result\n(song, score, reason)]
    F[Sort all scored songs by score desc]
    G[Take Top K]
    H[Output recommendations\nTitle + Score + Explanation]

    A --> C
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
```
