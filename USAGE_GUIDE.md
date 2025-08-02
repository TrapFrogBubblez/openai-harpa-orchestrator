# 🎯 Usage Guide - AI-Powered HARPA Orchestrator

Master the art of AI-driven browser automation with natural language commands.

## 🚀 Quick Start

### Basic Task Execution
```bash
python orchestrator.py --task "your task description"
```

### With Custom Task ID
```bash
python orchestrator.py --task "your task description" --task-id "my_custom_task"
```

### Debug Mode (Recommended for First Use)
```bash
python orchestrator.py --task "your task description" --debug
```

---

## 📝 Command Reference

### Core Commands

| Command | Description | Example |
|---------|-------------|---------|
| `--task` | Natural language task description | `--task "Find iPhone prices on Amazon"` |
| `--task-id` | Unique identifier for task persistence | `--task-id "price_research_jan2025"` |
| `--debug` | Enable detailed execution logging | `--debug` |

### Task Management
```bash
# Run a new task
python orchestrator.py --task "Search for Python tutorials"

# Run with specific ID for tracking
python orchestrator.py --task "Research competitor pricing" --task-id "competitor_analysis"

# Resume/Continue existing task (uses saved state)
python orchestrator.py --task "Continue previous research" --task-id "competitor_analysis"
```

---

## 🎨 Task Categories & Examples

### 🔍 Web Search & Research

**Simple Search:**
```bash
python orchestrator.py --task "Search Google for 'machine learning courses'"
```

**Comparative Research:**
```bash
python orchestrator.py --task "Compare features of ChatGPT vs Claude on their official websites"
```

**Academic Research:**
```bash
python orchestrator.py --task "Find recent research papers about renewable energy on Google Scholar"
```

### 🛒 E-commerce & Shopping

**Product Research:**
```bash
python orchestrator.py --task "Find the best-rated wireless headphones under $200 on Amazon"
```

**Price Comparison:**
```bash
python orchestrator.py --task "Compare iPad Air prices on Apple, Amazon, and Best Buy"
```

**Policy Information:**
```bash
python orchestrator.py --task "Find return policy for electronics on Best Buy website"
```

### 📊 Data Collection & Analysis

**Social Media Monitoring:**
```bash
python orchestrator.py --task "Check latest posts about AI automation on Twitter"
```

**Market Research:**
```bash
python orchestrator.py --task "Collect information about top 5 project management tools from their websites"
```

**News Aggregation:**
```bash
python orchestrator.py --task "Find today's top technology news from TechCrunch and Verge"
```

### 🏢 Business & Professional

**Competitor Analysis:**
```bash
python orchestrator.py --task "Analyze pricing pages of top 3 CRM software companies"
```

**Lead Research:**
```bash
python orchestrator.py --task "Find contact information for tech startups in San Francisco"
```

**Job Market Research:**
```bash
python orchestrator.py --task "Search for remote Python developer jobs on LinkedIn and Indeed"
```

---

## 🛠️ Advanced Usage Patterns

### Multi-Step Tasks
The AI automatically breaks down complex tasks:

```bash
python orchestrator.py --task "Research Tesla Model 3: find specifications, pricing, reviews, and nearest dealership"
```

**What happens internally:**
1. Navigate to Tesla website
2. Find Model 3 specifications
3. Check pricing information  
4. Search for reviews on multiple sites
5. Locate nearest dealership
6. Compile comprehensive report

### Task Persistence & Resumption

**Long-running Task:**
```bash
python orchestrator.py --task "Create comprehensive market analysis of electric vehicles" --task-id "ev_market_study"
```

**Resume Later:**
```bash
python orchestrator.py --task "Continue the electric vehicle market analysis" --task-id "ev_market_study"
```

The system automatically:
- Saves progress after each step
- Remembers what was already completed
- Continues from where it left off
- Maintains context across sessions

### Batch Processing

