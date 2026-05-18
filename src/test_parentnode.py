import unittest

from parent_node import ParentNode
from leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nested_parent_nodes(self):
        inner = ParentNode("span", [LeafNode("b", "bold")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span><b>bold</b></span></div>")

    def test_many_children(self):
        node = ParentNode("p", [
            LeafNode("b", "bold"),
            LeafNode(None, "plain"),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(node.to_html(), "<p><b>bold</b>plain<i>italic</i></p>")

    def test_parent_with_props(self):
        node = ParentNode("div", [LeafNode(None, "text")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container">text</div>')

    def test_no_tag_raises(self):
        node = ParentNode(None, [LeafNode(None, "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_raises(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()