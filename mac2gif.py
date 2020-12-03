import utility as util


def upload(file_path):
    if util.get_file_size(file_path) < 10:
        print("\nUploading to Imgur...")
        link = util.upload_to_imgur(util.get_file(file_path))
    else:
        print("\nFile too large for Imgur, uploading to Giphy...")
        link = util.upload_to_giphy(util.get_file(file_path))

    util.copy_to_clipboard(link)


while True:
    file_path = input(
        "\nPlease enter the path to the file you would like to upload: ")
    # exit()
    upload(file_path)
