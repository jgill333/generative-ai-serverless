import os
import json
import random
from flask import Flask, request, make_response
from werkzeug.exceptions import HTTPException


STABILITY_AI_API_KEY = os.environ.get("STABILITY_AI_API_KEY", "REPLACE_ME_WITH_KEY_IF_NOT_IN_OS_ENV_VARIABLES")


app = Flask(__name__)


@app.get("/")
def hello_world():
    return {"message": "Hello!"}


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@app.route("/fun", methods=["POST", "GET"], strict_slashes=False)
@app.route("/fun/<prompt>", methods=["POST", "GET"], strict_slashes=False)
def generate_peter_g_image(provider="stability", prompt: str = ""):
    if not prompt:
        prompt = request.args.get("text", request.args.get("prompt", ""))

    if provider.lower() != "stability":
        provider = "openai"

    image_styles = [
        "Photograph",
        "High-fashion photography",
        "Renaissance-style portrait",
        "Velvet painting",
        "Cinematic photo",
    ]

    venues = [
        "in Austin",
        "in Berkley, California",
        "in Boston",
        "at a famous Austin landmark",
        "at a bar in Boston",
        "at Berkeley the university",
        "in Palo Alto",
        "at a famous Boston landmark",
        "at a Boston Red Socks game",
        "at a Boston Bruins game",
    ]

    random_people = [
        "Noam Chomsky",
        "Larry Page",
        "Geoffrey Hinton",
        "Alan Kay",
        "Bob Metcalfe",
        "Tim Berners-Lee",
        "Margaret Hamilton",
        "Alan Turing",
        "Barbara Liskov",
        "Shafi Goldwasser",
        "Claude Shannon",
        "Sergey Brin",
        "Mark Dean",
        "Steve Wozniak",
        "Steve Jobs",
        "Bill Gates",
        "Jeff Bezos",
        "Albert Einstein",
        "Grace Hopper",
        "Richard Feynman",
        "Garfield The Cat",
        "Mario from the Nintendo video games",
        "Monica Bellucci",
        "Emma Stone",
        "Nicolas Cage",
    ]

    important_figures = ["Santa Claus", "Friendly and Happy Snowman", "Happy Polar bear"]

    image_style = random.choice(image_styles)
    chosen_person1 = random.choice(random_people)
    chosen_person2 = random.choice(random_people)
    chosen_figure = random.choice(important_figures)
    chosen_venue = random.choice(venues)

    prompt_list = []
    prompt_suffixes = [
        "Not blurry",
        "No unrealistic people",
        "No deformed structures",
        "Ensure that the image is not low contrast",
    ]

    suffix_weight = 0.9

    if not prompt:
        prompt += (
            f"{image_style.title()} of {chosen_person1} and {chosen_person2} dressed for "
            f"the Christmas winter holidays having a great time drinking "
            f"cocktails with {chosen_figure} {chosen_venue}."
        )

    prompt_list.append({"text": prompt[:2000], "weight": 0.8})

    # key_phrase = "Jonathan's"
    # prompt_list.append(
    #     {
    #         "text": f"Ensure that the text {key_phrase} is on a neon sign and that there is a disco ball.",
    #         "weight": 0.93,
    #     }
    # )

    for ps in prompt_suffixes:
        prompt_list.append({"text": ps, "weight": suffix_weight})

    import base64
    import requests

    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = "https://api.stability.ai"
    api_key = STABILITY_AI_API_KEY

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "text_prompts": prompt_list,
            "cfg_scale": 8,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 40,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    for i, image in enumerate(data["artifacts"]):
        img_bytes = base64.b64decode(image["base64"])
        response = make_response(img_bytes)
        response.headers.set("Content-Type", "image/png")
        return response
    return "No image generated", 500


if __name__ == "__main__":
    app.run()
