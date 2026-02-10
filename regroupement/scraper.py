"""
Content Scraper - Extracts content from web sources
"""
import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any


class ContentScraper:
    """Scrapes content from web pages"""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_url(self, url: str) -> Dict[str, Any]:
        """Scrape content from a URL"""
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            # Get title
            title = soup.title.string if soup.title else "No title"
            
            return {
                'url': url,
                'title': title,
                'content': text[:5000],  # Limit content length
                'success': True,
                'error': None
            }
            
        except Exception as e:
            return {
                'url': url,
                'title': None,
                'content': None,
                'success': False,
                'error': str(e)
            }
    
    def scrape_multiple(self, urls: list) -> list:
        """Scrape content from multiple URLs"""
        results = []
        for url in urls:
            result = self.scrape_url(url)
            results.append(result)
        return results
