import re
import json
import os
import threading
import time
import requests
import shutil
from requests.exceptions import RequestException

def get_proble_set(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

url = "https://leetcode.com/api/problems/all/"
html = json.loads(get_proble_set(url))
problemset = html["stat_status_pairs"]

namesset = {}
names = []

for data in problemset:
    s = ''
    str(data["stat"]["frontend_question_id"]) + "_" + data["stat"]["question__title"]
    for c in (str(data["stat"]["frontend_question_id"]) + "_" + data["stat"]["question__title"]):
        if(c == ' ' ): 
            s = s + "_"
        elif(c == '//'):
            s = s + '_'
        elif(c == ':'): 
            s = s
        elif(c == '?'):
            s = s + "_question"
        elif(c != ' '): 
            s = s + c

    # print(s)
    namesset[int(s.split("_")[0])] = s

for name in sorted (namesset):
    path = str(int(int(name) / 100 + 1) * 100)+"/"+namesset[name]
    # print(path)
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        
    folder = os.path.exists(path + "/main.cpp")
    if not folder:
        shutil.copy('./get_topic/code/main.cpp', path)

    folder = os.path.exists(path + "/CMakeLists.txt")
    if not folder:
        shutil.copy('./get_topic/code/CMakeLists.txt', path) 

    folder = os.path.exists(path + "/readme.md")
    if not folder:
        shutil.copy('./get_topic/code/readme.md', path) 
    
