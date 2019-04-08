import json
import os
import KNKY_ZenParser as Parser

def loadURLsFromJson():
    if os.path.exists("input.json"):
        with open("input.json") as json_data:
            d = json.load(json_data)
        return d["urls"]
    else:
        print('JSON file not found. Create input.json with {"urls": ["url1", "url2", "..."]}')
    return []

Parser.parseToHtml(loadURLsFromJson())