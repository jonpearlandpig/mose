# MOSE — Multi-Operator Systems Engine

> The governance layer AI tools forgot to build.

**Built:** November 2025 · **By:** Jon Hartman / Pearl & Pig · Nashville
**Version:** 4.6.0 · **Status:** Production. Running live operations.

---

## What this is

MOSE is an operating system for AI-enabled work.

Not a chatbot. Not a workflow tool. Not a prompt library. An OS.

It governs decisions, tracks rights, protects IP, and routes reasoning
through a 35-role operator mesh — silently, while you just do the work.

Every AI tool gives you output. MOSE gives you:

- **Ownership** — every artifact OCID-stamped with authorship + lineage
- **Governance** — weighted decision framework, two-key protocol
- **Rights protection** — native IP tracking, voice/likeness compliance
- **Drift detection** — catches tone, scope, rights, and timeline drift silently
- **Vertical OS generation** — one schema, infinite domain deployments

One kernel. Infinite vertical operating systems.

---

## Two things in this repo

### 1. The Schema Pack `/schema/`
Machine-readable governance infrastructure.
Validate it. Fork it. Build vertical OSs on it.
Zero external dependencies. Runs on Python 3.7+.

### 2. Pearl OS `/pearl-os/`
A complete Claude Project system prompt that installs MOSE
into Claude as a governance-first enterprise OS.
Built for real operations. Copy it. Paste it. Use it.

---

## Quick start — Schema

```bash
git clone https://github.com/pearlpig/mose-public
cd mose-public/schema
python validate_mose.py mose_instance.json
```

Expected output:
```
✅ system_identity validated
✅ core_principles validated
✅ architecture validated
✅ decision_framework validated
✅ gate_framework validated
✅ rights_layer validated
✅ operator_mesh validated
✅ context_ledger present
✅ os_factory present
✅ drift_engine present
✅ validation_pack present
✅ versioning present
✅ exports present

✅ VALIDATION PASSED
```

---

## Quick start — Pearl OS

1. Open [claude.ai](https://claude.ai)
2. Create a new Project
3. Go to Project Settings → Instructions
4. Paste the full contents of `pearl-os/PEARL_OS_V1_SYSTEM_PROMPT.md` verbatim
5. Type: **"Pearl OS, activate."**

First test:
> "Generate a TELA Tour Master deployment brief for a spring 2027 touring run."

If the output is structured, operator-informed, governed, and ends with
**Outcome → Next Step → Gate** — the system is live.

---

## What makes MOSE different

Every AI governance tool on the market governs data or models.
MOSE governs **decisions and rights**.

That is a different abstraction — and it maps to how organizations
actually function.

| What others do | What MOSE does |
|---|---|
| Track data lineage | Track decision lineage |
| Monitor model outputs | Govern operator reasoning |
| Compliance reporting | Rights-native authorship |
| Workflow automation | Governed execution with rollback |
| Data cataloging | OCID-stamped artifact ownership |

The 35-role operator mesh is not 35 AI agents.
It is a weighted decision framework that silently routes every complex
task through the right domain expertise — strategy, finance, legal,
creative, ops, risk, rights, compliance — before surfacing governed output.

The user doesn't manage this. They don't see it.
They just get a structured, rights-checked answer.

---

## Architecture — 6 Layers

```
┌─────────────────────────────────┐
│  1. Interface Layer             │  Natural language → governed execution
├─────────────────────────────────┤
│  2. Governance Layer            │  Decisions · Weights · Two-Key Protocol
├─────────────────────────────────┤
│  3. Rights Layer                │  OCIDs · IP lineage · Compliance
├─────────────────────────────────┤
│  4. Operator Mesh               │  35-role decision network
├─────────────────────────────────┤
│  5. Context Ledger              │  Full project memory + history
├─────────────────────────────────┤
│  6. OS Factory                  │  Vertical OS generation pipeline
└─────────────────────────────────┘
```

---

## Vertical OS examples built on MOSE

| OS | Domain | Status |
|---|---|---|
| Flightpath COS | Creative IP production | Live |
| TELA OS | Touring + logistics + medical ops | Live |
| Pearl OS | Internal creative/operational studio | Live |
| ECOS | Label + marketing | Live |
| Aperture OS | Public affairs | Live |
| Tobias OS | Finance + diligence | Live |

---

## OCID — Origin Chain ID

Every artifact produced by MOSE gets an OCID:

```
FORMAT: {TYPE}-{PROJECT}-v{VERSION}-{OWNER}-{TIMESTAMP}
EXAMPLE: DOC-CRUSADE-v1.0.0-JH-20260414T000000Z
```

This is the authorship record. Permanent. Versioned. Traceable.
This is what makes MOSE deployable where provenance is not optional.

---

## Decision Weights

```
1 — Advisory      Input only. Cannot approve.
3 — Domain Lead   Owns domain-specific decisions.
5 — Final Auth    Required for money, rights, risk, public output.
```

Two-key protocol required for: legal · rights · finance ·
public communication · strategic direction.

---

## Gate Framework

```
S1  Spark     Purpose · Audience · Tone · Feasibility
B1  Build     Structure · Plan · Viability · Rights mapped
L1  Launch    Readiness · Legal clearance · Ops integrity
E1  Expand    Scalability · Margins · Repeatability
EV1 Evergreen Stability · Compliance renewal · Maintenance
```

Work does not proceed without proofs. No intuition-only decisions.

---

## Repo structure

```
mose-public/
├── README.md
├── LICENSE.md
├── INSTALL.md
│
├── schema/
│   ├── mose_schema.json          ← JSON Schema definition
│   ├── mose_instance.json        ← Canonical MOSE v4.6.0 instance
│   ├── validate_mose.py          ← Validation script (no dependencies)
│   └── vertical_os_template.json ← Build your own vertical OS
│
├── pearl-os/
│   ├── PEARL_OS_V1_SYSTEM_PROMPT.md  ← Install into Claude Project
│   ├── INSTALL.md                     ← 3-step setup guide
│   └── ACTIVATION_TEST.md             ← Verify system is live
│
└── CONTRIBUTING.md               ← Submit vertical OS templates
```

---

## Build on this

**Fork the schema** and build a vertical OS for your domain.
Use `vertical_os_template.json` as your starting point.
Validate with `validate_mose.py` before deploying.

**Extend the operator mesh** by adding domain-specific roles.
Follow the role schema: title · tagline · weight · phase alignment.

**Submit vertical OS templates** via pull request.
Healthcare. Finance. Faith-based production. Gaming. Legal. Education.
If it needs governance, MOSE can run it.

---

## What this is NOT

- Not a SaaS product you pay for (yet)
- Not a framework that requires cloud infrastructure
- Not a prompt template collection
- Not theoretical — this runs live operations

---

## Proof of deployment

MOSE has been running live across:
- Entertainment / creative IP production
- Touring and road operations
- Medical operations
- Marketing and label operations
- Public affairs
- Finance and diligence

Since November 2025. Multi-deployment. Multiple industries.

---

## License

Schema pack (`/schema/`) — Apache 2.0
Pearl OS system prompt (`/pearl-os/`) — CC Attribution 4.0
KB architecture documents — All rights reserved · Pearl & Pig

---

## Contact

Built by **Jon Hartman**
Founder & Architect · Pearl & Pig · Nashville

OCID: `SYS-MOSE-v4.6.0-JH-20251101T000000Z`

---

> *"The OS that runs the work, so you can run the business."*

**Pearl & Pig · Nashville · 2025**
