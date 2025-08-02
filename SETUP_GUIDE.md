# 🤖 AI-Powered HARPA Orchestrator - Complete Setup Guide

Transform natural language commands into automated browser actions using GPT-4o + HARPA AI.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows 10/11
- **Python**: 3.8+ (recommended: 3.10+)
- **Chrome/Chromium**: Latest version
- **Internet Connection**: Required for API calls

### Required Accounts & API Keys
- **OpenAI Account**: For GPT-4o API access
- **HARPA AI Extension**: Installed in Chrome with API key

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/TrapFrogBubblez/openai-harpa-orchestrator.git
cd openai-harpa-orchestrator
```

### Step 2: Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv myenv

# Activate environment
# On Linux/macOS:
source myenv/bin/activate
# On Windows:
myenv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install
```

### Step 4: Verify Installation
```bash
# Check if all packages are installed correctly
python -c "import openai, playwright, requests, dotenv; print('✅ All packages installed successfully!')"
```

---

## 🔑 API Keys Setup

### Get OpenAI API Key

1. **Visit**: [OpenAI Platform](https://platform.openai.com)
2. **Sign up/Login** to your account
3. **Navigate to**: API Keys section
4. **Create** a new API key
5. **Copy** the key (starts with `sk-`)

### Get HARPA AI API Key

1. **Install HARPA Extension**:
   - Visit Chrome Web Store
   - Search "HARPA AI" 
   - Install extension (ID: `eanggfilgoajaocelnaflolkadkeghjp`)

2. **Access HARPA Interface**:
   - Go to any website
   - Press `Alt+V` (or click HARPA icon in toolbar)
   - HARPA sidebar should appear

3. **Find AUTOMATE Tab**:
   - Look for "AUTOMATE" tab at the top of HARPA interface
   - Click on it

4. **Generate API Key**:
   - Enable "Remote-Control Browser" option
   - Click "CREATE NEW KEY" button
   - Copy the generated API key

### Configure Environment Variables

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** with your real keys:
   ```bash
   OPENAI_API_KEY=sk-your-actual-openai-key-here
   HARPA_API_KEY=your-harpa-api-key-here
   OPENAI_MODEL=gpt-4o
   ```

3. **Verify configuration**:
   ```bash
   python -c "from config import Config; print('✅ OpenAI Key:', Config.OPENAI_API_KEY[:10] + '...'); print('✅ HARPA Key:', Config.HARPA_API_KEY[:10] + '...')"
   ```

---

## 🧪 Testing Your Setup

### Basic Health Check
```bash
python HEALTH_CHECK.py
```
Should output: `System health: OK`

### Test AI Connection
```bash
python orchestrator.py --task "Go to google.com and search for 'hello world'" --debug
```

### Expected Output
```
🤖 AI-Powered HARPA Orchestrator
==================================================
🚀 Starting task: Go to google.com and search for 'hello world'
📋 Task ID: default_task
🔧 Debug mode: ON
==================================================

--- Iteration 1 ---
🤖 AI Command: Go to google.com and search for "hello world"
🔄 Executing command through HARPA...
🌐 HARPA Result: Successfully navigated to google.com and performed search...
✅ Task marked complete by AI!
🎯 FINAL RESULT: Task completed successfully
✅ SUCCESS!
```

---

## 📖 Usage Examples

### Simple Web Search
```bash
python orchestrator.py --task "Search for Python tutorials on Google"
```

### Product Research
```bash
python orchestrator.py --task "Find return policy for Sony headphones on BestBuy"
```

### Information Extraction
```bash
python orchestrator.py --task "Go to Wikipedia and summarize the article about artificial intelligence"
```

### Multi-step Task
```bash
python orchestrator.py --task "Compare prices of iPhone 15 on Amazon and Best Buy" --task-id "price-comparison"
```

---

## ⚙️ Configuration Options

### Model Selection
Edit `.env` to change AI model:
```bash
OPENAI_MODEL=gpt-4o          # Recommended for complex tasks
OPENAI_MODEL=gpt-4o-mini     # Faster, cheaper option
OPENAI_MODEL=gpt-3.5-turbo   # Budget option
```

### Rate Limiting
Modify `config.py` for API usage control:
```python
MAX_REQUESTS_PER_MINUTE = 5  # Adjust based on your plan
MAX_TOKENS = 1000           # Increase for complex tasks
REQUEST_TIMEOUT = 60        # Seconds to wait for responses
```

---

## 🐛 Troubleshooting

### Common Issues

**❌ "ModuleNotFoundError: No module named 'requests'"**
```bash
pip install requests
```

**❌ "Using placeholder API key"**
- Check your `.env` file exists and has real API keys
- Ensure no spaces around the `=` in `.env`

**❌ "HARPA API key invalid"**
- Regenerate API key in HARPA extension
- Make sure "Remote-Control Browser" is enabled

**❌ "Task completes immediately without execution"**
- Update to latest `orchestrator.py` (should be fixed)
- Use `--debug` flag to see detailed execution

**❌ "Alt+V doesn't work"**
- Try clicking HARPA icon directly in Chrome toolbar
- Reinstall HARPA extension if needed
- Check if extension is enabled in `chrome://extensions/`

### Debug Mode
Always use debug mode when troubleshooting:
```bash
python orchestrator.py --task "your task here" --debug
```

### Check System Status
```bash
# Verify Python environment
which python
python --version

# Check installed packages
pip list

# Test individual components
python -c "import openai; print('OpenAI OK')"
python -c "import requests; print('Requests OK')"
python -c "from harpa_integration import execute_harpa; print('HARPA Integration OK')"
```

---

## 📁 Project Structure

```
openai-harpa-orchestrator/
├── orchestrator.py          # Main execution engine
├── config.py               # Configuration management
├── harpa_integration.py    # HARPA API interface
├── state_manager.py        # Task persistence
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── .env                   # Your API keys (create this)
├── HEALTH_CHECK.py        # System verification
├── TASK_PROFILES.py       # Predefined task templates
└── persistent_data/       # Task state storage (auto-created)
```

---

## 🚨 Security Notes

- **Never commit `.env`** file to version control
- **Keep API keys secure** - treat them like passwords
- **Monitor API usage** to avoid unexpected charges
- **Use specific task descriptions** for better results

---

## 🤝 Support & Contributing

### Getting Help
1. **Check this guide first** - most issues are covered here
2. **Use debug mode** to see detailed execution logs
3. **Create GitHub issue** with full error logs and setup details

### Contributing
See `CONTRIBUTING.md` for guidelines on:
- Bug reports
- Feature requests  
- Code contributions
- Testing procedures

---

## 🎯 What's Next?

Once your setup is working:

1. **Explore Examples**: Check `EXAMPLES.md` for advanced use cases
2. **Create Custom Tasks**: Build task profiles in `TASK_PROFILES.py`
3. **Monitor Usage**: Track API calls and costs
4. **Scale Up**: Handle more complex multi-step automation

---

## 📄 License

This project is licensed under the MIT License - see `LICENSE` file for details.

---

**🎉 Congratulations!** Your AI-powered browser automation system is now ready. Start with simple tasks and gradually work up to more complex automation workflows.