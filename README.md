# OpenAI-HARPA Orchestrator

Persistent AI agent combining GPT-4o reasoning with HARPA browser automation.

## Features
- Multi-day task persistence
- Browser automation via Playwright
- Natural language task delegation

## Getting Started

### Installation
\`\`\`bash
git clone https://github.com/TrapFrogBubblez/openai-harpa-orchestrator.git
cd openai-harpa-orchestrator
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python -m playwright install
\`\`\`

### Configuration
1. Copy \`.env.example\` to \`.env\`
2. Add your OpenAI API key
3. Update HARPA extension ID in \`config.py\`

### Usage
\`\`\`bash
python orchestrator.py --task "Find return policy for Sony headphones on BestBuy"
\`\`\`

## Examples
See [EXAMPLES.md](EXAMPLES.md) for more use cases

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information