**Multiple Related Tasks:**
```bash
# Task 1: Research
python orchestrator.py --task "Research top 10 AI companies" --task-id "ai_research_part1"

# Task 2: Analysis  
python orchestrator.py --task "Analyze funding rounds for AI companies from previous research" --task-id "ai_research_part2"

# Task 3: Comparison
python orchestrator.py --task "Compare AI companies by revenue and market cap" --task-id "ai_research_part3"
```

---

## 📋 Task Writing Best Practices

### ✅ Effective Task Descriptions

**Be Specific:**
```bash
# ✅ Good
python orchestrator.py --task "Find iPhone 15 Pro pricing on Apple.com, Amazon, and Best Buy"

# ❌ Vague  
python orchestrator.py --task "Look up phone prices"
```

**Include Context:**
```bash
# ✅ Good
python orchestrator.py --task "Search for beginner Python courses on Coursera and Udemy with ratings above 4.5"

# ❌ Generic
python orchestrator.py --task "Find Python courses"
```

**Specify Output Format:**
```bash
# ✅ Good
python orchestrator.py --task "Create a comparison table of top 3 project management tools with pricing and features"

# ❌ Unclear
python orchestrator.py --task "Compare project management tools"
```

### 🎯 Task Complexity Guidelines

**Simple Tasks (1-2 steps):**
- Single website searches
- Basic information lookup
- Simple data extraction

**Medium Tasks (3-5 steps):**
- Multi-site comparisons
- Research with analysis
- Data collection + formatting

**Complex Tasks (5+ steps):**
- Comprehensive market research
- Multi-phase analysis
- Cross-platform data aggregation

---

## 📊 Monitoring & Debugging

### Understanding Output

**Normal Execution:**
```
🤖 AI-Powered HARPA Orchestrator
==================================================
🚀 Starting task: Search for Python tutorials
📋 Task ID: default_task
==================================================

--- Iteration 1 ---
🤖 AI Command: Go to Google and search for "Python tutorials for beginners"
🔄 Executing command through HARPA...
🌐 HARPA Result: Successfully found search results with top Python learning resources
✅ Task marked complete by AI!
🎯 FINAL RESULT: Found comprehensive list of Python tutorials including...
✅ SUCCESS!
```

**Debug Mode Output:**
```bash
python orchestrator.py --task "your task" --debug
```
Shows detailed API calls, response parsing, and state management.

### Common Execution Patterns

**Single Iteration (Simple Task):**
```
Iteration 1: Command → HARPA → Result → Complete
```

**Multiple Iterations (Complex Task):**
```
Iteration 1: Navigate to first site
Iteration 2: Extract data
Iteration 3: Navigate to second site  
Iteration 4: Compare results
Iteration 5: Format final output → Complete
```

---

## 🚨 Error Handling & Recovery

### Automatic Recovery
The system automatically handles:
- Network timeouts → Retry
- Rate limits → Wait and retry
- Partial failures → Continue with alternative approach
- API errors → Fallback strategies

### Manual Intervention

**If Task Stalls:**
```bash
# Check saved state
ls persistent_data/
cat persistent_data/your_task_id_state.json

# Resume with adjusted approach
python orchestrator.py --task "Continue previous task with simpler approach" --task-id "your_task_id"
```

**If Task Fails:**
```bash
# Run with debug to see detailed logs
python orchestrator.py --task "your task" --debug

# Try breaking into smaller tasks
python orchestrator.py --task "Just navigate to website and describe what you see"
```

---

## 📈 Performance Optimization

### Task Efficiency Tips

**Optimize Task Descriptions:**
- Be specific about target websites
- Include expected data formats
- Specify completion criteria

**Use Appropriate Task IDs:**
```bash
# Descriptive IDs for tracking
--task-id "competitor_pricing_jan2025"
--task-id "customer_research_batch1" 
--task-id "market_analysis_phase2"
```

**Monitor Resource Usage:**
- Check API usage in OpenAI dashboard
- Monitor HARPA API limits
- Use appropriate model for task complexity

### Batch Processing Strategies

**Sequential Processing:**
```bash
for company in apple microsoft google; do
    python orchestrator.py --task "Research $company stock performance this quarter" --task-id "${company}_analysis"
done
```

