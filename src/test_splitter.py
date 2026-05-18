import unittest

from text_node import TextNode, TextType
from splitter import split_nodes_link, split_nodes_image

class TestSplitter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_first(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and some trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and some trailing text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_bold(self):
        node = TextNode("to boot dev", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.BOLD)
            ],
            new_nodes,
        )

    def test_split_multiple_nodes(self):
        node1 = TextNode("Visit [boot dev](https://www.boot.dev)", TextType.TEXT)
        node2 = TextNode("No links here", TextType.TEXT)
        new_nodes = split_nodes_link([node1, node2])
        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode("boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode("No links here", TextType.TEXT),
            ],
            new_nodes,
        )