# Regroupement Usage Guide

## Overview

Regroupement is an AI-powered system that helps you achieve technical objectives by analyzing sources and generating implementation plans.

## Installation

```bash
# Clone repository
git clone https://github.com/ADLIB-Mrani/Regroupement.git
cd Regroupement

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### 1. Basic Usage (Without AI)

```python
from regroupement.regroupement import Regroupement

# Initialize
system = Regroupement()

# Execute
result = system.execute(
    objective="Create a data warehouse",
    sources=[
        "https://tutorial.com/datawarehouse",
        "https://youtube.com/watch?v=dw-tutorial"
    ]
)

# The result contains:
# - Generated plan
# - Processed sources
# - Execution status
```

### 2. Using the CLI

```bash
# Basic usage
python cli.py \
  --objective "Build a REST API" \
  --sources https://restfulapi.net

# With AI (requires API key)
export OPENAI_API_KEY=sk-your-key
python cli.py \
  --objective "Create microservices architecture" \
  --sources https://microservices.io \
  --use-ai

# Quiet mode (minimal output)
python cli.py \
  --objective "Setup CI/CD pipeline" \
  --sources https://tutorial.com \
  --quiet
```

### 3. AI-Enhanced Planning

```python
from regroupement.regroupement import Regroupement

# Initialize with AI
system = Regroupement(
    api_key="sk-your-openai-key",  # Or set OPENAI_API_KEY env var
    verbose=True
)

result = system.execute(
    objective="Implement machine learning pipeline",
    sources=[
        "https://scikit-learn.org/stable/tutorial/",
        "https://youtube.com/watch?v=ml-tutorial"
    ]
)

# AI will analyze sources and generate a sophisticated plan
```

## Features

### Source Types Supported

1. **Web Pages**: Any HTTP/HTTPS URL
   - Automatically scraped using BeautifulSoup
   - Content extracted and cleaned

2. **YouTube Videos**: YouTube URLs
   - Transcripts automatically extracted
   - Supports multiple languages (English, French by default)

3. **Text/Markdown**: Direct text or files
   - Can be provided as content directly

### Plan Generation

#### Rule-Based (No AI Required)
- Generates structured 5-phase implementation plan
- Based on best practices and templates
- Always available, no API key needed

#### AI-Powered (With OpenAI)
- Analyzes source content intelligently
- Generates custom plans based on context
- Provides specific recommendations
- Requires OpenAI API key

### Execution Options

#### Dry Run (Default)
```python
result = system.execute(
    objective="...",
    sources=["..."],
    dry_run=True  # Only generates plan
)
```

#### Auto-Execute (Use with Caution)
```python
system = Regroupement(auto_execute=True)
result = system.execute(
    objective="...",
    sources=["..."],
    dry_run=False  # Will attempt to execute
)
```

**Note**: Auto-execution is disabled by default for safety. Plans are generated but not executed automatically.

## Examples

### Example 1: Data Warehouse Project

```python
from regroupement.regroupement import Regroupement

system = Regroupement(verbose=True)

result = system.execute(
    objective="Create a data warehouse for business analytics with ETL pipeline",
    sources=[
        "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/",
        "https://youtube.com/watch?v=dw-design",
        "https://docs.snowflake.com/en/user-guide-getting-started.html"
    ]
)

print(result['plan']['plan'])
```

### Example 2: REST API Development

```python
system = Regroupement(verbose=True)

result = system.execute(
    objective="Build a RESTful API with authentication and rate limiting",
    sources=[
        "https://restfulapi.net/",
        "https://flask-restful.readthedocs.io/",
        "https://youtube.com/watch?v=rest-api-tutorial"
    ]
)
```

### Example 3: With Custom Settings

```python
system = Regroupement(
    api_key="sk-your-key",
    auto_execute=False,  # Safety first
    verbose=True
)

# Add sources incrementally
system.add_sources([
    "https://tutorial1.com",
    "https://youtube.com/watch?v=vid1"
])

system.add_sources([
    "https://tutorial2.com"
])

# Check statistics
stats = system.get_stats()
print(f"Total sources: {stats['sources_count']}")

# Execute
result = system.execute(
    objective="Implement GraphQL API with subscriptions"
)
```

## Advanced Usage

### Processing Sources Separately

```python
system = Regroupement(verbose=False)
system.add_sources(["https://example.com"])

# Process sources
sources_content = system.process_sources()

# Analyze content
for source in sources_content:
    if source['success']:
        print(f"✓ {source['url']}: {len(source.get('content', ''))} chars")
    else:
        print(f"✗ {source['url']}: {source['error']}")

# Generate plan manually
plan = system.generate_plan(
    objective="My objective",
    sources_content=sources_content
)
```

### Custom Source Types

```python
from regroupement.source_manager import SourceManager

manager = SourceManager()

# Add with custom content
manager.add_source(
    url="local://file.txt",
    source_type="text",
    content="My custom content here"
)
```

## Configuration

### Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your-api-key-here
YOUTUBE_API_KEY=your-youtube-key  # Optional
```

### API Key Priority

1. Passed directly to constructor: `Regroupement(api_key="...")`
2. Environment variable: `OPENAI_API_KEY`
3. `.env` file: `OPENAI_API_KEY=...`

## Output Format

### Result Structure

```python
{
    'objective': 'Your objective',
    'sources_processed': 3,
    'plan': {
        'objective': 'Your objective',
        'plan': 'Generated plan text...',
        'method': 'ai' or 'rule-based',
        'sources_count': 3,
        'success': True
    },
    'execution': {
        'executed': False,
        'dry_run': True,
        'message': 'Execution skipped...'
    },
    'success': True
}
```

## Testing

Run the test suite:

```bash
# Run all tests
python -m unittest test_regroupement.py -v

# Run specific test class
python -m unittest test_regroupement.TestSourceManager -v

# Run demo
python demo.py
```

## Troubleshooting

### Issue: Sources not loading
- Check internet connectivity
- Verify URLs are accessible
- Some sites may block automated scraping

### Issue: YouTube transcripts not available
- Not all videos have transcripts
- Try different language codes
- Some videos disable transcript extraction

### Issue: AI not working
- Verify OPENAI_API_KEY is set correctly
- Check API key has credits
- System falls back to rule-based if AI fails

## Best Practices

1. **Start with dry run**: Always test with `dry_run=True` first
2. **Verify sources**: Use accessible, quality sources
3. **Review plans**: Always review generated plans before execution
4. **Use AI wisely**: AI planning requires API credits
5. **Handle errors**: Check `result['success']` and handle failures

## Safety Features

- **Dry run by default**: Plans are not executed automatically
- **Safe mode**: Command execution requires explicit opt-in
- **Content limits**: Source content is truncated to prevent overload
- **Timeout protection**: Network requests have timeout limits
- **Error handling**: Graceful fallback on failures

## Next Steps

1. Review generated plans carefully
2. Adjust and customize as needed
3. Execute steps manually or semi-automatically
4. Iterate and improve based on results

## Support

For issues or questions:
- Check documentation
- Review examples
- Open an issue on GitHub
