from pathlib import Path
import json, re
root = Path(__file__).resolve().parents[1]
for skill in (root / 'skills').iterdir():
    source = skill / 'SKILL.md'
    text = source.read_text()
    assert text.startswith('---\n') and '\nname:' in text and '\ndescription:' in text
    for doc in skill.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            path = link.split('#')[0]
            if path and '://' not in path:
                assert (doc.parent / path).exists(), (doc, path)
    for template in skill.rglob('*.json'):
        json.loads(template.read_text())
    print(skill.name, 'OK')
