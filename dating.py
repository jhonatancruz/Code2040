from datetime import datetime
from datetime import timedelta
from time import strftime
import dateutil.parser
import requests
import json

t= '6a23da4bf386f3eeb5f2911f0e6ab947'
url= 'http://challenge.code2040.org/api/dating'
payload = {'token': t}

r= requests.post(url, json= payload)
jsonResponse = json.loads(r.text)

datestamp = jsonResponse['datestamp'] # requests value of datestamp
interval = jsonResponse['interval'] # requests value of interval

parseDate= dateutil.parser.parse(datestamp) # converts from ISO format to DateTime format
addDate= parseDate+ timedelta(seconds= interval) #adds the number of seconds

convert= addDate.isoformat()
convert= convert[:20].replace('+','Z' )

dictionary = {}
dictionary['token'] = t
dictionary['datestamp'] = convert

p = requests.post('http://challenge.code2040.org/api/dating/validate', json = dictionary)
