# Regroupement

🤖 **AI-Powered Goal Achievement System**

Regroupement est un système intelligent qui prend des sources (tutoriels, vidéos YouTube, documentation) et un objectif en entrée, puis utilise la puissance de l'IA, du scraping et des APIs pour générer un plan d'implémentation ou l'exécuter directement.

**Regroupement is an intelligent system that takes sources (tutorials, YouTube videos, documentation) and an objective as input, then uses the power of AI, scraping, and APIs to generate an implementation plan or execute it directly.**

## 🌟 Features

- **Multi-Source Support**: Process tutorials, YouTube videos, web pages, and documentation
- **AI-Powered Planning**: Use OpenAI to generate intelligent implementation plans
- **Web Scraping**: Automatically extract content from web sources
- **YouTube Integration**: Extract transcripts from YouTube videos
- **Execution Engine**: Optionally execute generated plans (with safety controls)
- **Flexible Architecture**: Works with or without AI (rule-based fallback)

## 📋 Example Use Case

**Objective**: "Create a data warehouse for business analytics"

**Input Sources**:
- Tutorial: `https://datawarehouse-tutorial.com`
- YouTube: `https://youtube.com/watch?v=dw-setup-guide`
- Documentation: `https://docs.snowflake.com`

**Output**: A detailed step-by-step implementation plan with technologies, timeline, and best practices.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ADLIB-Mrani/Regroupement.git
cd Regroupement

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

#### Command Line Interface

```bash
# Generate a plan (without AI)
python cli.py \
  --objective "Create a data warehouse" \
  --sources https://tutorial.com/dw https://youtube.com/watch?v=xxx

# Use AI for enhanced planning (requires OpenAI API key)
export OPENAI_API_KEY=sk-your-api-key
python cli.py \
  --objective "Build a REST API" \
  --sources https://restfulapi.net \
  --use-ai
```

#### Python API

```python
from regroupement.regroupement import Regroupement

# Initialize the system
system = Regroupement(verbose=True)

# Define your objective and sources
objective = "Create a data warehouse"
sources = [
    "https://tutorial.com/datawarehouse",
    "https://youtube.com/watch?v=dw-guide"
]

# Execute (generates plan)
result = system.execute(
    objective=objective,
    sources=sources,
    dry_run=True  # Only generate plan, don't execute
)

# Access the plan
print(result['plan']['plan'])
```

## 📖 Documentation

### Core Components

1. **SourceManager**: Manages different types of input sources
2. **ContentScraper**: Extracts content from web pages
3. **YouTubeProcessor**: Extracts transcripts from YouTube videos
4. **AIOrchestrator**: Generates plans using AI or rule-based methods
5. **ExecutionEngine**: Executes generated plans (with safety controls)

### Configuration

Create a `.env` file (use `.env.example` as template):

```env
OPENAI_API_KEY=your_api_key_here
```

### API Reference

#### Regroupement Class

```python
Regroupement(
    api_key: Optional[str] = None,      # OpenAI API key
    auto_execute: bool = False,          # Auto-execute plans (use with caution)
    verbose: bool = True                 # Print progress messages
)
```

**Methods**:
- `add_sources(sources: List[str])`: Add sources to process
- `execute(objective: str, sources: List[str], dry_run: bool)`: Main execution method
- `get_stats()`: Get statistics about the current session

## 🎯 Examples

See `examples.py` for complete examples:

```bash
python examples.py
```

### Example 1: Data Warehouse

```python
system = Regroupement(verbose=True)

result = system.execute(
    objective="Create a data warehouse for business analytics",
    sources=[
        "https://www.example.com/datawarehouse-tutorial",
        "https://www.youtube.com/watch?v=example"
    ],
    dry_run=True
)
```

### Example 2: REST API

```python
system = Regroupement(verbose=True)

result = system.execute(
    objective="Build a RESTful API with authentication",
    sources=[
        "https://restfulapi.net/",
        "https://youtube.com/watch?v=rest-api-tutorial"
    ],
    dry_run=True
)
```

## 🔒 Safety Features

- **Dry Run by Default**: Plans are only displayed, not executed
- **Safe Mode**: Command execution is disabled by default
- **Manual Override Required**: Auto-execution requires explicit opt-in

## 🛠️ Development

### Project Structure

```
Regroupement/
├── regroupement/
│   ├── __init__.py
│   ├── regroupement.py          # Main class
│   ├── source_manager.py        # Source management
│   ├── scraper.py              # Web scraping
│   ├── youtube_processor.py     # YouTube processing
│   ├── ai_orchestrator.py      # AI planning
│   └── execution_engine.py     # Execution engine
├── cli.py                       # Command-line interface
├── examples.py                  # Usage examples
├── requirements.txt             # Dependencies
├── .env.example                # Environment template
└── README.md                   # This file
```

### Dependencies

- `requests`: HTTP requests for web scraping
- `beautifulsoup4`: HTML parsing
- `youtube-transcript-api`: YouTube transcript extraction
- `openai`: OpenAI API integration (optional)
- `python-dotenv`: Environment variable management

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Created to help automate learning and implementation of complex technical objectives using AI and web resources.

---

**Note**: This system is designed to assist with planning and learning. Always review generated plans before execution and use appropriate safety measures.
