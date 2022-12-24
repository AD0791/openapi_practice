from json import dump
from os import getenv
from pathlib import Path

from openai import (
    api_key,
    Image
)

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

api_key = getenv("OPENAI_API_KEY")

response = Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"openai_image_{response['created']}.json"



if "__name__" == "main.py":
    with open(file_name, mode="w", encoding="utf-8") as file:
        dump(response, file)
