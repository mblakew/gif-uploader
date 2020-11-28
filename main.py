import utility
import pyperclip as clip

while True:
    file_path = input("\nPlease enter the path to the file you would like to upload: ")

    file = utility.get_file(file_path)
    if not file:
        print("\nFile path is invalid")
        continue

    link = utility.upload(file)

    if link:
        clip.copy(link)
        print("\nThe link should be on your clipboard! If not, here it is: " + link)
        exit()
    else:
        print(
            "\nSomething went wrong. The file might have been too large, check json for more details"
        )
        continue
