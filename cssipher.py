import sys
from random import choice
from string import ascii_letters

if len(sys.argv) != 2:
    exit('Usage: cssipher.py <input>')

def generate_class():
    return ''.join(choice(ascii_letters) for x in range(3))

def generate_css():
    css_output = ''
    name_map = {}
    for letter in string.ascii_letters:
        if letter in input_string:
            css_class = generate_class()
            css_output += span_template.format(name=css_class, letter=letter)
            name_map[letter] = css_class
    return css_output, name_map

span_template = '.{name} span {{ display: none;}} .{name}:after {{ content: "{letter}";}} '

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

output_string = ''
css_output, letter_map = generate_css()

for i in sys.argv[1]:
    if i in letter_map.keys():
        output_string += '<p class="{}"><span>{}</span></p>'.format(letter_map[i], choice(ascii_letters))
    else:
        output_string += i

html_output = html_template.format(css=css_output, body=output_string)

with open('output.html', 'w') as f:
    f.write(html_output)
