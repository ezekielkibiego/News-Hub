import unittest
class Sources:
    """
    Sources class to define sources object
    """

    def __init__(self, id, name, description, url, category, en, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = en
        self.country = country


class NewsSourceTest(unittest.TestCase):
    def setUp(self):
        self.new_sources = Sources(
            'abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', "https://abcnews.go.com", 'general','en', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))

if __name__ == '__main__':
    unittest.main()
