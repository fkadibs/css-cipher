import sys
from random import choice
from string import ascii_letters

if len(sys.argv) != 2:
    exit('Usage: cssipher.py <input>')

css_template = '.{name} span {{ display: none;}} .{name}:after {{ content: "{letter}";}} '

html_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html charset=UTF-8"/>
    <style type="text/css"> p {{ display: inline;}} {css} </style>
  </head>
  <body>
    {body}
  </body>
</html>
"""


def generate_html():
    # build the css
    css_output = ''
    name_map = {}
    
    for letter in ascii_letters:
        if letter in sys.argv[1]:
            css_class = ''.join(choice(ascii_letters) for x in range(3))
            css_output += css_template.format(name=css_class, letter=letter)
            name_map[letter] = css_class
    
    # build the html
    output_string = ''
    for letter in sys.argv[1]:
        if letter in letter_map.keys():
            output_string += '<p class="{}"><span>{}</span></p>'.format(letter_map[letter], choice(ascii_letters))
        else:
            output_string += i

    return html_template.format(css=css_output, body=output_string)


with open('output.html', 'w') as f:
    html = generate_html()
    f.write(html)
