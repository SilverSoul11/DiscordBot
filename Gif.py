import requests

"""Function to post random funny gif from giphy website."""
def Meme():
    api_key = "OeVOS0X6WOQNHUEtsOqXobSt3jvPeA11"
    url = "https://api.giphy.com/v1/gifs/random?api_key=" + api_key + "&tag=funny&rating=R"
    get_json_data = requests.get(url).json()
    get_url = get_json_data['data']['url']
    return get_url()
