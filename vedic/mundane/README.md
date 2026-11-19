# Mundane astrology log

A running record of world news set against the transits of the day, in both the tropical and the sidereal (Lahiri) zodiac. The aim is a dataset that can eventually be scored, not a collection of good stories.

## Layout

| Path | Contents |
|---|---|
| `entries/YYYY-MM-DD.md` | One snapshot per session: the sky, the news, the matches, classical text checks, and the dated calls made that day |
| `matches.csv` | One row per news-to-transit match, with a strength rating. Used to tally how often the matches are strong, weak or misses. |
| `forecasts.csv` | Every dated call, written before the event. Status stays `open` until scored. |
| `tools/sky.py` | Prints the positions for any date: `python3 tools/sky.py 2026-11-19` |

## Rules

1. **Write the sky before reading the news** where possible, so the sky can't be picked to fit the stories.
2. **Log misses.** Wherever the standard rule points the wrong way (for example, gold falling while Jupiter is strong in Leo), record it as a miss rather than leaving it out.
3. **Rate every match:**
   - `strong`: the classical meaning and the timing both fit, and the event isn't routine.
   - `moderate`: the meaning fits, but the timing is loose or the event is common.
   - `weak`: plausible symbolism only.
   - `miss`: the standard reading points the other way.
4. **Note the base rate.** War, storms and shipwrecks happen almost every week, so matches on them count for little.
5. **Make forecasts specific and dated**, with a scoring condition someone else could check. Score them once the window closes; never edit an `open` call after the fact.
6. **Cite the classical source** when a call rests on a text (for example, Brihat Samhita 17.13). The texts are in `../texts/`.

## Method notes

- Positions come from the DE421 ephemeris via skyfield. The sidereal positions use a linear Lahiri approximation, accurate to about 0.01°.
- The nodes are mean nodes. The South Node (Ketu) is the point opposite the North Node (Rahu).
- **Planetary war (graha yuddha):** two planets within about 1°. The brighter one wins (Brihat Samhita 17.9–12).
