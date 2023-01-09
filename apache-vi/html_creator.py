"""
Website module creator
"""
output_dir = '../output_dir'
output_dir_img = './img'
log_length = 69



def html_creator(log_length, output_dir):
    # to open/create a new html file in the write mode
    html = open(output_dir + '/index.html', 'w')
    
    # the html code which will go in the file index.html
    html_template = f"""<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.tailwindcss.com"></script>
        <title></title>
    </head>
    <body>

    <h1 class="m-2 text-4xl font-bold leading-tight text-center text-gray-800">Log results</h1>
    <p class="m-2 text-xl">There is {log_length} lines in the log file</p>
    <div class="m-4 flex">
        <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/browser_graph.png" alt="Breakdown of connections by browser"/>
        <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/week_graph.png" alt="Histogram of connections by week"/>
        <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/month_graph.png" alt="Histogram of connections by month"/>
    </div>
    </body>
    </html>
    """
    
    # writing the code into the file
    html.write(html_template)
    # close the file
    html.close()
