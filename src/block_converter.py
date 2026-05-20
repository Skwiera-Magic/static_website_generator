def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = []
    for block in blocks:
        block = block.strip()
        if block:
            stripped.append(block)
    return stripped