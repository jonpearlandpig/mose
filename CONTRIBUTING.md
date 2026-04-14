# Contributing to MOSE

MOSE is open infrastructure. Build on it.

The most valuable contributions are **vertical OS templates** —
domain-specific governance systems built on the MOSE schema.
Every industry that runs on AI needs one. Most don't have one yet.

---

## What to contribute

### Vertical OS Templates *(highest value)*

A vertical OS is a governed operating system for a specific domain,
built by inheriting from MOSE Master Schema v4.6.

Examples the community needs:
- `healthcare_os.json` — HIPAA, patient data, clinical workflows
- `legal_os.json` — case management, privilege, compliance
- `education_os.json` — curriculum, student data, accreditation
- `realestate_os.json` — transaction governance, disclosure, compliance
- `gaming_os.json` — IP protection, player data, content governance
- `nonprofit_os.json` — donor data, grant compliance, program governance
- `construction_os.json` — safety, permitting, contractor management
- `agriculture_os.json` — supply chain, certification, traceability
- `media_os.json` — rights clearance, distribution, syndication
- `startup_os.json` — decision tracking, investor governance, IP filing

If your domain isn't listed, build it anyway.

### Bug reports and validation issues

Found a case where the validator passes something it shouldn't?
Open an issue with the JSON that triggered it.

### Documentation improvements

Clearer explanations. Better examples. More languages.
All welcome.

---

## How to build a vertical OS

### Step 1 — Copy the template

```bash
cp schema/vertical_os_template.json my_domain_os.json
```

### Step 2 — Define your identity

```json
{
  "vertical_os_identity": {
    "name": "HealthcareOS",
    "domain": "Healthcare / Clinical Operations",
    "version": "1.0.0",
    "description": "Governance OS for clinical workflows with HIPAA compliance",
    "author": "Your Name",
    "ocid": "SYS-HEALTHOS-v1.0.0-YOURNAME-TIMESTAMP"
  }
}
```

### Step 3 — Customize gates for your domain

Add industry-specific validation gates that your domain requires.
Keep all five core MOSE gates (S1, B1, L1, E1, EV1).
Extend with domain gates as needed.

```json
{
  "industry_specific_gates": [
    {
      "name": "HIPAA Compliance Gate",
      "code": "HC1",
      "validates": [
        "phi_handling_policy",
        "breach_notification_plan",
        "baa_executed",
        "access_controls_documented"
      ]
    }
  ]
}
```

### Step 4 — Add domain operators

Add roles specific to your industry. Keep the core MOSE
role schema (title, tagline, description, focus_areas,
traits, invoke_pattern, decision_weight, phase_alignment).

```json
{
  "custom_operators": [
    {
      "title": "HIPAA Compliance Officer",
      "tagline": "PHI protection and breach prevention",
      "decision_weight": 5,
      "phase_alignment": ["all"]
    }
  ]
}
```

### Step 5 — Validate

```bash
python schema/validate_mose.py my_domain_os.json
```

Must pass before submitting.

### Step 6 — Submit a pull request

---

## Pull request requirements

Before opening a PR, confirm:

- [ ] Validation passes: `python validate_mose.py your_os.json`
- [ ] OCID included in the file with your authorship
- [ ] All 5 core gates present (S1, B1, L1, E1, EV1)
- [ ] At least 35 operators defined (or `total_roles` field set)
- [ ] Domain-specific compliance requirements documented
- [ ] README section in the file explains the vertical context
- [ ] No KB document content reproduced (proprietary)

### PR title format

```
feat: [domain] vertical OS — [brief description]
```

Examples:
```
feat: healthcare vertical OS — HIPAA clinical workflows
feat: legal vertical OS — case management and privilege
feat: gaming vertical OS — IP protection and content governance
```

---

## OCID for your contributions

Every vertical OS you submit should include an OCID
that records your authorship permanently.

Format:
```
SYS-{YOUROS}-v{VERSION}-{YOURHANDLE}-{TIMESTAMP}
```

Example:
```
SYS-HEALTHOS-v1.0.0-DRSMITH-20260414T120000Z
```

This is your authorship record. It lives in the file
and in the git history. It's yours.

---

## What we don't accept

- KB document reproductions or derivatives
- System prompts that claim to be Pearl OS v1 without attribution
- Vertical OSs that override or contradict MOSE core principles
- Anything that removes OCID or rights tracking from the architecture

---

## Community standards

This is governance infrastructure. Keep it serious.

- Be precise. Vague governance is not governance.
- Be honest about compliance requirements.
- Credit your sources and your domain expertise.
- If you're not sure a compliance claim is accurate, flag it.

---

## Questions

Open an issue. Tag it `question`.

---

**MOSE v4.6.0 · Pearl & Pig · Nashville · 2025**
**Built by Jon Hartman. Extended by the community.**
