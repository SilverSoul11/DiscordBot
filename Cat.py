import requests

"""Function for getting random cat pictures."""
def getCatPic():
    url = "https://api.thecatapi.com/v1/images/search?size=full&mime_types=jpg,png,gif&format=json&order=RANDOM&page=0"
    get_json_data = requests.get(url).json()
    get_url = get_json_data[0]['url']
    return get_url
