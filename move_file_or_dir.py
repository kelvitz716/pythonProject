import os


source = "C:\\Users\\user\\Downloads\\IMG_20230423_082131.jpg" #put here the full file directory
destination = "C:\\Users\\user\\OneDrive\\Pictures\\shee's.jpg" #put here the full destination directory

try:
    if os.path.exists(destination):
        print("There's a similar file/dir in destination location: ")
    else:
        os.replace(source,destination)
        print(f"{source} file/dir was moved. ")
except ValueError as e:
    print(e)
