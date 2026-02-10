"""
YouTube Processor - Extracts content from YouTube videos
"""
import re
from typing import Optional, Dict, Any
from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeProcessor:
    """Processes YouTube videos to extract transcripts and metadata"""
    
    @staticmethod
    def extract_video_id(url: str) -> Optional[str]:
        """Extract video ID from YouTube URL"""
        patterns = [
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})',
            r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})',
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def get_transcript(self, url: str, languages: list = ['en', 'fr']) -> Dict[str, Any]:
        """Get transcript from YouTube video"""
        video_id = self.extract_video_id(url)
        
        if not video_id:
            return {
                'url': url,
                'video_id': None,
                'transcript': None,
                'success': False,
                'error': 'Could not extract video ID'
            }
        
        try:
            # Try to get transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            
            # Combine transcript entries
            full_transcript = ' '.join([entry['text'] for entry in transcript_list])
            
            return {
                'url': url,
                'video_id': video_id,
                'transcript': full_transcript[:10000],  # Limit length
                'success': True,
                'error': None
            }
            
        except Exception as e:
            return {
                'url': url,
                'video_id': video_id,
                'transcript': None,
                'success': False,
                'error': str(e)
            }
    
    def get_multiple_transcripts(self, urls: list) -> list:
        """Get transcripts from multiple YouTube videos"""
        results = []
        for url in urls:
            result = self.get_transcript(url)
            results.append(result)
        return results
