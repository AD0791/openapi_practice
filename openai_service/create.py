from json import dump
from pathlib import Path
from decouple import config 
from dotenv import load_dotenv
from base64 import b64decode
import openai


load_dotenv()
OPENAI_API_KEY= config('OPENAI_API_KEY')

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
DATA_DIR = Path.cwd() / "responses"
DATA_DIR.mkdir(exist_ok=True)

openai.api_key = OPENAI_API_KEY

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"openai_image_{response['created']}.json"


with open(file_name, mode="w", encoding="utf-8") as file:
    dump(response, file)


""" def create_image():
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
        response_format="b64_json",
    )

    file_name = DATA_DIR / f"openai_image_{response['created']}.json"


    with open(file_name, mode="w", encoding="utf-8") as file:
        json_file = dump(response, file)
    
    return json_file
 """
