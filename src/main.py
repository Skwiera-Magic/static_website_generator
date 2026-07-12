from text_node import TextNode, TextType
from static_to_public_copier import clean_and_copy
from generate_page import generate_page, generate_pages_recursive


def main():
    clean_and_copy("./static", "./public")
    generate_pages_recursive("./content/", "./template.html", "./public/")


if __name__ == "__main__":
    main()
