import webbrowser
import json
from make_booster import make_clayton_booster
from typing import Literal

#list of card art types for type hinting in below function
ART_TYPES = Literal["small", "normal", "large", "png", "art_crop", "border_crop"]


#Function that takes in a booster and returns the html string, can be saved to an HTML file if wanted for viewing
#Currently shows export to file at bottom of booster_html.py
def booster_to_html(booster: list[dict], art_type: ART_TYPES = 'normal') -> str: #art_type is optional, defaults is 'normal' if not specified
    # Generate HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Booster Pack Art</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            .card-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
            img { width: 250px; height: auto; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2); }
        </style>
    </head>
    <body>
        <h1>Booster Pack Art</h1>
        <div class="card-container">
    """

    # Fetch images and add them to HTML
    for card in booster:
        image_url = card['image_uris'][art_type]
        html_content += f'<img src="{image_url}" alt="Card Image">\n'

    # Close HTML content
    html_content += """
        </div>
    </body>
    </html>
    """

    return html_content


#Function to write a booster to a file for debugging purposes, art_type is optional
def write_booster_to_file(booster: list[dict], filename: str, art_type: ART_TYPES = 'normal'):
    html_content = booster_to_html(booster, art_type)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)




#Makes it so this only runs when we run this file, not when we import it to use booster_to_html function
if __name__ == '__main__':
    #Make a booster
    b = make_clayton_booster('dft', 'play')
    #write that booster to html file
    write_booster_to_file(b, 'booster_pack.html')

    #Open the HTML file in the default web browser
    #webbrowser.open('booster_pack.html')

    # Debug stuff
    """poop = 0
    while poop == 0:
        for i in range(6):
            if int(booster[i]['collector_number']) in range(292,332):
                poop = 1
                break
        booster = make_clayton_booster('dft', 'play')"""