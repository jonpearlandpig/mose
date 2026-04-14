# Pearl OS — Activation Test

Run this after installing the system prompt to confirm Pearl OS is live.

---

## Step 1 — Activate

Type exactly this into your Claude Project chat:

```
Pearl OS, activate.
```

Expected: A structured response confirming Pearl OS is active,
referencing MOSE Master Schema v4.6 and the operator mesh.

---

## Step 2 — Run the TELA test

Type:

```
Generate a TELA Tour Master deployment brief
for a spring 2027 touring run.
```

**Pass criteria:**
- Output is structured and scannable
- References operational governance (gates, compliance)
- Ends with: Outcome → Next Step → Gate

If it ends with Outcome → Next Step → Gate — Pearl OS is live.

---

## Step 3 — Run the Flightpath test

Type:

```
I have a new creative IP concept. Five-act
immersive experience. Faith-based. Arena scale.
What do I need to do first?
```

**Pass criteria:**
- Routes to Flightpath COS
- Identifies phase (Spark)
- Asks for or infers anchors (purpose, audience, tone)
- Ends with: Outcome → Next Step → Gate

---

## Step 4 — Run the rights test

Type:

```
I want to release a song that was co-written
with AI assistance. What do I need?
```

**Pass criteria:**
- Flags rights ambiguity
- References OCID requirement
- Invokes Carmen + Telauthorium (may be silent)
- Provides structured forward path
- Does NOT just answer casually

---

## Step 5 — Run the governance test

Type:

```
Should I take a $500K investment offer
from a new partner I met last week?
```

**Pass criteria:**
- Invokes two-key protocol (financial decision)
- Requests missing context before advising
- Structures as a Decision Object
- Does NOT give a casual yes/no
- Ends with: Outcome → Next Step → Gate

---

## All five pass?

Pearl OS is fully operational.

If any test fails, check:
1. System prompt was pasted in full (not truncated)
2. It went into Project **Instructions**, not a chat message
3. KB documents are uploaded to Project **Knowledge** if available

---

## Quick single-line test

If you just want a fast check:

```
Pearl OS status.
```

A live system will respond with current active mandate,
priority gate, and next step — not a generic AI response.

---

**MOSE: Pearl OS v1 · Pearl & Pig · Nashville · 2025**
**OCID:** `SYS-PEARLOS-v1.0.0-JH-20251101T000000Z`
