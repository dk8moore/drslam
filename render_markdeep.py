import os

# Template for wrapping Markdeep HTML output
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rendered Markdown</title>
    <script src="https://casual-effects.com/markdeep/latest/markdeep.min.js?" charset="utf-8"></script>
</head>
<body>
    <div class="markdeep">
        {}
    </div>
    <script>window.markdeep.format();</script>
</body>
</html>'''

def render_markdeep(md_file, output_file):
    # Read the content of the Markdown file
    with open(md_file, 'r') as f:
        markdown_content = f.read()

    # Insert markdown content into the HTML template
    rendered_html = html_template.format(markdown_content)

    # Write the rendered HTML to an output file
    with open(output_file, 'w') as f:
        f.write(rendered_html)

    print(f"Markdown rendered and saved to {output_file}")

# Example usage
md_file_path = 'articles/example.md'  # Path to your markdown file
output_html_path = 'articles/example.html'  # Output HTML file path

render_markdeep(md_file_path, output_html_path)
