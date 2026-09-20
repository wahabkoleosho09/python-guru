"""
a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

FILENAME = input("File name: ").strip().lower()
images = ("jpg","jpeg","png","gif")
documents = ("pdf","doc","docx","zip","rar","7z")
videos = ("mp4","avi","mov","mkv")
plain = ("txt")
zip_files = ("zip","rar","7z")

try:
    file_name,extension = FILENAME.rsplit("." , 1)
    if extension in images:
        print(f"image/{extension}",end="")
    elif extension in plain:
        print(f"text/plain",end="")
    elif extension in documents:
        print(f"application/{extension}",end="")
    elif extension in videos:
        print(f"videos/{extension}",end="")
    # elif extension in zip_files:
    #     print(f"application/{extension}",end="")
    else:
        print("application/octet-stream")
except ValueError:
    print("application/octet-stream")
