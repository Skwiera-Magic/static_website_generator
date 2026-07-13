import os

from pathlib import Path
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    with open(from_path) as markdown_file:
        markdown_text = markdown_file.read()

    with open(template_path) as template_file:
        template_text = template_file.read()

    markdown_as_html = markdown_to_html_node(markdown_text).to_html()
    webpage_title = extract_title(markdown_text)

    output_text = template_text.replace("{{ Title }}", webpage_title)
    output_text = output_text.replace("{{ Content }}", markdown_as_html)
    output_text = output_text.replace('href="/', 'href="{basepath}')
    output_text = output_text.replace('src="/', 'src="{basepath}')

    dest_folder = os.path.dirname(dest_path)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    print(f"Generating page: {from_path}\nTo: {dest_path}")
    with open(dest_path, "x") as output_html:
        output_html.write(output_text)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
