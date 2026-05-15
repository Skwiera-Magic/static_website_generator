from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Delimiters amount is odd while it should be even")
        parts = node.text.split(delimiter)
        for i in range(len(parts)):
            if i % 2 == 1:
                new_node = TextNode(parts[i], text_type)
            else:
                new_node = TextNode(parts[i], TextType.TEXT)
            new_nodes.append(new_node)
    return new_nodes