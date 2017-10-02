# Instructions
#
# easy_install requests
# python dashku_59d23c86dacdcd2d0235ae09.py
#
import requests
import json

payload = {
  "message": "Affirmative, Dave. I read you.",
  "_id": "59d23c86dacdcd2d0235ae09",
  "apiKey": "43311178-4f63-40ce-bf73-73ea510fb581"
}
headers = {'content-type': 'application/json'}

requests.post('http://dashku.com/api/transmission', data=json.dumps(payload),headers=headers)