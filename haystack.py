import urllib.parse
import urllib.request
import json

#accessing the page with a token
url = 'http://challenge.code2040.org/api/haystack'
values = {'token' : '6a23da4bf386f3eeb5f2911f0e6ab947'
          }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read().decode("utf-8") # reading in the string and decoding it
jsonResponse=json.loads(the_page)
haystack = jsonResponse["haystack"]
needle= jsonResponse["needle"]
needleVal= haystack.index(needle)

url = 'http://challenge.code2040.org/api/haystack/validate'
values = {'token' : '6a23da4bf386f3eeb5f2911f0e6ab947',
        'needle':needleVal }
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)





# needle= de("needle")
# haystack= de("haystack")
# pos= haystack.index(needle)
#
# for needle in de:
#     if haystack==de['needle']:
#         print("yes")
#needleVal= de.get('needle')
#print(the_page)
# print(de)
# print(needle)
# print(haystack)
# print(pos)
