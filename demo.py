"""
Demo script with realistic example
"""
from regroupement.regroupement import Regroupement


def demo_real_sources():
    """Demo with real, accessible sources"""
    print("=" * 70)
    print("REGROUPEMENT DEMO - Real World Example")
    print("=" * 70)
    print()
    
    # Initialize system
    system = Regroupement(verbose=True)
    
    # Define a realistic objective
    objective = "Learn Python web development and create a simple web application"
    
    # Use real, accessible sources
    sources = [
        "https://www.python.org/about/",  # Python official site
        "https://docs.python.org/3/tutorial/",  # Python tutorial
    ]
    
    print(f"🎯 Objective: {objective}")
    print(f"📚 Sources: {len(sources)} URLs")
    print()
    
    # Execute the system
    result = system.execute(
        objective=objective,
        sources=sources,
        dry_run=True
    )
    
    # Display statistics
    print("\n" + "=" * 70)
    print("SESSION STATISTICS")
    print("=" * 70)
    stats = system.get_stats()
    print(f"Total sources: {stats['sources_count']}")
    print(f"Web sources: {stats['sources_by_type']['web']}")
    print(f"YouTube sources: {stats['sources_by_type']['youtube']}")
    print(f"AI enabled: {stats['has_ai']}")
    print(f"Plan generation: {'AI' if stats['has_ai'] else 'Rule-based'}")
    print()
    
    print("✅ Demo completed successfully!")
    print()
    print("To use AI-powered planning:")
    print("  1. Get an OpenAI API key from https://platform.openai.com/")
    print("  2. Set environment variable: export OPENAI_API_KEY=sk-...")
    print("  3. Re-run with AI enabled")
    print()


if __name__ == '__main__':
    try:
        demo_real_sources()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
