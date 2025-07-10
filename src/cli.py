import subprocess
import sys


def serve():
    """Run the MkDocs server."""
    additional_args = sys.argv[1:]
    subprocess.run(["mkdocs", "serve", *additional_args])
