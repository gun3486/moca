import requests
import json

url = 'https://schoolmenukr.ml/api/high/F100000120'
response = requests.get(url)
school_menu = json.loads(response.text)
print(school_menu)