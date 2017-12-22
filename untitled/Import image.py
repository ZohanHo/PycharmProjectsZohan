import random

import urllib.request


def load(url):
    name = random.randrange (1, 10000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve (url, full_name)

load ("http://vignette2.wikia.nocookie.net/lotr/images/b/be/HBT-DWF-007.jpg/revision/latest/scale-to-width-down/640?cb=20120318235802")