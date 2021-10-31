import unittest
from models import sources
Sources=sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(123,'Python Must Be Crazy','A thrilling new Python Series','https://abcnews.go.com','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))


if __name__ == '_main_':
    unittest.main()


