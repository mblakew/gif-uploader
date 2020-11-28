import requests as requests
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
def upload(file):
    url = "https://api.imgur.com/3/image"
    CLIENT_ID = config("CLIENT_ID")

    payload = {"type": "file", "disable_audio": "0"}
    files = [("image", file)]
    headers = {"Authorization": "Client-ID {0}".format(CLIENT_ID)}

    res = requests.request("POST", url, headers=headers, data=payload, files=files)
    if res.status_code != 200:
        print("Something went wrong, response: ")
        print(res.json())
        return None

    return res.json()["data"]["link"]
