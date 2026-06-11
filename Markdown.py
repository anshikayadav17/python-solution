import markdown

text = """
# Hello
This is Python
"""

html = markdown.markdown(text)

print(html)
