import utility
import pyperclip as clip

while True:
    file_path = input("\nPlease enter the path to the file you would like to upload: ")

    
   
    print("\nAttempting Imgur upload...")
    link = utility.upload_to_imgur(file_path)

    if not link:
        print("\nUpload to Imgur failed, uploading to Giphy...")
        link = utility.upload_to_giphy(file_path)

    if link:
        clip.copy(link)
        print("\nThe link should be on your clipboard! If not, copy it here: " + link)
        exit()
    else:
        print(
            "\nSomething went wrong. The file might have been too large, or the daily upload limit " +
            "to Giphy may have been met check json for more details"
        )
        continue
