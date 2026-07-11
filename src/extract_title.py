from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            words = block.split(" ")
            if words[0] == "#":
                return " ".join(words[1:])
    raise Exception("No h1 title found")