import unittest

from text_converter import text_to_textnodes
from text_node import TextNode, TextType


class TestConverter(unittest.TestCase):
    def test_text_to_textnodes(self):
        result = text_to_textnodes("hello **world** and `code` and ![image](https://i.imgur.com/3elNhQu.png) and [link](https://boot.dev)")
        self.assertListEqual(result, [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
