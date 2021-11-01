import unittest
from app.models import Sources


class NewsSourceTest(unittest.TestCase):
    def setUp(self):
        self.new_sources = Sources(
            'abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', "https://abcnews.go.com", 'general', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))

