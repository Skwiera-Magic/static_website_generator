import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(node, node2)

    def test_not_eq01(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is another text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_not_eq02(self):
        node = TextNode("This is a text node", TextType.ITALIC, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)

    def test_not_eq03(self):
        node = TextNode("This is a text node", TextType.BOLD, "http")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()