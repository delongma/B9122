import urllib.request
response=urllib.request.urlopen('http://placekitten.com/500/600')
cat_image=response.read()

with open('cat_500*600.jpg','wb')as f:
    f.write(cat_image)
