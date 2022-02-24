import requests
import json
app_id = "62b446bs"
app_key = "c2fe6960887f53b88999a76728dd7e34"
language = 'en-gb'
fields = 'pronunciations'
strictMatch = 'false'
word_id = 'python'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)

print("Ali".lower())