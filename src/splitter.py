from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        content = node.text
        images = extract_markdown_images(content)
        if images == [] or node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        for image in images:
            alt = image[0]
            url = image[1]
            sections = content.split(f"![{alt}]({url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(text = sections[0], text_type = TextType.TEXT))
            new_nodes.append(TextNode(text = alt, text_type = TextType.IMAGE, url = url))
            content = sections[-1]
        if content != "":
            new_nodes.append(TextNode(text = content, text_type = TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        content = node.text
        links = extract_markdown_links(content)
        if links == [] or node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        for link in links:
            text = link[0]
            url = link[1]
            sections = content.split(f"[{text}]({url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(text = sections[0], text_type = TextType.TEXT))
            new_nodes.append(TextNode(text = text, text_type = TextType.LINK, url = url))
            content = sections[-1]
        if content != "":
            new_nodes.append(TextNode(text = content, text_type = TextType.TEXT))
    return new_nodes