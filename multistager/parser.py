def parse_dockerfile(path: str) -> list[dict]:
    instructions = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            instructions.append({
                "instruction": parts[0].upper(),
                "value": parts[1] if len(parts) > 1 else ""
            })
    return instructions
