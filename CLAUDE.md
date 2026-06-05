# arithmetic — project instructions

This repository holds **Class 2 structural readings** of external
mathematical objects through the harmonics framework's minimum alphabet.
It is a federated sibling of `nickjoven/harmonics`; the framework concepts
it references live in **that** repo's substrate, which is the authority on
what they say. Orientation is in `README.md`; the canonical (Class-2-only)
claim index is `MANIFEST.yml`.

This file imports the harmonics working discipline. The short version of
that discipline, and the two rules specific to this repo, follow.

## Knowledge is a cache of the substrate

Treat everything you "know" about a framework concept — the value of a
forced quantity, what `minimum_alphabet.md` claims, which class a reading
sits in — as a **cache entry over the substrate**, not as ground truth. An
entry has a *key* (the named concept), a *resolution* (the granularity you
rely on), and a *freshness* (whether you read it from the substrate this
session or are recalling it). An entry is **stale** when the content moved
since you read it, and **fabricated** when you never read it at all and are
filling in a plausible detail. Both are silent failures: the numbers look
clean and nothing surfaces the gap until someone checks.

The substrate of record for framework concepts is **harmonics**, not this
repo. When you reference `q₃ = q₂² − 1`, the forcing of `Γ₀(6)`, or any
`minimum_alphabet.md` claim, you are reading harmonics' cache; verify
against it, do not vouch for it from memory.

## Verify-before-assert

Before asserting a framework concept at a particular resolution, check it
against the substrate. **Verify when** any of these hold:

1. **Not read this session** — you have not retrieved the concept from the
   substrate in this conversation, or only at a coarser resolution than you
   are about to assert.
2. **Taken on assumption** — the detail comes from inference or memory, not
   from content you read. If you cannot name where it came from, it is an
   assumption.
3. **Load-bearing** — the assertion feeds a note's verdict, a commit, a
   MANIFEST edit, or an answer a reader will rely on.

If you cannot verify a load-bearing detail, **say so** — assert it as
unverified and name the gap rather than presenting a cache guess as fact.
For quantitative claims that are checkable here, the discipline is
stronger: **run the check.** Every study ships a pure-Python script that
prints the numbers its note cites; the note must agree with the script, and
the script must run. A number in prose that the script does not produce is
a fabrication waiting to be caught.

## Classification — and the one line you may not cross

The harmonics Class 1–5 ladder (`harmonics:numerology_inventory.md`):

- **Class 1** — confirmed numerology (no structural basis, or contradicted
  in-repo).
- **Class 2** — noted coincidence / structural correspondence with **no
  claim of derivation**.
- **Class 3** — suspect by association.
- **Class 4** — needs individual audit.
- **Class 5** — explicitly *not* numerology (structural, evidenced).

**Everything in this repo is Class 2 and stays Class 2.** A reading that
claims the framework *derives* its object (proves Collatz, derives π,
selects a CM discriminant) has crossed into a claim this repo does not
back. The correct move when a reading seems to promote is the one recorded
in `harmonics:vocabulary_is_the_work_pattern.md`: **name the object
precisely**, and the over-claim either dissolves or sharpens into a real,
framework-native open question — which you record as open, not as proved.

Concretely: the framework explaining *why* Collatz contracts (the rate
`q₃/q₂²`, the boundary `q < q₂²`) is Class 2 and legitimate. The framework
*proving* Collatz would be a Class 5 claim this repo cannot make — so when
the prose nears it, stop at the mechanism and flag the conjecture as open.

## House style for a study

Each study is a directory with two files: `<name>.md` and `<name>.py`.

- The note opens with a **Status / classification** block: Class 2, what it
  is *not*, and the companion check.
- The note keeps the **weak layer and the strong layer apart** (a generic
  decomposition that "almost anything" satisfies is not evidence; say so).
- The note has a **"What this does and does not show"** section with
  explicit guard rails, and an **Open / could-sharpen** section.
- The check is **pure Python, no numpy, self-contained, deterministic**
  (seed any sampling). It prints every load-bearing number in the note.
- Cross-repo references use `harmonics:<path>` and are **referenced, not
  reproduced**.

## Autosave / commit policy

Commit after each logical unit (a study, an infra file, a passing check).
Commit messages summarize the *why*. Never push without asking. A study is
not done until its check runs clean and the note's numbers match the
check's output.
