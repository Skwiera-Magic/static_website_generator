import os
import sys

from static_to_public_copier import clean_and_copy
from generate_page import generate_page, generate_pages_recursive


def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    if not os.path.exists("docs"):
        os.makedirs("docs")

    clean_and_copy("./static", "./docs")
    generate_pages_recursive("./content/", "./template.html", "./docs/", basepath)


if __name__ == "__main__":
    main()
