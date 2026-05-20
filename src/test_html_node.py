import unittest

from html_node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html01(self):
        node = HTMLNode("a", "click me", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html02(self):
        node = HTMLNode("a", "click me", [])
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html03(self):
        node = HTMLNode("a", "click me", [], {})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html04(self):
        node = HTMLNode("a", "click me", [], {"href": "www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html05(self):
        node = HTMLNode("a", "click me", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), ' href="https://www.google.com" target="blank"')


if __name__ == "__main__":
    unittest.main()
