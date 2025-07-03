def classify(instructions, artifact_hint=None):
    builder = []
    runtime = []
    artifacts = []

    for ins in instructions:
        if ins["instruction"] == "RUN" and "install" in ins["value"]:
            builder.append(ins)
        elif ins["instruction"] == "COPY" and artifact_hint and artifact_hint in ins["value"]:
            artifacts.append(artifact_hint)
        else:
            runtime.append(ins)

    return {
        "builder": builder,
        "runtime": runtime,
        "artifacts": artifacts or [artifact_hint] if artifact_hint else []
    }
