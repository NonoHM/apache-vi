# to open/create a new html file in the write mode
f = open('./tests/test.html', 'w')
c = open('./tests/test.css', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>




<h2>Welcome To site de fou</h2>

<p>Default code has been loaded into the Editor.</p>






</body>
</html>
"""
css_template = """




"""

# writing the code into the file
f.write(html_template)
c.write(css_template)

# close the file
f.close()
c.close()