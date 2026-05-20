from text_node import TextNode, TextType

print("hello world")


def main():
    textnode = TextNode(
        text="Is this working?",
        text_type=TextType.BOLD,
        url="www.google.com",
    )

    print(textnode)


if __name__ == "__main__":
    main()
