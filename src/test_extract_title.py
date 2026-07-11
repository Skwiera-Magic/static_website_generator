import unittest

from extract_title import extract_title


class TestConverter(unittest.TestCase):
    def test_extract_title(self):
        title = "# Random Title"
        extracted_title = extract_title(title)
        self.assertEqual("Random Title", extracted_title)

    def test_extract_title_spaces(self):
        title = "# Random Title   "
        extracted_title = extract_title(title)
        self.assertEqual("Random Title", extracted_title)

    def test_extract_title_h2(self):
        with self.assertRaises(Exception):
            extract_title("## Random Title")

    def test_extract_title_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("Random Title")