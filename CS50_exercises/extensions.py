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
