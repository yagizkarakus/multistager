def write_multistage_dockerfile(stages, output_path, runtime_base=None):
    with open(output_path, "w") as f:
        f.write("FROM node:18 AS builder\n")
        for ins in stages["builder"]:
            f.write(f"{ins['instruction']} {ins['value']}\n")
        
        f.write(f"\nFROM {runtime_base or 'node:18-slim'} AS final\n")
        f.write("WORKDIR /app\n")

        for path in stages["artifacts"]:
            f.write(f"COPY --from=builder /app/{path} /app/{path}\n")

        for ins in stages["runtime"]:
            f.write(f"{ins['instruction']} {ins['value']}\n")
