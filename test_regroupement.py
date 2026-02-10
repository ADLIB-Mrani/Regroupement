"""
Unit tests for Regroupement system
"""
import unittest
from regroupement.source_manager import SourceManager, Source
from regroupement.scraper import ContentScraper
from regroupement.youtube_processor import YouTubeProcessor
from regroupement.ai_orchestrator import AIOrchestrator
from regroupement.execution_engine import ExecutionEngine
from regroupement.regroupement import Regroupement


class TestSourceManager(unittest.TestCase):
    """Test SourceManager functionality"""
    
    def setUp(self):
        self.manager = SourceManager()
    
    def test_add_source(self):
        """Test adding a single source"""
        source = self.manager.add_source("https://example.com")
        self.assertEqual(len(self.manager), 1)
        self.assertIsInstance(source, Source)
    
    def test_add_multiple_sources(self):
        """Test adding multiple sources"""
        urls = ["https://example.com", "https://youtube.com/watch?v=test"]
        self.manager.add_sources(urls)
        self.assertEqual(len(self.manager), 2)
    
    def test_detect_youtube(self):
        """Test YouTube URL detection"""
        source = self.manager.add_source("https://youtube.com/watch?v=abc123")
        self.assertEqual(source.source_type, 'youtube')
    
    def test_detect_web(self):
        """Test web URL detection"""
        source = self.manager.add_source("https://example.com/tutorial")
        self.assertEqual(source.source_type, 'web')
    
    def test_get_sources_by_type(self):
        """Test filtering sources by type"""
        self.manager.add_source("https://youtube.com/watch?v=test")
        self.manager.add_source("https://example.com")
        
        youtube_sources = self.manager.get_sources_by_type('youtube')
        self.assertEqual(len(youtube_sources), 1)
        self.assertEqual(youtube_sources[0].source_type, 'youtube')


class TestYouTubeProcessor(unittest.TestCase):
    """Test YouTubeProcessor functionality"""
    
    def setUp(self):
        self.processor = YouTubeProcessor()
    
    def test_extract_video_id_standard(self):
        """Test extracting video ID from standard YouTube URL"""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        video_id = self.processor.extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_short(self):
        """Test extracting video ID from short YouTube URL"""
        url = "https://youtu.be/dQw4w9WgXcQ"
        video_id = self.processor.extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_embed(self):
        """Test extracting video ID from embed YouTube URL"""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        video_id = self.processor.extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_invalid(self):
        """Test with invalid URL"""
        url = "https://example.com"
        video_id = self.processor.extract_video_id(url)
        self.assertIsNone(video_id)


class TestAIOrchestrator(unittest.TestCase):
    """Test AIOrchestrator functionality"""
    
    def setUp(self):
        self.orchestrator = AIOrchestrator()
    
    def test_analyze_sources_no_ai(self):
        """Test generating plan without AI"""
        sources_content = [
            {
                'url': 'https://example.com',
                'title': 'Test Tutorial',
                'content': 'This is a test tutorial content',
                'success': True
            }
        ]
        
        objective = "Build a web application"
        plan = self.orchestrator.analyze_sources(sources_content, objective)
        
        self.assertTrue(plan['success'])
        self.assertEqual(plan['method'], 'rule-based')
        self.assertIn('plan', plan)
        self.assertIn(objective, plan['plan'])
    
    def test_summarize_sources(self):
        """Test source summarization"""
        sources_content = [
            {
                'url': 'https://example.com',
                'title': 'Tutorial',
                'content': 'Content here',
                'success': True
            }
        ]
        
        summary = self.orchestrator._summarize_sources(sources_content)
        self.assertIn('Tutorial', summary)
        self.assertIn('Content here', summary)


class TestExecutionEngine(unittest.TestCase):
    """Test ExecutionEngine functionality"""
    
    def setUp(self):
        self.engine = ExecutionEngine()
    
    def test_execute_plan_dry_run(self):
        """Test plan execution in dry run mode"""
        plan = {
            'plan': 'Test plan content',
            'objective': 'Test objective'
        }
        
        result = self.engine.execute_plan(plan, dry_run=True)
        self.assertFalse(result['executed'])
        self.assertTrue(result['dry_run'])
    
    def test_execute_command_safe_mode(self):
        """Test command execution in safe mode"""
        result = self.engine.execute_command('echo test', safe_mode=True)
        self.assertFalse(result['executed'])
        self.assertIn('Safe mode', result['message'])


class TestRegroupement(unittest.TestCase):
    """Test main Regroupement class"""
    
    def setUp(self):
        self.system = Regroupement(verbose=False)
    
    def test_initialization(self):
        """Test system initialization"""
        self.assertIsNotNone(self.system.source_manager)
        self.assertIsNotNone(self.system.scraper)
        self.assertIsNotNone(self.system.youtube_processor)
        self.assertIsNotNone(self.system.ai_orchestrator)
        self.assertIsNotNone(self.system.execution_engine)
    
    def test_add_sources(self):
        """Test adding sources"""
        sources = ["https://example.com", "https://youtube.com/watch?v=test"]
        self.system.add_sources(sources)
        self.assertEqual(len(self.system.source_manager), 2)
    
    def test_get_stats(self):
        """Test getting system statistics"""
        self.system.add_sources(["https://example.com", "https://youtube.com/watch?v=test"])
        stats = self.system.get_stats()
        
        self.assertEqual(stats['sources_count'], 2)
        self.assertIn('sources_by_type', stats)
        self.assertIn('has_ai', stats)


if __name__ == '__main__':
    unittest.main()
