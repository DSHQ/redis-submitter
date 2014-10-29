__author__ = 'ob3'

import urllib
from httplib2 import Http
from urllib import urlencode
import json
import logging
# >>> h = Http()
# >>> data = dict(name="Joe", comment="A test comment")
# >>> resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
# >>> resp
# {'status': '200', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding,User-Agent',
#  'server': 'Apache', 'connection': 'close', 'date': 'Tue, 31 Jul 2007 15:29:52 GMT',
#  'content-type': 'text/html'}

class Submitter:
    h = None
    def __init__(self):
        self.h = Http()
        pass

    def __call__(self, *args, **kwargs):
        print "test"
        pass

    def request(self, url, method, data):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        send_data = None
        send_data = dict(data=json.dumps(data))

        send_data = urllib.urlencode(send_data)
        return self.h.request(url, method.upper(), body=send_data, headers=headers)