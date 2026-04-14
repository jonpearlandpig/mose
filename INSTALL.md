# MOSE — Installation Guide

**Two installs. Pick one or both.**

---

## Option A — Schema Pack
*For builders, developers, and architects*

### Requirements
- Python 3.7+ (no external dependencies)
- Any OS (Linux, macOS, Windows)

### Install

```bash
git clone https://github.com/pearlpig/mose-public
cd mose-public/schema
```

### Validate

```bash
python validate_mose.py mose_instance.json
```

Expected output:
```
✅ VALIDATION PASSED
```

If you see that — you're running MOSE governance infrastructure.

### Build a vertical OS

```bash
cp vertical_os_template.json my_industry_os.json
# Edit my_industry_os.json for your domain
python validate_mose.py my_industry_os.json
```

---

## Option B — Pearl OS (Claude Project)
*For operators, founders, and creative executives*

### Requirements
- Claude.ai account (free or paid)
- Claude Project access

### Step 1 — Create a Project
1. Go to [claude.ai](https://claude.ai)
2. Click **Projects** in the left sidebar
3. Click **New Project**
4. Name it: `MOSE Pearl OS` or anything you want

### Step 2 — Install the System Prompt
1. Open your new Project
2. Click **Project Settings** (top right)
3. Click **Instructions**
4. Open `pearl-os/PEARL_OS_V1_SYSTEM_PROMPT.md`
5. Copy everything from the divider line down
6. Paste verbatim into the Instructions field
7. Save

### Step 3 — Activate
Type exactly this into the Project chat:

```
Pearl OS, activate.
```

Then run the activation test:

```
Generate a TELA Tour Master deployment brief
for a spring 2027 touring run.
```

If the output is structured, governed, and ends with
**Outcome → Next Step → Gate** — Pearl OS is live.

---

## Optional — Add Knowledge Documents

Pearl OS performs at full capacity when the KB Pack
is uploaded to Project Knowledge.

In your Project Settings → Knowledge, upload:
- KB_01 — MOSE Master Schema v4.6
- KB_02 — Operator Mesh v4.6
- KB_03 — Flightpath COS v4.6
- KB_04 — TELA OS v4.6
- KB_05 — Vertical Proof Library v1.0
- KB_06 — Business Layer v1.0
- KB_07 — Creative OS Examples v1.0
- KB_08 — Behavior Core v1.0
- KB_09 — Unified Instruction Kernel v1.2

The system prompt activates without KB documents.
KB documents extend and deepen every output.

---

## Troubleshooting

**Schema validation fails**
- Check Python version: `python --version` (need 3.7+)
- Verify JSON syntax before validating
- Check that all 13 required sections are present

**Pearl OS not responding correctly**
- Confirm system prompt was pasted in full
- Check it went into Project Instructions, not a regular chat
- Re-type "Pearl OS, activate." and run the test prompt

**Output doesn't end with Outcome → Next Step → Gate**
- The system prompt may be truncated
- Re-paste from the file, not from memory or a copy of a copy

---

## Validation exit codes

```
0 — Passed
1 — Failed
```

CI/CD integration:
```bash
python validate_mose.py your_os.json
if [ $? -eq 0 ]; then
    echo "✅ Governance validated — deploying"
else
    echo "❌ Validation failed — blocked"
    exit 1
fi
```

---

**MOSE v4.6.0 · Pearl & Pig · Nashville · 2025**
