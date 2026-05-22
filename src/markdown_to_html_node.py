from markdown_to_blocks import markdown_to_blocks
from text_converter import text_to_textnodes
from text_node import text_node_to_html_node, TextNode, TextType
from block_to_block_type import block_to_block_type, BlockType
from html_node import HTMLNode
from leaf_node import LeafNode
from parent_node import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        lines = block.split("\n")
        tag = ""
        value = ""
        
        if block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            tag = f"h{level}"
            value = block[level + 1:]
        elif block_type == BlockType.PARAGRAPH:
            tag = "p"
            value = " ".join(lines)
        elif block_type == BlockType.CODE:
            code_node = ParentNode("code", [text_node_to_html_node(TextNode(block[4:-3], TextType.TEXT))])
            pre_node = ParentNode("pre", [code_node])
            nodes.append(pre_node)
            continue
        elif block_type == BlockType.QUOTE:
            tag = "blockquote"
            cleaned_lines = [line.strip("> ") for line in lines]
            value = " ".join(cleaned_lines)
        elif block_type == BlockType.UNORDERED_LIST:
            li_list = []
            for line in lines:
                line = line[2:]
                inline_children = text_to_children(line)
                li_list.append(ParentNode("li", inline_children))
            nodes.append(ParentNode("ul", li_list))
            continue
        elif block_type == BlockType.ORDERED_LIST:
            li_list = []
            for i, line in enumerate(lines):
                prefix = f"{i + 1}. "
                line = line[len(prefix):]
                inline_children = text_to_children(line)
                li_list.append(ParentNode("li", inline_children))
            nodes.append(ParentNode("ol", li_list))
            continue
        nodes.append(ParentNode(tag, text_to_children(value)))
    return ParentNode("div", nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children