# Quick Start Guide

Get started with Regroupement in 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/ADLIB-Mrani/Regroupement.git
cd Regroupement

# Install dependencies
pip install -r requirements.txt
```

## Your First Plan

### Option 1: Using the CLI (Easiest)

```bash
python cli.py \
  --objective "Create a REST API with Python" \
  --sources https://fastapi.tiangolo.com
```

### Option 2: Using Python Code

Create a file `my_first_plan.py`:

```python
from regroupement.regroupement import Regroupement

# Initialize the system
system = Regroupement()

# Execute with your objective and sources
result = system.execute(
    objective="Build a data warehouse",
    sources=[
        "https://tutorial.example.com/datawarehouse",
        "https://youtube.com/watch?v=dw-tutorial"
    ]
)

# Print the generated plan
print(result['plan']['plan'])
```

Run it:
```bash
python my_first_plan.py
```

## Next Steps

### 1. Try the Demo
```bash
python complete_demo.py
```

### 2. Run the Tests
```bash
python -m unittest test_regroupement.py -v
```

### 3. Enable AI (Optional)

Get an OpenAI API key from https://platform.openai.com/

```bash
# Set your API key
export OPENAI_API_KEY=sk-your-key-here

# Run with AI enabled
python cli.py \
  --objective "Build microservices architecture" \
  --sources https://microservices.io \
  --use-ai
```

### 4. Learn More

- **Full Documentation**: See [README.md](README.md)
- **Detailed Usage**: See [USAGE.md](USAGE.md)
- **Project Overview**: See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

## Common Use Cases

### Data Warehouse
```bash
python cli.py \
  --objective "Create a data warehouse for analytics" \
  --sources \
    https://www.kimballgroup.com \
    https://youtube.com/watch?v=dw-guide
```

### REST API
```bash
python cli.py \
  --objective "Build a RESTful API with authentication" \
  --sources \
    https://restfulapi.net \
    https://flask-restful.readthedocs.io
```

### CI/CD Pipeline
```bash
python cli.py \
  --objective "Setup CI/CD with GitHub Actions" \
  --sources \
    https://docs.github.com/actions \
    https://youtube.com/watch?v=cicd-tutorial
```

## Tips

- Start without AI (it's free and works great!)
- Use quality sources (official docs, good tutorials)
- Review the generated plan before executing
- The system is safe by default (dry run mode)

## Need Help?

- Check the examples: `python examples.py`
- Run the demo: `python complete_demo.py`
- Read the docs: [README.md](README.md) and [USAGE.md](USAGE.md)
- Run tests to see how it works: `python -m unittest test_regroupement.py -v`

Happy building! 🚀
