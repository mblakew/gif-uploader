import utility
import pyperclip as clip
from PIL import ImageGrab
import io
import codecs
import os
from pathlib import Path




file_path = input("\nPlease enter the path to the file you would like to upload: ")
print(Path(file_path).stat().st_size)


img = ImageGrab.grabclipboard()
img.show()
print("NEW TEST\n\n\n\n")
print(img.format)
# img = img.save('temp.gif')
# # print(img.save('/Users/blakewilliams/Projects/Python/mac2imgur/temp.jpeg'))
# print(img)

# print(utility.get_file('/Users/blakewilliams/Downloads/EJLcI7mU0AEKuzw.jpeg'))


# print(img)

# img_bytes = io.BytesIO()
# img.save(img_bytes, format='PNG')

# # Convert bytes to base64
# base64_data = codecs.encode(img_bytes.getvalue(), 'base64')

# # Convert base64 data to a string
# base64_text = codecs.decode(base64_data, 'ascii')

# html_img_tag = "<img src="data:image/png;base64, %s" />" % base64_text

# print(html_img_tag)


# utility.upload(img)

# while True:
#     file_path = input("\nPlease enter the path to the file you would like to upload: ")

#     file = utility.get_file(file_path)
#     if not file:
#         print("\nFile path is invalid")
#         continue

#     link = utility.upload(file)

#     if link:
#         clip.copy(link)
#         print("\nThe link should be on your clipboard! If not, here it is: " + link)
#         exit()
#     else:
#         print(
#             "\nSomething went wrong. The file might have been too large, check json for more details"
#         )
#         continue



if os.path.exists("temp.gif"):
  os.remove("temp.gif")

if os.path.exists("temp.jpeg"):
  os.remove("temp.jpeg")