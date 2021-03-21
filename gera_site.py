import webbrowser


def abrir_site(links):
    # Abre o arquivo
    f = open('x.html', 'w')

    # Gera a lista de links
    link_string = ''
    for index, link in enumerate(links):
        link_string += f"<li><p>Link {index + 1}: <a href='{link}' target='_blank'>{link}</a></p></li>"

    # Gera o html da página
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

    # Escreve o html no arquivo
    f.write(html_template)

    # Fecha o arquivo
    f.close()

    # Abre o arquivo no browser
    webbrowser.open_new_tab('x.html')