**Parallel Task Design:**
```bash
# Break large tasks into independent parts
python orchestrator.py --task "Research AI companies in healthcare sector" --task-id "ai_healthcare"
python orchestrator.py --task "Research AI companies in finance sector" --task-id "ai_finance"  
python orchestrator.py --task "Research AI companies in retail sector" --task-id "ai_retail"
```

---

## 🔧 Integration Patterns

### Scripting Integration

**Bash Script Example:**
```bash
#!/bin/bash
# research_automation.sh

echo "Starting comprehensive market research..."

python orchestrator.py --task "Research competitor A pricing and features" --task-id "competitor_a"
python orchestrator.py --task "Research competitor B pricing and features" --task-id "competitor_b"
python orchestrator.py --task "Research competitor C pricing and features" --task-id "competitor_c"

echo "Research complete. Check persistent_data/ for results."
```

**Python Script Integration:**
```python
import subprocess
import json

def run_research_task(task_description, task_id):
    result = subprocess.run([
        'python', 'orchestrator.py',
        '--task', task_description,
        '--task-id', task_id
    ], capture_output=True, text=True)
    
    return result.stdout

# Use in larger automation workflows
companies = ['apple', 'microsoft', 'google']
for company in companies:
    result = run_research_task(f"Get latest news about {company}", f"{company}_news")
    # Process results...
```

---

## 📚 State Management

### Understanding Task State

**State File Location:**
```
persistent_data/your_task_id_state.json
```

**State File Contents:**
```json
{
  "task": "Research Tesla Model 3 pricing",
  "progress": [
    {
      "iteration": 1,
      "command": "Navigate to Tesla website",
      "result": "Successfully loaded Tesla homepage"
    },
    {
      "iteration": 2, 
      "command": "Find Model 3 pricing information",
      "result": "Located pricing: $47,740 starting price"
    }
  ],
  "status": "completed",
  "final_result": "Tesla Model 3 starts at $47,740..."
}
```

### State Management Commands

**View Task State:**
```bash
cat persistent_data/my_task_state.json | python -m json.tool
```

**Clean Up Old States:**
```bash
# Remove specific task
rm persistent_data/old_task_state.json

# Clean all completed tasks
find persistent_data/ -name "*_state.json" -exec grep -l '"status": "completed"' {} \; | xargs rm
```

---

## 🎓 Learning & Experimentation

### Start Simple
```bash
# Begin with basic tasks
python orchestrator.py --task "Go to google.com and tell me what you see"
python orchestrator.py --task "Search for 'hello world' on Google"
python orchestrator.py --task "Visit Wikipedia and summarize the main page"
```

### Progress to Complex
```bash
# Gradually increase complexity
python orchestrator.py --task "Compare iPhone vs Samsung phone prices on Amazon and Best Buy"
python orchestrator.py --task "Research the top 5 AI tools for content creation and create a feature comparison"
```

### Experiment with Styles
```bash
# Different approaches to same goal
python orchestrator.py --task "Find Python learning resources" --task-id "approach_1"
python orchestrator.py --task "Create a curated list of the best Python tutorials for beginners with ratings and links" --task-id "approach_2"
```

---

## 💡 Pro Tips

1. **Use descriptive task IDs** for easy tracking and resumption
2. **Start with debug mode** when trying new task types
3. **Break complex tasks** into smaller, testable components  
4. **Monitor API usage** to manage costs effectively
5. **Save successful task patterns** for reuse
6. **Use specific websites** in task descriptions for better results
7. **Include data format preferences** in task descriptions
8. **Test with simple tasks first** before complex automation

---

## 🤝 Getting Help

If tasks aren't working as expected:

1. **Use debug mode** to see detailed execution
2. **Check the troubleshooting section** in SETUP.md
3. **Review task description** for clarity and specificity
4. **Test with simpler versions** of the task first
5. **Check persistent_data/** for saved state information

---

Ready to automate the web with AI? Start with simple tasks and work your way up to complex multi-step automation! 🚀