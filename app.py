from flask import Flask, request, jsonify
from utilities import *
import numpy as np
import json

application = Flask(__name__)


@application.route("/")
def index():
    data = {}
    data["message"] = "Hello, your app is working!"
    return jsonify(data)

@application.route("/photo", methods=["POST"])
def index2():
    read = request.get_json()
    if type(read) == str:
        read = json.loads(read)
    img = read['img']
    img = decode(img)

    save = read['save']
    if save:
        save_face(img, read['name'])
        return "", 204
    else:
        new_img, names = get_faces(img)
        sound_bytes = read_names(names)
        data = {}
        data['img'] = new_img.tolist()
        data['sound'] = str(sound_bytes)
        data['names'] = names

        return jsonify(data)
