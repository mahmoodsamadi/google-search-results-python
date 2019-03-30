import random
import unittest
import os
from lib.google_search_results import GoogleSearchResults

class TestSearchApi(unittest.TestCase):

    def setUp(self):
        GoogleSearchResults.SERP_API_KEY = os.getenv("API_KEY", "demo")

    @unittest.skipIf((os.getenv("API_KEY", "demo") == "demo"), "no api_key provided")
    def test_get_json(self):
        gsr = GoogleSearchResults({"q": "Coffee", "location": "Austin,Texas"})
        results = gsr.get_json()
        self.assertIsNotNone(results["local_results"][0]["title"])

if __name__ == '__main__':
    unittest.main()