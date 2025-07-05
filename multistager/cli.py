import typer
from multistager import parser, classifier, generator

app = typer.Typer()

@app.command()  
def convert(
    input: str = typer.Option(..., help="Input Dockerfile path"),
    output: str = typer.Option("Dockerfile.multi", help="Output Dockerfile path"),
    runtime_base: str = typer.Option(None, help="Runtime base image (optional)"),
    artifact_path: str = typer.Option(None, help="Build artifact path hint"),
    debug: bool = typer.Option(False, help="Enable debug output"),
    genarate: bool = typer.Option(True, help="Enable/Disable generate output")
):
    instructions = parser.parse_dockerfile(input)
    stages = classifier.classify(instructions, artifact_path)

    if debug:
        typer.echo("=== Classified stages ===")
        typer.echo(stages)

    

    if genarate:
        generator.write_multistage_dockerfile(stages, output, runtime_base) 
        typer.echo(f"Multistage Dockerfile written to {output}")

def main():
    app()

if __name__ == "__main__":
    main()
