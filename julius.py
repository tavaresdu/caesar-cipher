#!/usr/bin/env python
import os
import json
import string
import hashlib
from collections import deque
import requests

__author__ = "Eduardo Corrêa"
__email__ = "tavaresdu@gmail.com"

URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
TOKEN = os.environ['CODENATION_TOKEN']
FILENAME = 'answer.json'

def main():
    j = get_json_from_api()
    j['decifrado'] = decipher_text(j['cifrado'], j['numero_casas'])
    j['resumo_criptografico'] = sha1_hash(j['decifrado'])
    save_json_to_file(j)

def get_json_from_api():
    response = requests.get(URL + TOKEN)
    return json.loads(response.text)

def decipher_text(ciphered_text, rotation):
    intab = rotate_text(string.ascii_lowercase, rotation)
    transtab = str.maketrans(intab, string.ascii_lowercase)
    return ciphered_text.translate(transtab)

def rotate_text(text, rotation):
    lst = list(text)
    rotation = rotation % len(lst)
    lst = lst[rotation:] + lst[:rotation]
    return ''.join(lst)

def sha1_hash(text):
    h = hashlib.sha1(text.encode('UTF-8'))
    return h.hexdigest()

def save_json_to_file(json_obj):
    json_str = json.dumps(json_obj)
    with open(FILENAME, 'w') as f:
        f.write(json_str)

if __name__ == '__main__':
    main()