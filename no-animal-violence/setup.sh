#!/usr/bin/env bash
# Set up all No Animal Violence checks for a project
# Run from the project root directory
set -euo pipefail

echo "=== Setting up No Animal Violence language checks ==="

# 1. Pre-commit hook
if [ -f ".pre-commit-config.yaml" ]; then
    echo "Pre-commit config exists. Add the no-animal-violence hook manually."
else
    echo "Creating .pre-commit-config.yaml..."
    cat > .pre-commit-config.yaml << 'YAML'
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: main
    hooks:
      - id: no-animal-violence
        stages: [pre-commit]
YAML
fi

# 2. Install pre-commit if needed
if command -v pre-commit &>/dev/null; then
    pre-commit install
    echo "Pre-commit hooks installed."
else
    echo "pre-commit not found. Install: pip install pre-commit"
fi

# 3. Semgrep rules
echo "Copying Semgrep rules..."
mkdir -p .semgrep
if [ -d "../semgrep-rules-no-animal-violence/rules" ]; then
    cp ../semgrep-rules-no-animal-violence/rules/*.yaml .semgrep/
else
    echo "Semgrep rules not found locally. Clone from:"
    echo "  https://github.com/Open-Paws/semgrep-rules-no-animal-violence"
fi

# 4. ESLint plugin (if JS/TS project)
if [ -f "package.json" ]; then
    echo "Installing ESLint plugin..."
    npm install --save-dev eslint-plugin-no-animal-violence 2>/dev/null || \
        echo "ESLint plugin not published to npm. Install from GitHub."
fi

# 5. Vale (if docs exist)
if find . -name "*.md" -type f | head -1 | grep -q .; then
    if command -v vale &>/dev/null; then
        echo "Setting up Vale..."
        mkdir -p .vale/styles
        cat > .vale.ini << 'INI'
StylesPath = .vale/styles
MinAlertLevel = warning
Packages = https://github.com/Open-Paws/vale-no-animal-violence/releases/latest/download/NoAnimalViolence.zip
[*.md]
BasedOnStyles = NoAnimalViolence
INI
        vale sync
    else
        echo "Vale not found. Install: brew install vale / scoop install vale"
    fi
fi

echo "=== Setup complete ==="
