"""
AI Orchestrator - Uses AI to analyze sources and generate implementation plans
"""
import os
from typing import List, Dict, Any, Optional


class AIOrchestrator:
    """Orchestrates AI-powered analysis and planning"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.has_ai = bool(self.api_key)
        
    def analyze_sources(self, sources_content: List[Dict[str, Any]], objective: str) -> Dict[str, Any]:
        """Analyze sources and objective to create implementation plan"""
        
        # Prepare summary of sources
        sources_summary = self._summarize_sources(sources_content)
        
        if self.has_ai:
            try:
                plan = self._generate_ai_plan(sources_summary, objective)
            except Exception as e:
                # Fallback to rule-based plan if AI fails
                plan = self._generate_fallback_plan(sources_summary, objective)
        else:
            # Use rule-based approach if no AI available
            plan = self._generate_fallback_plan(sources_summary, objective)
        
        return plan
    
    def _summarize_sources(self, sources_content: List[Dict[str, Any]]) -> str:
        """Create a summary of all sources"""
        summary_parts = []
        
        for idx, source in enumerate(sources_content, 1):
            if source.get('success'):
                content = source.get('content') or source.get('transcript', '')
                title = source.get('title', 'Unknown')
                url = source.get('url', '')
                
                # Take first 500 chars of content
                preview = content[:500] if content else "No content"
                summary_parts.append(f"Source {idx} ({url}):\nTitle: {title}\nPreview: {preview}...\n")
        
        return "\n".join(summary_parts)
    
    def _generate_ai_plan(self, sources_summary: str, objective: str) -> Dict[str, Any]:
        """Generate plan using AI (OpenAI API)"""
        try:
            import openai
            
            client = openai.OpenAI(api_key=self.api_key)
            
            prompt = f"""You are an AI assistant that helps achieve technical objectives.

Given these sources:
{sources_summary}

And this objective:
{objective}

Create a detailed implementation plan with:
1. Step-by-step instructions
2. Technologies/tools needed
3. Estimated timeline
4. Potential challenges
5. Resources to use

Format your response as a structured plan."""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful technical assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            plan_text = response.choices[0].message.content
            
            return {
                'objective': objective,
                'plan': plan_text,
                'method': 'ai',
                'sources_count': len(sources_summary.split('Source ')) - 1,
                'success': True
            }
            
        except Exception as e:
            raise Exception(f"AI plan generation failed: {str(e)}")
    
    def _generate_fallback_plan(self, sources_summary: str, objective: str) -> Dict[str, Any]:
        """Generate a basic plan without AI"""
        
        sources_count = len(sources_summary.split('Source ')) - 1
        
        plan = f"""# Implementation Plan for: {objective}

## Overview
This plan is based on {sources_count} source(s) provided.

## Step-by-Step Implementation

### Phase 1: Research & Planning
1. Review all provided sources thoroughly
2. Identify key concepts and technologies
3. Document requirements and constraints

### Phase 2: Environment Setup
1. Set up development environment
2. Install necessary tools and dependencies
3. Configure project structure

### Phase 3: Implementation
1. Start with basic foundation
2. Implement core features incrementally
3. Test each component as you build

### Phase 4: Testing & Validation
1. Run comprehensive tests
2. Validate against requirements
3. Fix any issues found

### Phase 5: Deployment
1. Prepare deployment configuration
2. Deploy to target environment
3. Monitor and verify functionality

## Resources
The following sources were analyzed:
{sources_summary[:1000]}

## Next Steps
1. Review this plan
2. Gather additional information if needed
3. Begin implementation following the phases above

## Notes
- This is a rule-based plan. For AI-enhanced planning, configure OpenAI API key.
- Adjust timeline based on complexity and resources available.
- Consider security, scalability, and maintainability in implementation.
"""
        
        return {
            'objective': objective,
            'plan': plan,
            'method': 'rule-based',
            'sources_count': sources_count,
            'success': True
        }
