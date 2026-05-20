from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    head_count = 0
    for char in markdown:
        if char == "#":
            head_count += 1
        else:
            break

    lines = markdown.split("\n")
    quote_lines = 0
    quote = False

    unordered_list_lines = 0
    unordered_list = False

    ordered_list_lines = 0
    ordered_list = False

    for line in lines:
        if line.startswith(">"):
            quote_lines += 1
        if line.startswith("- "):
            unordered_list_lines += 1
        if line.startswith(f"{ordered_list_lines + 1}. "):
            ordered_list_lines += 1
    if quote_lines == len(lines):
        quote = True
    if unordered_list_lines == len(lines):
        unordered_list = True
    if ordered_list_lines == len(lines):
        ordered_list = True

    if 1 <= head_count <= 6 and len(markdown) > head_count and markdown[head_count] == " ":
        return BlockType.HEADING
    elif markdown.startswith("```\n") and markdown.endswith("\n```"):
        return BlockType.CODE
    elif quote is True:
        return BlockType.QUOTE
    elif unordered_list is True:
        return BlockType.UNORDERED_LIST
    elif ordered_list is True:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
