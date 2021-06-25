import urllib.request
from os import rename, mkdir

web_url = input("請輸入Youtube網址: ")
# web_url = input("Enter Youtube video url: ")
img_file = open("ytimg.txt", "a", encoding="utf-8")
video_link = web_url[32:]

img_link = ("https://img.youtube.com/vi/" + video_link + "/maxresdefault.jpg" + "\n")

img_file.write(img_link)
img_file.close()

try:
    mkdir("Image")
except FileExistsError:
    Do_Nothing = 0

urllib.request.urlretrieve(img_link, "Image/maxresdefault.jpg")
rename('Image/maxresdefault.jpg', 'Image/' + video_link + '.jpg')
