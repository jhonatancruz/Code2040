import urllib.parse
import urllib.request

#accessing the page with a token
url = 'http://challenge.code2040.org/api/reverse'
values = {'token' : '6a23da4bf386f3eeb5f2911f0e6ab947'
          }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read() # reading in the string
reverse_page= the_page[::-1] # reversing the string

#accessing the page to submit the reverserd string and sending it there
url = 'http://challenge.code2040.org/api/reverse/validate'
values = {'token' : '6a23da4bf386f3eeb5f2911f0e6ab947',
        'string':reverse_page }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
