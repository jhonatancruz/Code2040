import requests
import json

t= '6a23da4bf386f3eeb5f2911f0e6ab947'
url= 'http://challenge.code2040.org/api/prefix'
payload = {'token': t}


r= requests.post(url, json= payload)
jsonReponse = json.loads(r.text)
prefix = jsonReponse['prefix']
words = jsonReponse['array']
not_prefix = []

# for i in range(0, len(words)):
#     if(words[i].startswith(prefix)== False):
#         not_prefix.append(words[i])
for item in words:
    if not item.startswith(prefix):
        not_prefix.append(item)

dictionary = {}
dictionary['token'] = t
dictionary['array'] = not_prefix

p = requests.post('http://challenge.code2040.org/api/prefix/validate', json = dictionary)
