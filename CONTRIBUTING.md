# 🤝 Contributing to AI-Powered HARPA Orchestrator

Thank you for your interest in contributing! This project thrives on community contributions, from bug fixes to new features to documentation improvements.

## 🌟 Ways to Contribute

### 🐛 Bug Reports
- Report issues with detailed reproduction steps
- Include system information and error logs
- Suggest potential solutions if you have ideas

### ✨ Feature Requests  
- Propose new automation capabilities
- Suggest UI/UX improvements
- Request additional AI model integrations

### 💻 Code Contributions
- Bug fixes and performance improvements
- New task types and automation patterns
- Integration with additional services
- Testing and quality assurance

### 📚 Documentation
- Improve setup and usage guides
- Add examples and tutorials
- Translate documentation
- Create video tutorials or blog posts

### 🧪 Testing
- Test on different operating systems
- Validate with various browser configurations
- Performance testing and optimization
- Edge case discovery

---

## 🚀 Getting Started

### Development Environment Setup

**1. Fork & Clone**
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/openai-harpa-orchestrator.git
cd openai-harpa-orchestrator
```

**2. Set Up Development Environment**
```bash
# Create virtual environment
python3 -m venv dev-env
source dev-env/bin/activate  # On Windows: dev-env\Scripts\activate

# Install dependencies + development tools
pip install -r requirements.txt
pip install pytest black flake8 mypy  # Development tools

# Install Playwright browsers
python -m playwright install
```

**3. Configure for Development**
```bash
# Copy environment template
cp .env.example .env

# Add your API keys for testing
# OPENAI_API_KEY=your-key-here
# HARPA_API_KEY=your-key-here
```

**4. Verify Setup**
```bash
# Run health check
python HEALTH_CHECK.py

# Test basic functionality
python orchestrator.py --task "Go to google.com and describe what you see" --debug
```

---

## 🔄 Development Workflow

### Branch Strategy

**Main Branches:**
- `main` - Production-ready code
- `develop` - Integration branch for features

**Feature Branches:**
```bash
# Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Examples:
git checkout -b feature/add-firefox-support
git checkout -b bugfix/fix-timeout-handling  
git checkout -b docs/improve-setup-guide
```

### Making Changes

**1. Code Development**
```bash
# Make your changes
# Edit files as needed

# Test frequently during development
python orchestrator.py --task "test task" --debug
```

**2. Code Quality Checks**
```bash
# Format code
black .

# Check style
flake8 .

# Type checking (if applicable)
mypy orchestrator.py
```

**3. Testing**
```bash
# Run existing tests
pytest tests/ -v

# Test your specific changes
python orchestrator.py --task "specific test for your feature" --debug

# Test edge cases
python orchestrator.py --task "edge case scenario" --debug
```

**4. Documentation Updates**
- Update relevant `.md` files if you changed functionality
- Add docstrings to new functions
- Update examples if you added new capabilities

### Commit Guidelines

**Commit Message Format:**
```bash
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New features
- `fix`: Bug fixes  
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat(harpa): add support for Firefox browser automation"
git commit -m "fix(orchestrator): handle timeout errors gracefully"  
git commit -m "docs(setup): add Windows-specific installation steps"
git commit -m "refactor(integration): simplify API error handling"
```

**Good Commit Practices:**
- Keep commits focused on single changes
- Write clear, descriptive messages
- Include context in commit body for complex changes
- Reference issue numbers when applicable

---

## 🧪 Testing Standards

### Required Testing

**Before Submitting:**
1. **Functionality Test**: Core feature works as expected
2. **Integration Test**: Plays well with existing system
3. **Edge Case Test**: Handles errors and unusual inputs
4. **Performance Test**: Doesn't significantly slow down system

**Testing Commands:**
```bash
# Basic functionality
python orchestrator.py --task "simple test task" --debug

# Error handling
python orchestrator.py --task "intentionally problematic request" --debug

# Performance (time the execution)
time python orchestrator.py --task "standard benchmark task"

# State management
python orchestrator.py --task "multi-step task" --task-id "test_persistence"
```

### Test Categories

**Unit Tests** (if applicable):
```bash
# Test individual functions
pytest tests/test_config.py
pytest tests/test_state_manager.py
```

**Integration Tests**:
```bash
# Test component interactions
python orchestrator.py --task "end-to-end integration test" --debug
```

**Manual Testing Checklist:**
- [ ] Feature works with different task types
- [ ] Error messages are helpful and actionable
- [ ] State persistence works correctly
- [ ] Performance is acceptable
- [ ] Documentation matches implementation
- [ ] Works on different operating systems (if possible)

---

## 📋 Code Standards

### Python Style Guide

**Follow PEP 8 with these specifics:**

**Imports:**
```python
# Standard library imports first
import os
import json
from typing import Dict, List, Optional

# Third-party imports
import requests
from openai import OpenAI
from playwright.sync_api import sync_playwright

# Local imports last
from config import Config
from state_manager import save_state, load_state
```

**Function Documentation:**
```python
def execute_harpa_command(command: str, url: str = None) -> str:
    """
    Execute a command through HARPA's API.
    
    Args:
        command: Natural language command from GPT-4o
        url: Target URL for the action (optional)
    
    Returns:
        String result from HARPA execution
        
    Raises:
        APIError: If HARPA API request fails
        ValueError: If command format is invalid
    """
    # Implementation here
```

**Error Handling:**
```python
def api_call_example():
    """Example of proper error handling."""
    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logger.error("API request timed out")
        raise APITimeoutError("HARPA API request timed out")
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise APIError(f"HARPA API error: {e}")
```

**Configuration Management:**
```python
# Use Config class for all settings
from config import Config

