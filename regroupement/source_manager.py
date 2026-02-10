"""
Source Manager - Handles different types of input sources
"""
import re
from typing import List, Dict, Any
from urllib.parse import urlparse


class Source:
    """Represents a source of information"""
    
    def __init__(self, url: str, source_type: str = None, content: str = None):
        self.url = url
        self.source_type = source_type or self._detect_type(url)
        self.content = content
        
    def _detect_type(self, url: str) -> str:
        """Detect the type of source from URL"""
        try:
            parsed = urlparse(url)
            hostname = parsed.hostname or ''
            
            # Check hostname properly to avoid URL injection
            if hostname in ['www.youtube.com', 'youtube.com', 'm.youtube.com'] or hostname == 'youtu.be':
                return 'youtube'
            elif url.endswith('.pdf'):
                return 'pdf'
            elif url.endswith(('.md', '.txt')):
                return 'text'
            elif url.startswith('http'):
                return 'web'
            else:
                return 'unknown'
        except Exception:
            return 'unknown'
    
    def __repr__(self):
        return f"Source(url={self.url}, type={self.source_type})"


class SourceManager:
    """Manages collection of sources"""
    
    def __init__(self):
        self.sources: List[Source] = []
        
    def add_source(self, url: str, source_type: str = None, content: str = None):
        """Add a new source"""
        source = Source(url, source_type, content)
        self.sources.append(source)
        return source
    
    def add_sources(self, urls: List[str]):
        """Add multiple sources"""
        for url in urls:
            self.add_source(url)
    
    def get_sources_by_type(self, source_type: str) -> List[Source]:
        """Get all sources of a specific type"""
        return [s for s in self.sources if s.source_type == source_type]
    
    def get_all_sources(self) -> List[Source]:
        """Get all sources"""
        return self.sources
    
    def __len__(self):
        return len(self.sources)
    
    def __repr__(self):
        return f"SourceManager({len(self.sources)} sources)"
