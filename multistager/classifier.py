import re
from multistager.patterns import DEFAULT_PATTERNS

def classify(instructions, language='nodejs', artifact_hint=None):
    builder = []
    runtime = []
    artifacts = set()

    patterns = DEFAULT_PATTERNS.get(language, {"install": [], "build": [], "artifacts": []})
    artifact_keywords = ['build', 'dist', 'out', 'node_modules', 'public', '.next', '.output', 'static']

    def extract_artifact(value):
        for keyword in artifact_keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', value):
                return keyword
        return None

    for ins in instructions:
        instr = ins.get("instruction", "").upper()
        value = ins.get("value", "")

        if instr == "RUN":
            if any(p.search(value) for p in patterns["install"] + patterns["build"]):
                builder.append(ins)
            else:
                runtime.append(ins)

        elif instr == "COPY":
            matched = False

            if artifact_hint and artifact_hint in value:
                artifacts.add(artifact_hint)
                matched = True
            else:
                for p in patterns["artifacts"]:
                    if p.search(value):
                        artifact = extract_artifact(value)
                        if artifact:
                            artifacts.add(artifact)
                            matched = True
                        break

            if matched:
                runtime.append(ins)
            else:
                builder.append(ins)

        elif instr in {"CMD", "ENTRYPOINT"}:
            artifact = extract_artifact(value)
            if artifact:
                artifacts.add(artifact)
            runtime.append(ins)

        else:
            runtime.append(ins)

    if not artifacts and artifact_hint:
        artifacts.add(artifact_hint)

    return {
        "builder": builder,
        "runtime": runtime,
        "artifacts": sorted(set(a.strip('/').lower() for a in artifacts))
    }
