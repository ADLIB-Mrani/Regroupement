#!/usr/bin/env python3
"""
Command-line interface for Regroupement
"""
import sys
import argparse
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from regroupement.regroupement import Regroupement


def main():
    parser = argparse.ArgumentParser(
        description='Regroupement - AI-powered goal achievement system',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate plan for creating a data warehouse
  python cli.py --objective "Create a data warehouse" --sources https://tutorial.com/dw https://youtube.com/watch?v=xxx
  
  # Use with AI (requires OPENAI_API_KEY environment variable)
  export OPENAI_API_KEY=sk-...
  python cli.py --objective "Build a REST API" --sources https://tutorial.com --use-ai
  
  # Execute plan (use with caution)
  python cli.py --objective "Setup Python project" --sources https://guide.com --execute
        """
    )
    
    parser.add_argument(
        '--objective',
        required=True,
        help='The objective or goal to achieve'
    )
    
    parser.add_argument(
        '--sources',
        nargs='+',
        required=True,
        help='List of source URLs (tutorials, YouTube videos, documentation)'
    )
    
    parser.add_argument(
        '--use-ai',
        action='store_true',
        help='Use AI for enhanced planning (requires OPENAI_API_KEY)'
    )
    
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute the plan automatically (disabled by default for safety)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )
    
    parser.add_argument(
        '--api-key',
        help='OpenAI API key (alternatively use OPENAI_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Get API key from args or environment
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    
    if args.use_ai and not api_key:
        print("⚠ Warning: --use-ai specified but no API key provided.")
        print("   Set OPENAI_API_KEY environment variable or use --api-key")
        print("   Falling back to rule-based planning.\n")
    
    # Initialize Regroupement
    system = Regroupement(
        api_key=api_key if args.use_ai else None,
        auto_execute=args.execute,
        verbose=not args.quiet
    )
    
    # Execute
    try:
        result = system.execute(
            objective=args.objective,
            sources=args.sources,
            dry_run=not args.execute
        )
        
        if not args.quiet:
            print("\n✅ Success!")
            print(f"   Objective: {result['objective']}")
            print(f"   Sources processed: {result['sources_processed']}")
            
            if args.execute:
                print(f"   Execution: {'Completed' if result['execution']['executed'] else 'Skipped'}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
