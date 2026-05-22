from split_nodes_delimiter import split_nodes_delimiter
from splitter import split_nodes_image, split_nodes_link
from text_node import TextNode, TextType


def text_to_textnodes(text):
    old_node = TextNode(text=text, text_type=TextType.TEXT)
    nodes = split_nodes_delimiter([old_node], text_type=TextType.BOLD, delimiter="**")
    nodes = split_nodes_delimiter(nodes, text_type=TextType.ITALIC, delimiter="_")
    nodes = split_nodes_delimiter(nodes, text_type=TextType.CODE, delimiter="`")
    nodes = split_nodes_link(old_nodes=nodes)
    nodes = split_nodes_image(old_nodes=nodes)
    return nodes
