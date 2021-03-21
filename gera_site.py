import webbrowser


def abrir_site(links):
    # to open/create a new html file in the write mode
    f = open('x.html', 'w')

    link_string = ''
    for index, link in enumerate(links):
        link_string += f"<li><p>Link {index + 1}: <a href='{link}' target='_blank'>{link}</a></p></li>"

    # the html code which will go in the file GFG.html
    html_template = f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Links dos conteúdos</title>
    </head>
    <body>
        <ul>
            {link_string}
        </ul>
    </body>
    </html>
    """

    # writing the code into the file
    f.write(html_template)

    # close the file
    f.close()

    webbrowser.open_new_tab('x.html')
