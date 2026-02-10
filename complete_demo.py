#!/usr/bin/env python3
"""
Complete demonstration of Regroupement system capabilities
Shows all features and use cases
"""
from regroupement.regroupement import Regroupement


def print_section(title):
    """Print a section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def demo_basic_usage():
    """Demonstrate basic usage without AI"""
    print_section("1. BASIC USAGE - Without AI")
    
    system = Regroupement(verbose=True)
    
    result = system.execute(
        objective="Create a data warehouse for business analytics",
        sources=[
            "https://example.com/datawarehouse-guide",
            "https://docs.example.com/analytics"
        ],
        dry_run=True
    )
    
    print(f"\n✓ Status: {'Success' if result['success'] else 'Failed'}")
    print(f"✓ Sources processed: {result['sources_processed']}")
    print(f"✓ Plan method: {result['plan']['method']}")


def demo_source_types():
    """Demonstrate different source types"""
    print_section("2. MULTIPLE SOURCE TYPES")
    
    system = Regroupement(verbose=True)
    
    # Add various source types
    system.add_sources([
        "https://tutorial.example.com/guide",          # Web page
        "https://youtube.com/watch?v=tutorial123",     # YouTube
        "https://example.com/guide.pdf",               # PDF
        "https://github.com/project/README.md",        # Markdown
    ])
    
    # Show statistics
    stats = system.get_stats()
    print("\n📊 SOURCE STATISTICS:")
    print(f"   Total sources: {stats['sources_count']}")
    print(f"   Web pages: {stats['sources_by_type']['web']}")
    print(f"   YouTube videos: {stats['sources_by_type']['youtube']}")
    print(f"   PDFs: {stats['sources_by_type']['pdf']}")
    print(f"   Text files: {stats['sources_by_type']['text']}")


def demo_different_objectives():
    """Demonstrate different types of objectives"""
    print_section("3. DIFFERENT OBJECTIVES")
    
    objectives = [
        ("Data Engineering", "Build an ETL pipeline with Apache Airflow"),
        ("Web Development", "Create a RESTful API with authentication"),
        ("DevOps", "Set up CI/CD pipeline with GitHub Actions"),
        ("Machine Learning", "Implement a recommendation system"),
        ("Cloud Architecture", "Design scalable microservices on AWS")
    ]
    
    for category, objective in objectives:
        print(f"\n📋 {category}:")
        print(f"   Objective: {objective}")
        
        system = Regroupement(verbose=False)
        result = system.execute(
            objective=objective,
            sources=["https://example.com/tutorial"],
            dry_run=True
        )
        
        print(f"   ✓ Plan generated: {result['plan']['success']}")


def demo_step_by_step():
    """Demonstrate step-by-step processing"""
    print_section("4. STEP-BY-STEP PROCESSING")
    
    # Initialize
    print("Step 1: Initialize system")
    system = Regroupement(verbose=False)
    
    # Add sources
    print("Step 2: Add sources")
    system.add_sources([
        "https://fastapi.tiangolo.com/",
        "https://youtube.com/watch?v=api-tutorial"
    ])
    print(f"   Added {len(system.source_manager)} sources")
    
    # Process sources
    print("Step 3: Process sources")
    sources_content = system.process_sources()
    successful = sum(1 for s in sources_content if s.get('success'))
    print(f"   Processed: {len(sources_content)} sources ({successful} successful)")
    
    # Generate plan
    print("Step 4: Generate plan")
    plan = system.generate_plan(
        objective="Build a FastAPI application",
        sources_content=sources_content
    )
    print(f"   Generated plan using {plan['method']} method")
    
    # Display plan excerpt
    print("\nStep 5: Plan excerpt (first 300 chars):")
    print("   " + plan['plan'][:300].replace("\n", "\n   ") + "...")


def demo_configuration():
    """Demonstrate configuration options"""
    print_section("5. CONFIGURATION OPTIONS")
    
    configs = [
        ("Default", {}),
        ("Quiet mode", {"verbose": False}),
        ("With AI (no key)", {"api_key": None}),
    ]
    
    for name, config in configs:
        print(f"\n⚙️  {name}:")
        system = Regroupement(**config)
        stats = system.get_stats()
        print(f"   AI enabled: {stats['has_ai']}")
        print(f"   Auto-execute: {stats['auto_execute']}")


def demo_safety_features():
    """Demonstrate safety features"""
    print_section("6. SAFETY FEATURES")
    
    print("🔒 Safety mechanisms:")
    print("   1. Dry run by default (no auto-execution)")
    print("   2. Safe mode for command execution")
    print("   3. Content length limits (5000 chars for web, 10000 for video)")
    print("   4. Network timeout protection (10 seconds)")
    print("   5. Secure URL hostname validation")
    print("   6. Error handling with graceful fallbacks")
    
    # Demonstrate dry run
    print("\n📋 Dry run example:")
    system = Regroupement(verbose=False)
    result = system.execute(
        objective="Test objective",
        sources=["https://example.com"],
        dry_run=True
    )
    print(f"   Executed: {result['execution']['executed']}")
    print(f"   Message: {result['execution']['message']}")


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 70)
    print("  REGROUPEMENT - COMPLETE DEMONSTRATION")
    print("  AI-Powered Goal Achievement System")
    print("=" * 70)
    
    demos = [
        ("Basic Usage", demo_basic_usage),
        ("Source Types", demo_source_types),
        ("Different Objectives", demo_different_objectives),
        ("Step-by-Step", demo_step_by_step),
        ("Configuration", demo_configuration),
        ("Safety Features", demo_safety_features),
    ]
    
    for name, demo_func in demos:
        try:
            demo_func()
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
    
    print("\n" + "=" * 70)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\n📚 Next steps:")
    print("   1. Try the CLI: python cli.py --help")
    print("   2. Run tests: python -m unittest test_regroupement.py")
    print("   3. Check USAGE.md for detailed documentation")
    print("   4. Configure OpenAI API key for AI-powered planning")
    print("\n✨ Happy building!\n")


if __name__ == '__main__':
    main()
