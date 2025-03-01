from flask import Flask, request, send_file
import os
import markdown
from md_to_html import convert_md_to_html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.md'):
            md_file_path = os.path.join(os.getcwd(), file.filename)
            file.save(md_file_path)
            html_file_path = convert_md_to_html(md_file_path)
            if html_file_path:
                return send_file(html_file_path, as_attachment=True)

    return '''
    <!doctype html>
    <title>Markdown to HTML Converter</title>
    <h1>Upload a Markdown file</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".md">
        <input type="submit" value="Convert to HTML">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
