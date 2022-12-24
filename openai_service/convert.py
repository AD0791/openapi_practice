from json import load
from base64 import b64decode
from pathlib import Path

DATA_DIR = Path.cwd() / "responses"
JSON_FILE = DATA_DIR / "openai_image_1671918753.json"
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

IMAGE_DIR.mkdir(parents=True, exist_ok=True)


with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)


""" def convert_image():
    with open(JSON_FILE, mode="r", encoding="utf-8") as file:
        response = load(file)

    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
        with open(image_file, mode="wb") as png:
            the_image = png.write(image_data)
    return the_image
 """
