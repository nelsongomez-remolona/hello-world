# The Daily Brief — Editorial Standard

Purpose: inform and teach, not provoke. Each edition should leave the reader with a better model of how the world works, the way a well-briefed policymaker, central banker, or executive sees it.

## Selection test

A story qualifies only if it plausibly changes a decision someone with real authority must make: a government, central bank, military, regulator, large investor, or multinational. Rank by:

1. **Structural consequence**: does it shift prices, alliances, supply chains, legal precedent, or capabilities over months or years?
2. **Breadth**: how many countries, markets, or people does it touch?
3. **Novelty of information**: is something actually new known, or is it the same story with louder adjectives?

Exclude by default: celebrity and personality drama, crime without systemic implications, outrage cycles, sports, entertainment launches, single-poll horse-race politics, and "could"/"might" speculation without a concrete trigger.

## Format per item

Every item both **updates** (what is new) and **educates** (what you need to know to understand it).

- **What happened** (update): plain, dated. No adjectives a wire service wouldn't use.
- **Background** (educate): 2–4 sentences on how the underlying thing works: the institution, mechanism, history, or term a reader needs to understand the story without prior knowledge. E.g. what IEEPA is and why it matters legally, how a CVE is disclosed and patched, what a central bank's real rate is. Skip only if an earlier edition in the past two weeks explained it, and link that edition.
- **Why it matters**: the mechanism (who is affected, through what channel), not the vibe. When the interpretation is disputed, give the two strongest readings and say who holds each.
- **Confidence**: confirmed by multiple outlets / single source / official claim from an interested party / state media. Say which.
- **Watch**: the next concrete date, decision, or data point that will resolve uncertainty.

## Links

Link the claims inside the text itself: every factual claim, figure, and quote is linked at the point it appears to the source it came from, using the most primary source available (the statement, ruling, report or dataset over coverage of it). No unlinked claims. There is no separate sources list at the end.

## Topic coverage

Rotate the "educate" weight across areas where surveys show people rate staying informed as important but feel least informed (Pew, 2026): economic and tax policy, health systems, foreign policy, the limits of executive power, social insurance, technology regulation. Also cover areas UK audiences report as underserved (Reuters Institute): education, environment, science. Each edition: at least one main item outside security and conflict.

## Edition structure

1. **Overview**: one line per main item.
2. **Main items** (exactly 5): format above. Word budget per item: What happened ~60, Background ~50, Why it matters ~60, then Confidence and Watch on one combined line. Include follow-through: when a previous watchlist item resolves, report how, including when the outcome was uneventful.
3. **Briefly**: up to 4 one- or two-sentence items, for stories that matter but don't need explaining today.
4. **Concept**: one paragraph (~70 words) on an idea decision-makers use (e.g. risk premium, term structure, sovereign immunity), illustrated by today's news.
5. **Watchlist**: a table of dated events in the coming days and weeks, up to 7 rows.
6. **Left out**: one line naming the high-volume stories deliberately skipped.

## Language rules

- No "slams," "shock," "chaos," "historic" unless quoting someone, and attribute the quote.
- Numbers over adjectives. Give the baseline (vs. pre-war, vs. last year, vs. consensus).
- Separate what a party *claims* from what is *verified*.
- Disclose conflicts of interest of the writer (this brief is produced with Claude, made by Anthropic; any Anthropic story is flagged).
- Length target: 7 minutes of reading, i.e. 1,300–1,500 words excluding link URLs. Check with a word count before the fact-check. If over, cut a Briefly item or a main item's Why-it-matters before cutting Background.

## Fact-check (required before sending)

Nothing is sent until a fact-check pass is complete. The check is a separate step from writing, done by a reviewer with fresh context (a subagent that didn't write the draft), because the writer tends to confirm its own claims.

1. **List every checkable claim**: names, numbers, dates, votes, quotes, attributions, and descriptions of status ("pending," "not yet released," "first since").
2. **Check dates first.** Open each linked source and confirm its publication date falls within the coverage window. Search results mix in pages from earlier years; a source with an unclear or older date doesn't count as verification of a current claim.
3. **Verify against the linked page itself**, not a search snippet. Numbers and votes should come from the primary source (central bank release, court summary, official statement) when one exists.
4. **Check that the status is still current.** For anything described as pending, upcoming or unreleased, search whether it has happened since the source was published.
5. **Check for omissions**: something material the source reports that changes the meaning of a story (e.g. a casualty event, a vote split, a narrowed scope).
6. **Decide each claim:**
   - verified → keep
   - wrong → correct it
   - unverifiable → label it in the text (single source / unverified) or cut it
   - if a main item's central claim fails → drop the item
7. **Write a log** to `digest/factchecks/YYYY-MM-DD.md`: claim, status (OK / FIXED / ADDED / LABELLED / NOT VERIFIED), source, note.
8. **Gate.** Send only if no claim is left wrong and every NOT VERIFIED item is minor and labelled. Otherwise commit the edition and log, don't send, and report why.
9. **Corrections.** If a previous edition was wrong, the next edition opens with a correction note.

The email ends with one line: "Fact-checked: N claims checked, X corrected, Y labelled. Log: <link>."

## Source tiers

Prefer, in order: primary documents (central bank statements, court rulings, IEA/IMF reports, official readouts), wire services (Reuters, AP, AFP, Anadolu), specialist outlets (Just Security, CNBC/Bloomberg markets, Kyiv Independent, Al Jazeera for the Middle East), then general press. Flag state media as such.