# ✅ Good
api_key = Config.HARPA_API_KEY
timeout = Config.REQUEST_TIMEOUT

# ❌ Avoid hardcoded values
api_key = "hardcoded-key"
timeout = 30
```

### File Organization

**Project Structure:**
```
openai-harpa-orchestrator/
├── orchestrator.py          # Main execution engine
├── config.py               # Configuration management  
├── harpa_integration.py    # HARPA API interface
├── state_manager.py        # Task persistence
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── logging.py         # Logging configuration
│   └── validators.py      # Input validation
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_orchestrator.py
│   └── test_harpa_integration.py
└── docs/                   # Documentation
    ├── SETUP.md
    ├── USAGE.md
    └── API.md
```

---

## 🚀 Submitting Changes

### Pull Request Process

**1. Pre-submission Checklist:**
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Feature is complete and functional
- [ ] No sensitive information (API keys, etc.) in code

**2. Create Pull Request:**
```bash
# Push your feature branch
git push origin feature/your-feature-name

# Go to GitHub and create Pull Request
# Target: develop branch (not main)
```

**3. Pull Request Template:**
```markdown
## Description
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have tested this change locally
- [ ] I have added tests for new functionality
- [ ] All existing tests pass

## Related Issues
Closes #123 (if applicable)

## Screenshots/Logs
Include relevant output or screenshots if applicable.
```

### Review Process

**What Reviewers Look For:**
1. **Functionality**: Does the code work as intended?
2. **Code Quality**: Is it readable, maintainable, and well-structured?
3. **Testing**: Are changes adequately tested?
4. **Documentation**: Is documentation complete and accurate?
5. **Performance**: Does it impact system performance?
6. **Security**: Are there any security implications?

**Review Timeline:**
- Initial review within 48-72 hours
- Follow-up reviews within 24 hours
- Merge after approval and passing CI checks

---

## 🐛 Issue Reporting

### Bug Report Template

**Use this template for bug reports:**

```markdown
## Bug Description
Clear, concise description of the bug.

## To Reproduce
Steps to reproduce the behavior:
1. Run command '...'
2. See error '...'

## Expected Behavior
What you expected to happen.

## Actual Behavior  
What actually happened.

## Environment
- OS: [e.g., Ubuntu 20.04, Windows 11, macOS 12]
- Python version: [e.g., 3.9.7]
- Browser: [e.g., Chrome 96.0.4664.110]
- HARPA version: [e.g., v11.2.1]

## Error Logs
```
Paste full error output here
```

## Additional Context
Any other context about the problem.
```

### Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature.

## Use Case
Explain the problem this feature would solve.

## Proposed Solution
Describe how you envision this feature working.

## Alternatives Considered
Other approaches you've considered.

## Additional Context
Any other context, mockups, or examples.
```

---

## 🏆 Recognition

### Contributors

We recognize contributors in several ways:
- **GitHub Contributors**: Automatic recognition in repository
- **Release Notes**: Major contributors mentioned in releases  
- **Documentation**: Active contributors listed in README
- **Special Roles**: Consistent contributors may be invited as maintainers

### Contribution Types Valued

**Code Contributions:**
- New features and enhancements
- Bug fixes and performance improvements
- Test coverage improvements
- Code refactoring and cleanup

**Non-Code Contributions:**
- Documentation improvements
- Issue triage and user support
- Community building and outreach
- Translation and localization

---

## 🤔 Getting Help

### Before Contributing

**Questions About:**
- **Architecture**: Review existing code and documentation first
- **Features**: Check existing issues for similar requests
- **Bugs**: Search issues to see if already reported
- **Setup**: Follow SETUP.md thoroughly

### Communication Channels

**GitHub Issues**: Best for technical discussions and bug reports
**Discussions**: Use GitHub Discussions for general questions
**Email**: For sensitive issues or private questions

### Mentor Program

**New Contributors:**
- Comment on issues you're interested in working on
- Ask for guidance on implementation approach
- Request code reviews on work-in-progress branches
- Pair with experienced contributors for complex features

---

## 📜 Code of Conduct

### Our Standards

**Positive Behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable Behavior:**
- Harassment of any kind
- Discriminatory language or behavior
- Personal or political attacks
- Publishing others' private information
- Other conduct inappropriate in a professional setting

### Reporting

Report unacceptable behavior to project maintainers. All complaints will be reviewed and investigated promptly and fairly.

---

## 🎯 Roadmap & Priorities

### Current Priorities

**High Priority:**
1. Browser compatibility (Firefox, Safari support)
2. Enhanced error handling and recovery
3. Performance optimizations
4. Comprehensive test suite

**Medium Priority:**
1. Additional AI model integrations
2. Task templating system
3. Batch processing improvements
4. Advanced state management

**Future Goals:**
1. Web-based UI for task management
2. Plugin system for custom integrations
3. Cloud deployment options
4. Enterprise features

### How to Help

**Check Project Board**: See current issues and planned features
**Join Discussions**: Participate in feature planning
**Propose Ideas**: Submit well-researched feature requests
**Implement Features**: Take ownership of roadmap items

---

Thank you for contributing to the AI-Powered HARPA Orchestrator! Together, we're building the future of intelligent browser automation. 🚀

---

## 📚 Additional Resources

- [Setup Guide](SETUP.md) - Complete installation instructions
- [Usage Guide](USAGE.md) - Comprehensive usage documentation  
- [API Documentation](API.md) - Technical API reference
- [Example Tasks](EXAMPLES.md) - Real-world automation examples
- [GitHub Issues](https://github.com/TrapFrogBubblez/openai-harpa-orchestrator/issues) - Current bugs and feature requests