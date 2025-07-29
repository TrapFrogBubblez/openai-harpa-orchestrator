Setup Guide for Recursive Time Agent

Follow these steps to get the Recursive Time Agent up and running on your system:
1. Clone the Repository

git clone https://github.com/TrapFrogBubblez/openai-harpa-orchestrator.git

    cd openai-harpa-orchestrator

2. Create a Virtual Environment

Create an isolated Python environment to manage dependencies:

    python3 -m venv myenv

3. Activate the Virtual Environment

On Linux/macOS:

    source myenv/bin/activate

On Windows (PowerShell):

    .\myenv\Scripts\Activate.ps1

4. Install Required Dependencies:

    pip install -r requirements.txt

5. Install Browser Engines for Playwright:

    python -m playwright install

Once complete, you are ready to configure your environment variables and start using the Recursive Time Agent.