# Example Use Cases

## 1. Price Tracking
\`\`\`bash
python orchestrator.py --task "Monitor Amazon PS5 prices daily for 1 week"
\`\`\`

## 2. Research Assistant
\`\`\`bash
python orchestrator.py --task "Find return policies for gaming monitors across retailers"
\`\`\`

## Custom Task Template
\`\`\`python
# orchestrator.py
run_task(
    task_description="Your financial monitoring task",
    task_id="unique_task_name",
    duration="7d"  # Run for 7 days
)
