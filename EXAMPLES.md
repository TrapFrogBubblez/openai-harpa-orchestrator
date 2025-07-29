Example Use Cases

1. Persistent Market Price Monitoring

Monitor product prices over several days or weeks, tracking fluctuations and alerting on significant changes:

    python orchestrator.py --task "Track daily price changes for Tesla Model 3 on multiple car sales websites for 14 days"

2. Automated Research & Data Extraction

Automatically gather and summarize policies, reviews, or product specs from multiple sources:

    python orchestrator.py --task "Find and summarize return policies for high-end laptops from Amazon, BestBuy, and Newegg"

3. Continuous Forex Tick Data Scraper & Analyzer

Run ongoing data collection and analysis on live Forex tick data, generating insights or trading signals:

    python orchestrator.py --task "Collect and analyze real-time EUR/USD tick data, summarizing volatility trends every hour for 7 days"

4. Multi-step Task Automation with Memory

Perform multi-day tasks with state persistence, enabling complex workflows like multi-page data extraction or iterative web automation:

    python orchestrator.py --task "Scrape weather forecasts daily from multiple websites and compile a weekly trend report"

5. Custom Financial Monitoring & Alerts

Set up personalized monitoring tasks for any financial instrument or market event, allowing you to tailor automation to your trading strategy:

    python orchestrator.py --task "Monitor news headlines and sentiment about USD/JPY currency pair, alert on major changes over 3 days"

Custom Task Template

For programmatic task creation, you can use the following Python snippet inside your own scripts:

    from orchestrator import run_task

    run_task(
    task_description="Your detailed task description here",
    task_id="unique_task_identifier"
    )

This list demonstrates the flexibility and persistence this project offers, setting it apart from typical single-run bots or static scrapers.