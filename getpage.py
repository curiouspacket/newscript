

import httplib

try:
    h = httplib.HTTPConnection("www.google.com")
    h.request("HEAD" , "/")
    r = h.getresponse()
    print r.status, r.reasone
    h.close()

except Exception as ex:
    print "Couldn't find page"



    




