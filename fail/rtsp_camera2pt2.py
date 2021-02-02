import base64
import urllib.request



request = urllib.request.Request("http://192.168.1.46/dms.jpg")
base64string =  bytes('%s:%s' % ('admin', 'kayuwood'), 'ascii')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib.request.urlopen(request)
resulttext = result.read()
