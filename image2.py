import urllib.request
import random
def image(url):
    name=str(random.randrange(1,1000))+".jpg"
    urllib.request.urlretrieve(url,name)
image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmRRDWaHZ1HjgZNChh4psolxIHbsIPXqyZIvnd7WAtJdbqMTezag")