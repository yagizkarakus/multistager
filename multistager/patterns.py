import re

DEFAULT_PATTERNS = {
    "nodejs": {
        "install": [
            # NPM
            re.compile(r'\bnpm\s+install\b', re.I),
            re.compile(r'\bnpm\s+ci\b', re.I),
            re.compile(r'\bnpm\s+install\s+--legacy-peer-deps\b', re.I),
            re.compile(r'\bnpm\s+install\s+--production\b', re.I),
            re.compile(r'\bnpm\s+install\s+-g\s+\S+', re.I),
            re.compile(r'\bnpm\s+install\s+--omit=dev\b', re.I),
            # Yarn
            re.compile(r'\byarn\s+install\b', re.I),
            re.compile(r'\byarn\s+add\s+\S+', re.I),
            re.compile(r'\byarn\s+global\s+add\s+\S+', re.I),
            re.compile(r'\byarn\s+install\s+--frozen-lockfile\b', re.I),
            re.compile(r'\byarn\s+workspaces\s+run\s+install\b', re.I),
            # PNPM
            re.compile(r'\bpnpm\s+install\b', re.I),
            re.compile(r'\bpnpm\s+add\s+\S+', re.I),
            re.compile(r'\bpnpm\s+install\s+-g\s+\S+', re.I),
            re.compile(r'\bpnpm\s+install\s+--frozen-lockfile\b', re.I),
            re.compile(r'\bpnpm\s+install\s+--filter\b', re.I),
            # Lock files
            re.compile(r'\bcopy\s+(package(-lock)?\.json|yarn\.lock|pnpm-lock\.yaml)', re.I),
        ],
        "build": [
            re.compile(r'\bnpm\s+run\s+build\b', re.I),
            re.compile(r'\bnpm\s+run\s+build\s+\S+', re.I),
            re.compile(r'\byarn\s+(build|run\s+build)\b', re.I),
            re.compile(r'\byarn\s+run\s+build\b', re.I),
            re.compile(r'\bpnpm\s+run\s+build\b', re.I),
            re.compile(r'\bpnpm\s+run\s+build\s+\S+', re.I),
            re.compile(r'\bturbo\s+run\s+build\b', re.I),
            re.compile(r'\bwebpack\b', re.I),
            re.compile(r'\brollup\b', re.I),
        ],
        "artifacts": [
            re.compile(r'\bdist\b', re.I),
            re.compile(r'\bbuild\b', re.I),
            re.compile(r'\bout\b', re.I),
            re.compile(r'\bnode_modules\b', re.I),
            re.compile(r'packages/.+/dist', re.I),
            re.compile(r'packages/.+/build', re.I),
            re.compile(r'apps/.+/build', re.I),
            re.compile(r'\bpublic\b', re.I),
            re.compile(r'\b\.next\b', re.I),
            re.compile(r'\b\.output\b', re.I),
            re.compile(r'\bstatic\b', re.I),
        ]
    },

    "python": {
        "install": [
            re.compile(r'\bpip\s+install\b', re.I),
            re.compile(r'\bpip3\s+install\b', re.I),
            re.compile(r'\bpip\s+install\s+-r\s+\S+', re.I),
            re.compile(r'\bpip3\s+install\s+-r\s+\S+', re.I),
            re.compile(r'\bpip\s+install\s+\S+', re.I),
            re.compile(r'\bpython\s+-m\s+pip\s+install\b', re.I),
            re.compile(r'\bconda\s+install\b', re.I),
            re.compile(r'\bpoetry\s+install\b', re.I),
            re.compile(r'\bpoetry\s+add\s+\S+', re.I),
            re.compile(r'\bpoetry\s+update\b', re.I),
            re.compile(r'\bpipenv\s+install\b', re.I),
            re.compile(r'\bpipenv\s+install\s+--dev\b', re.I),
            re.compile(r'\bpython\s+setup\.py\s+install\b', re.I),
            re.compile(r'\bcopy\s+(requirements\.txt|Pipfile|Pipfile\.lock|pyproject\.toml)\b', re.I),
        ],
        "build": [
            re.compile(r'\bpython\s+setup\.py\s+build\b', re.I),
            re.compile(r'\bpython3\s+setup\.py\s+build\b', re.I),
            re.compile(r'\bpoetry\s+build\b', re.I),
            re.compile(r'\bpython\s+-m\s+build\b', re.I),
            re.compile(r'\bflit\s+build\b', re.I),
            re.compile(r'\bpyproject-build\b', re.I),
        ],
        "artifacts": [
            re.compile(r'\bdist\b', re.I),
            re.compile(r'\bbuild\b', re.I),
            re.compile(r'\bsite-packages\b', re.I),
            re.compile(r'\b__pycache__\b', re.I),
        ]
    }
}
