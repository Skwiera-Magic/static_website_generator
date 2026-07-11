from text_node import TextNode, TextType
from static_to_public_copier import clean_and_copy
from generate_page import generate_page


def main():
    clean_and_copy("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


if __name__ == "__main__":
    main()
