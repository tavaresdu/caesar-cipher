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
    json_obj = get_json_from_api()
    json_obj['decifrado'] = decipher_text(json_obj['cifrado'])
    json_obj['resumo_criptografico'] = calculate_hash(json_obj['decifrado'])
    save_json_to_file(json_obj)

def get_json_from_api():
    pass

def decipher_text(ciphered_text):
    pass

def calculate_hash(text):
    pass

def save_json_to_file(json_obj):
    pass

if __name__ == '__main__':
    main()