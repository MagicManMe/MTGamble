import webbrowser

from make_booster import make_clayton_booster
import json

booster = make_clayton_booster('dft','play')

#save json file for debugging
JSON_NAME = 'test.json'
with open(JSON_NAME, 'w', encoding='utf-8') as file:
    # json.dump([card for card in booster], file, indent=4, ensure_ascii=False)
    json.dump(booster, file, indent=4)


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
    image_url = card['image_uris']['normal']
    html_content += f'<img src="{image_url}" alt="Card Image">\n'

# Close HTML content
html_content += """
    </div>
</body>
</html>
"""

print(html_content)



#Debug stuff
"""poop = 0
while poop == 0:


    for i in range(6):
        if int(booster[i]['collector_number']) in range(292,332):
            poop = 1
            break
    booster = make_clayton_booster('dft', 'play')"""


# Save the HTML file
html_file = "booster_pack.html"
with open(html_file, "w", encoding="utf-8") as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open(html_file)