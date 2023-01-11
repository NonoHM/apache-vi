"""
Website module creator
"""
output_dir = '../output_dir'
output_dir_img = './img'
log_length = 69



def html_creator(log_length, output_dir):
    # to open/create a new html file in the write mode
    html = open(output_dir + '/index.html', 'w')
    css = open(output_dir + '/style.css', 'w')
    
    # the html code which will go in the file index.html
    html_template = f"""<html>

    <head>
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>Apache-vi</title>
    </head>
    <body>
        <header>
            <h1>Bienvenue sur notre page Apache</h1>
        </header>
        <nav>
            <ul>
                <li><a href="#">Accueil</a></li>
                <li><a href="#">Galerie</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <main>
            <section id="accueil">
                <h2>Bienvenue sur notre site</h2>
            </section>

            <h2>Découvrez nos dernières images</h2>
            
            <p class="m-2 text-xl">There is {log_length} lines in the log file</p>

            <div class="image-grid">
                <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/browser_graph.png" alt="Breakdown of connections by browser"/>
                <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/week_graph.png" alt="Histogram of connections by week"/>
                <img class="my-2 rounded-xl w-1/3" src="{output_dir_img}/month_graph.png" alt="Histogram of connections by month"/>
            </div>

            <section id="contact">
                <p>Pour plus de question vous pouvez nous contacter par mail au addreeses suivantes :</p>
                <p>alex.barbot@etu.univ-poitiers.fr ou noah.houmeau@etu.univ-poitiers.fr</p>
            </section>

        </main>
        <footer>
            <div class="contact-info">
                <a href="https://github.com/NonoHM/apache-vi", target="_blank">
                    <img src="image/logo-git.png" alt="Logo de GitHub">
                </a>

            </div>
        </footer>
    </body>
</html>
    """

    css_template = """
    * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        color: #444;
    }

    header {
        background-color: #333;
        color: #fff;
        padding: 20px;
        text-align: center;
    }

    header h1 {
        margin: 0;
        font-size: 36px;
    }

    nav {
        background-color: #eee;
        display: flex;
        justify-content: center;
    }

    nav ul {
        display: flex;
        list-style: none;
    }

    nav li {
        margin: 0 10px;
    }

    nav a {
        color: #444;
        text-decoration: none;
        font-size: 18px;
        padding: 10px 15px;
        display: block;
    }

    nav a:hover {
        background-color: #333;
        color: #fff;
    }

    main {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    main h2 {
        margin-bottom: 20px;
        font-size: 24px;
        text-align: center;
    }

    .image-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 10px;
    }

    .image-grid img {
        width: 100%;
        height: auto;
        border-radius: 5px;
        object-fit: cover;
        transition: transform 0.3s;
    }

    .image-grid img:hover {
        transform: scale(1.1);
    }

    footer {
        background-color: #333;
        color: #fff;
        padding: 20px;
        text-align: center;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }

    footer p {
        margin: 0;
        font-size: 14px;
    }
    .contact-info img {
        width: 32px;
        height: 32px;
        margin-right: 10px;
        vertical-align: middle;
    }

    """
    # writing the code into the file
    html.write(html_template)
    css.write(css_template)
    # close the file
    html.close()
    css.close()

