# Contributing

Thank you for your interest in contributing to AI Metro Digital Twin.

## Contribution Guidelines

- Keep the existing folder architecture intact.
- Do not rewrite the project unless a specific issue requires it.
- Preserve the simulation, preprocessing, training, evaluation, and dashboard workflow.
- Keep research outputs reproducible and document any new scenario assumptions.
- Use clear names for scripts, datasets, models, and result files.
- Avoid committing generated cache files, logs, virtual environments, or local IDE settings.

## Development Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For Linux/macOS, activate the environment with:

```bash
source .venv/bin/activate
```

## Code Style

- Follow PEP 8 formatting.
- Organize imports in standard-library, third-party, and local groups.
- Add docstrings to reusable functions.
- Keep comments focused on research assumptions or non-obvious implementation details.
- Do not change model logic or simulation parameters without documenting the reason.

## Pull Request Checklist

- The project still runs with the documented workflow.
- New dependencies are added only when used by project code.
- Generated artifacts are placed in the appropriate `data/`, `results/`, or `trained_models/` folder.
- README or documentation is updated when behavior, scenarios, or commands change.
- Large datasets and temporary files are excluded when they are not required for reproducibility.

## Reporting Issues

When opening an issue, include:

- The command you ran.
- The expected result.
- The actual result or error message.
- Your Python version and SUMO installation path.
- Any relevant dataset or scenario file names.
