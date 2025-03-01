import markdown
import os

def convert_md_to_html(md_file_path):
    # Check if the file exists
    if not os.path.isfile(md_file_path):
        print(f"File not found: {md_file_path}")
        return None

    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Define the HTML file path
    html_file_path = os.path.splitext(md_file_path)[0] + '.html'

    # Save the HTML content to a new file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Converted {md_file_path} to {html_file_path}")
    return html_file_path

if __name__ == "__main__":
    # Example usage
    md_file_path = input("Enter the path to the Markdown file: ")
    convert_md_to_html(md_file_path)
