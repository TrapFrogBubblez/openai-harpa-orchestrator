# Recursive Time Agent

A persistent AI agent combining GPT-4o reasoning with HARPA browser automation for multi-day task execution.

## Features
- Persistent task management across multiple days
- Browser automation powered by Playwright
- Natural language task delegation to streamline workflows

## Getting Started

### Installation

```bash
git clone https://github.com/TrapFrogBubblez/openai-harpa-orchestrator.git
cd openai-harpa-orchestrator
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python -m playwright install

Configuration

    Copy .env.example to .env

    Add your OpenAI API key to .env

    Update HARPA extension ID in config.py as needed

Usage

python orchestrator.py --task "Find return policy for Sony headphones on BestBuy"

Examples

See EXAMPLES.md for detailed use cases and sample tasks.
Contributing

Please see CONTRIBUTING.md for guidelines on how to contribute to this project.
License

This project is licensed under the MIT License — see the LICENSE file for details.