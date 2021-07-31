from codewars.scraper import Scraper
import unittest

class TestScraper(unittest.TestCase):

    def setUp(self):
        """Executes before EACH test"""
        self.scraper = Scraper()

    def tearDown(self):
        """Executes after EACH test"""
        del self.scraper

    def test_ScrapeHREF(self):
        data = self.scraper.hrefs(
            url='https://codewars.nl/discord/luffy'
            )

        self.assertEqual(
            type(data),
            list,
            "The webpage does not return a 200 response code"
        )
        self.assertEqual(
            len(data),
            1,
            "The webpage did not returned bytes"
        )