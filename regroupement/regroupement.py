"""
Main Regroupement class - The core system that orchestrates everything
"""
import os
from typing import List, Dict, Any, Optional
from .source_manager import SourceManager, Source
from .scraper import ContentScraper
from .youtube_processor import YouTubeProcessor
from .ai_orchestrator import AIOrchestrator
from .execution_engine import ExecutionEngine


class Regroupement:
    """
    Main class for the AI-powered goal achievement system.
    
    Accepts sources (tutorials, YouTube videos, documentation) and an objective,
    then uses AI, scraping, and APIs to either generate a plan or execute it directly.
    """
    
    def __init__(self, 
                 api_key: Optional[str] = None,
                 auto_execute: bool = False,
                 verbose: bool = True):
        """
        Initialize Regroupement system.
        
        Args:
            api_key: OpenAI API key for AI features (optional)
            auto_execute: Whether to auto-execute plans (default: False for safety)
            verbose: Whether to print progress messages
        """
        self.source_manager = SourceManager()
        self.scraper = ContentScraper()
        self.youtube_processor = YouTubeProcessor()
        self.ai_orchestrator = AIOrchestrator(api_key)
        self.execution_engine = ExecutionEngine(auto_execute=auto_execute)
        self.verbose = verbose
        
    def add_sources(self, sources: List[str]):
        """Add sources (URLs, file paths, etc.)"""
        self.source_manager.add_sources(sources)
        if self.verbose:
            print(f"✓ Added {len(sources)} source(s)")
    
    def process_sources(self) -> List[Dict[str, Any]]:
        """Process all sources to extract content"""
        results = []
        sources = self.source_manager.get_all_sources()
        
        if self.verbose:
            print(f"\n📥 Processing {len(sources)} source(s)...")
        
        for idx, source in enumerate(sources, 1):
            if self.verbose:
                print(f"  [{idx}/{len(sources)}] Processing {source.source_type}: {source.url}")
            
            if source.source_type == 'youtube':
                result = self.youtube_processor.get_transcript(source.url)
            elif source.source_type in ['web', 'unknown']:
                result = self.scraper.scrape_url(source.url)
            else:
                result = {
                    'url': source.url,
                    'content': source.content or 'Content not available',
                    'success': bool(source.content)
                }
            
            results.append(result)
            
            if self.verbose:
                status = "✓" if result.get('success') else "✗"
                print(f"    {status} {'Success' if result.get('success') else 'Failed: ' + str(result.get('error', 'Unknown error'))}")
        
        return results
    
    def generate_plan(self, objective: str, sources_content: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate implementation plan based on sources and objective"""
        if self.verbose:
            print(f"\n🤖 Generating plan for: {objective}")
            print(f"   Using {self.ai_orchestrator.has_ai and 'AI' or 'rule-based'} method...")
        
        plan = self.ai_orchestrator.analyze_sources(sources_content, objective)
        
        if self.verbose and plan.get('success'):
            print(f"✓ Plan generated successfully")
        
        return plan
    
    def execute(self, 
                objective: str,
                sources: Optional[List[str]] = None,
                dry_run: bool = True) -> Dict[str, Any]:
        """
        Main execution method.
        
        Args:
            objective: The goal to achieve
            sources: List of source URLs (optional if already added)
            dry_run: If True, only generate plan without executing (default: True)
        
        Returns:
            Dictionary with plan and execution results
        """
        # Add sources if provided
        if sources:
            self.add_sources(sources)
        
        # Process sources to extract content
        sources_content = self.process_sources()
        
        # Generate plan
        plan = self.generate_plan(objective, sources_content)
        
        # Execute or display plan
        if self.verbose:
            print(f"\n{'='*60}")
            print("IMPLEMENTATION PLAN")
            print('='*60)
            print(plan.get('plan', 'No plan generated'))
            print('='*60)
        
        # Execute plan (if not dry run)
        execution_result = self.execution_engine.execute_plan(plan, dry_run=dry_run)
        
        return {
            'objective': objective,
            'sources_processed': len(sources_content),
            'plan': plan,
            'execution': execution_result,
            'success': True
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the current session"""
        return {
            'sources_count': len(self.source_manager),
            'sources_by_type': {
                'youtube': len(self.source_manager.get_sources_by_type('youtube')),
                'web': len(self.source_manager.get_sources_by_type('web')),
                'pdf': len(self.source_manager.get_sources_by_type('pdf')),
                'text': len(self.source_manager.get_sources_by_type('text')),
            },
            'has_ai': self.ai_orchestrator.has_ai,
            'auto_execute': self.execution_engine.auto_execute
        }
