from text_node import TextNode, TextType
from static_to_public_copier import clean_and_copy


def main():
    clean_and_copy("./static", "./public")


if __name__ == "__main__":
    main()
