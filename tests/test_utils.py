import unittest
import hashlib
from src.utils import calculate_hash, clean_content

class TestUtils(unittest.TestCase):

    def test_calculate_hash(self):
        """calculate_hashのテスト"""
        content = 'Test Content'
        expected_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        content_hash = calculate_hash(content)
        self.assertEqual(content_hash, expected_hash)

    def test_clean_content(self):
        """clean_contentのテスト"""
        content_with_article = '<html><body><article>Test Content</article></body></html>'
        expected_cleaned_content = 'Test Content'
        cleaned_content = clean_content(content_with_article)
        self.assertEqual(cleaned_content, expected_cleaned_content)

        content_without_article = '<html><body>No Article Content</body></html>'
        cleaned_content_no_article = clean_content(content_without_article)
        self.assertEqual(cleaned_content_no_article, content_without_article)

if __name__ == '__main__':
    unittest.main()
