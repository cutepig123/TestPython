# http://stackoverflow.com/questions/34079/how-to-specify-an-authenticated-proxy-for-a-python-http-connection

# import os, urllib
#os.environ["http_proxy"] = "http://proxyserver:3128"
# data = urllib.urlopen("http://www.google.com").read()
# print data

# import urllib2, urllib

# proxy = urllib2.ProxyHandler({'http': 'http://aaants10.aaaex.asmpt.com:80'})
# auth = urllib2.HTTPBasicAuthHandler()
# opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
# urllib2.install_opener(opener)

# conn = urllib2.urlopen('http://python.org')
# return_str = conn.read()
# print return_str

import urllib2

def get_proxy_opener(proxyurl='http://aaants10.aaaex.asmpt.com:80', proxyuser="aaaex\\aeejshe", proxypass="hejinshou", proxyscheme="http"):
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, proxyurl, proxyuser, proxypass)

    proxy_handler = urllib2.ProxyHandler({proxyscheme: proxyurl})
    proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)

    return urllib2.build_opener(proxy_handler, proxy_auth_handler)

if __name__ == "__main__":
    import sys
    url_opener = get_proxy_opener()
#    print url_opener.open('http://www.google.com').read()
    urllib2.install_opener(url_opener)
    print urllib2.urlopen('http://www.google.com').read()

    #if len(sys.argv) > 4:
        #url_opener = get_proxy_opener(*sys.argv[1:4])
        #for url in sys.argv[4:]:
        #    print url_opener.open(url).headers
    #else:
       # print "Usage:", sys.argv[0], "proxy user pass fetchurls..."
