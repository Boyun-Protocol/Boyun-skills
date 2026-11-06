# Boyun-skills

First-party agent skills for [Boyun-core](https://github.com/Boyun-Protocol/Boyun-core). These instructions help agents construct sourced worlds and explain recorded financial consequences; they do not run inference or sign transactions by themselves.

| Skill | Purpose |
| --- | --- |
| `boyun-world-grounding` | Build evidence registers, source-or-cause support and reviewable world inputs. |
| `boyun-financial-reports` | Produce structured reports from recorded actor decisions, settlements and coverage. |

## Installation

Copy a folder under `skills/` into your agent's supported skill directory, preserving its `SKILL.md`, references and assets. In Cindy, import the local skill folder through Skills. No specific paid model or connector is required by installation.

Start by reading the selected SKILL.md. Use Boyun-core's CLI/MCP for execution, keep model provenance and cost limits explicit, and inspect replay before presenting conditional outcomes. World grounding comes before inference; reports describe completed evidence and disclose missing paths.

Each skill is self-contained. Shared technical reporting references are bundled with the financial-report skill; blank evidence templates belong to world grounding. Generic third-party presentation/transcript skills and marketing workflows are not redistributed here.

## Checks

```sh
python3 tools/check_skills.py
```

## License

AGPL-3.0-only for first-party Boyun skills. See [NOTICE](NOTICE) for project provenance. Installing a skill does not authorize spending, publishing or wallet operations.
