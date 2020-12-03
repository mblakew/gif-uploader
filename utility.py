import requests
from decouple import config
import pyperclip as clip
from pathlib import Path

IMGUR_ENDPOINT = "https://api.imgur.com/3/image"
GIPHY_GET_ENDPOINT = "http://api.giphy.com/v1/gifs"
GIPHY_UPLOAD_ENDPOINT = "http://upload.giphy.com/v1/gifs"


# Returns file size in bytes
def get_file_size(file_path):
    file_size_in_bytes = Path(file_path).stat().st_size
    return (file_size_in_bytes / (1024*1024))


# Copies link to clipboard and exits. Prints error message if link is empty
def copy_to_clipboard(link):
    if link:
        clip.copy(link)
        print("\nThe link should be on your clipboard! If not, copy it here: " + link)
        exit()
    else:
        print(
            "\nSomething went wrong. The file might have been too large, or the daily upload limit " +
            "to Giphy may have been met check json for more details"
        )


# Returns None if file could not be opened
def get_file(path):
    file = ""
    try:
        file = open(path, "rb")
    except FileNotFoundError:
        return None
    return file


# Uploads file to imgur and returns link if successful (status code 200).
# If unsuccessful, returns None
def upload_to_imgur(file):
    CLIENT_ID = config("CLIENT_ID")

    payload = {"type": "file", "disable_audio": "0"}
    files = [("image", file)]
    headers = {"Authorization": "Client-ID {0}".format(CLIENT_ID)}

    res = requests.request("POST", IMGUR_ENDPOINT, headers=headers,
                           data=payload, files=files)
    if res.status_code != 200:
        return None

    return res.json()["data"]["link"]


def upload_to_giphy(file):
    GIPHY_ID = config("GIPHY_ID")
    USERNAME = config("GIPHY_USERNAME")
    params = {
        "api_key": GIPHY_ID,
        "username": USERNAME
    }

    res = requests.post(GIPHY_UPLOAD_ENDPOINT,
                        params=params, files={'file': file})
    data = res.json()

    if res.status_code != 200:
        print("\nFailed to upload to Giphy, take a look at the JSON: \n")
        print(data)
        exit()

    joined_endpoint = '/'.join((GIPHY_GET_ENDPOINT, data['data']['id']))
    res = requests.get(joined_endpoint, params=params)

    res_data = res.json()
    return res_data['data']['url']
