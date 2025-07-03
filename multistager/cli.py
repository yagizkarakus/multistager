import typer
from multistager import parser, classifier, generator

app = typer.Typer()

@app.command()  # <=== THIS IS CRUCIAL
def convert(
    input: str = typer.Option(..., help="Input Dockerfile path"),
    output: str = typer.Option("Dockerfile.multi", help="Output Dockerfile path"),
    runtime_base: str = typer.Option(None, help="Runtime base image (optional)"),
    artifact_path: str = typer.Option(None, help="Build artifact path hint")
):
    instructions = parser.parse_dockerfile(input)
    stages = classifier.classify(instructions, artifact_path)
    generator.write_multistage_dockerfile(stages, output, runtime_base)
    print(f"Multistage Dockerfile written to {output}")

def main():
    app()

if __name__ == "__main__":
    main()
