import requests
from decouple import config


def get_file(path):
    file = ""
    try:
        file = open(path, "rb")
    except FileNotFoundError:
        return None
    return file


# Uploads file to imgur and returns link if successful (status code 200).
# If unsuccessful, returns None
def upload_to_imgur(path):
    file = get_file(path)
    url = "https://api.imgur.com/3/image"
    CLIENT_ID = config("CLIENT_ID")

    payload = {"type": "file", "disable_audio": "0"}
    files = [("image", file)]
    headers = {"Authorization": "Client-ID {0}".format(CLIENT_ID)}

    res = requests.request("POST", url, headers=headers, data=payload, files=files)
    if res.status_code != 200:
        # print("Something went wrong, response: ")
        # print(res.json())
        return None

    return res.json()["data"]["link"]


def upload_to_giphy(path):
    file = get_file(path)
    api_endpoint = "http://api.giphy.com/v1/gifs"
    upload_endpoint = "http://upload.giphy.com/v1/gifs"
    GIPHY_ID = config("GIPHY_ID")
    USERNAME = config("GIPHY_USERNAME")
    params = {
    "api_key": GIPHY_ID,
    "username": USERNAME
    }



    res = requests.post(upload_endpoint, params=params, files={'file': file})
    data = res.json()
    print("\nDATA: \n")
    print(data)
    gif_id = data['data']['id']
    print("\nJOINED_ENDPOINT: \n ")
    joined_endpoint = '/'.join((api_endpoint, gif_id))
    print(joined_endpoint)
    
    res = requests.get(joined_endpoint, params=params)
    res_data = res.json()
    print(res_data)
    return res_data['data']['url']