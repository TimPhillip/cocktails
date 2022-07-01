from flask import Flask
import os
import json

app = Flask(__name__, instance_relative_config=True)


def read_cocktails(path):
    all = []

    for file in os.listdir(path):

        with open(os.path.join(path, file), 'r') as f:
            cocktail_data = json.load(f)
            all.append(cocktail_data)

    return all


all_cocktails = read_cocktails(os.path.join(__path__[0], "../data"))

import cocktails.routes

