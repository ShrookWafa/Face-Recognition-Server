import requests 
import numpy as np
import json
import base64
import matplotlib.image


URL = "http://127.0.0.1:5000/photo"

f = open('image.jpg', 'rb').read()
f = str(base64.b64encode(f))
f = f[2:len(f)-1]

data = {"img": f, "name": "Shrook", "save": 1}

headers = {'content-type': 'application/json'}

r = requests.post(url=URL, json=json.dumps(data))

print("Response code is: ", r)

data = r.json()
print(data.keys())

print(data['names'])

sound = data['sound']
sound = sound[2:len(sound)-1]
sound = base64.b64decode(sound)

nf = open('myoutput.mp3', 'wb')
nf.write(sound)
nf.close()

image = data['img']
image = np.array(image, dtype=np.uint8)
matplotlib.image.imsave('myimg.png', image)

