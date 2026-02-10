"""
Example usage of Regroupement system
"""
from regroupement.regroupement import Regroupement


def example_data_warehouse():
    """Example: Creating a data warehouse"""
    print("=" * 60)
    print("EXAMPLE: Data Warehouse Implementation")
    print("=" * 60)
    
    # Initialize system
    system = Regroupement(verbose=True)
    
    # Define objective
    objective = "Create a data warehouse for business analytics"
    
    # Add sources (tutorials, documentation, videos)
    sources = [
        "https://www.example.com/datawarehouse-tutorial",  # Tutorial
        "https://www.youtube.com/watch?v=example",         # YouTube video
        "https://docs.example.com/dw-guide",               # Documentation
    ]
    
    # Execute (dry run - only generates plan, doesn't execute)
    result = system.execute(
        objective=objective,
        sources=sources,
        dry_run=True
    )
    
    print("\n" + "=" * 60)
    print("RESULT SUMMARY")
    print("=" * 60)
    print(f"Success: {result['success']}")
    print(f"Sources processed: {result['sources_processed']}")
    print(f"Plan generated: {result['plan']['success']}")
    

def example_rest_api():
    """Example: Building a REST API"""
    print("\n" + "=" * 60)
    print("EXAMPLE: REST API Implementation")
    print("=" * 60)
    
    system = Regroupement(verbose=True)
    
    objective = "Build a RESTful API with authentication"
    
    sources = [
        "https://restfulapi.net/",
        "https://www.youtube.com/watch?v=example-rest-api",
    ]
    
    result = system.execute(
        objective=objective,
        sources=sources,
        dry_run=True
    )
    
    print(f"\n✓ Plan generated for: {objective}")


def example_minimal():
    """Minimal example"""
    print("\n" + "=" * 60)
    print("EXAMPLE: Minimal Usage")
    print("=" * 60)
    
    # Simple usage
    system = Regroupement(verbose=False)
    
    result = system.execute(
        objective="Setup a Python web application",
        sources=[
            "https://flask.palletsprojects.com/",
            "https://docs.python.org/3/tutorial/"
        ],
        dry_run=True
    )
    
    # Print just the plan
    print("\nGENERATED PLAN:")
    print(result['plan']['plan'])


if __name__ == '__main__':
    # Run examples
    print("\n🚀 Regroupement Examples\n")
    
    try:
        # Example 1: Data Warehouse (main use case from requirements)
        example_data_warehouse()
        
        # Example 2: REST API
        # example_rest_api()
        
        # Example 3: Minimal usage
        # example_minimal()
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
