from io import BytesIO,StringIO
import requests
from PIL import Image


img_url = "http://www.neeu.com/uploads/photo2/644/644534/1372839968983.jpg"

response = requests.get(img_url)

f = BytesIO(response.content)
img = Image.open(f)
print(img.size)
