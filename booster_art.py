from PIL import Image
import requests
from io import BytesIO
from typing import Literal
from make_booster import make_clayton_booster

#Literal of types of card art, this is only a literal so pycharm will show you all your options
ART_TYPES = Literal["small", "normal", "large", "png", "art_crop", "border_crop"]

#Takes in a link to an image and returns it
def get_image_from_url(url: str) -> Image.Image:
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

#Takes in a card from a booster pack and returns its image(optional art type)
def get_card_art(card: dict, art_type: ART_TYPES = 'normal'):
    return get_image_from_url(card['image_uris'][art_type])

#Takes in a booster pack and returns a list of images of the card art (optional art type)
def get_booster_art(booster: list[dict], art_type: ART_TYPES = 'normal') -> list[Image.Image]:
    arts = []
    for card in booster:
        arts.append(get_card_art(card, art_type))
    return arts

if __name__ == '__main__':

    #Debug makes booster pack and shows each card's art
    b = make_clayton_booster('dft', 'play')
    for image in get_booster_art(b, 'small'):
        image.show()