import urllib.parse
import urllib.request

url = 'http://challenge.code2040.org/api/register'
values = {'token' : '6a23da4bf386f3eeb5f2911f0e6ab947',
          'github' : 'https://github.com/jhonatancruz/Code2040',
          }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)
