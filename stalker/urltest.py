import urllib.request
import urllib.parse
import requests
#Subclass of HTTPRedirectHandler. Does not do much, but is very
#verbose. prints out all the redirects. Compaire with what you see
#from looking at your browsers redirects (using live HTTP Headers or similar)
class ShibRedirectHandler (urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print (req)
        print (fp.geturl())
        print (code)
        print (msg)
        print (headers)
        #without this return (passing parameters onto baseclass) 
        #redirect following will not happen automatically for you.
        return urllib.request.HTTPRedirectHandler.http_error_302(self,
                                                          req,
                                                          fp,
                                                          code,
                                                          msg,
                                                          headers)

cookieprocessor = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(ShibRedirectHandler, cookieprocessor)

#Edit: should be the URL of the site/page you want to load that is protected with Shibboleth
(opener.open("https://www.info.iastate.edu/individuals/info/263608/Zabloski-Kyle").read())

#Inspect the page source of the Shibboleth login form; find the input names for the username
#and password, and edit according to the dictionary keys here to match your input names
loginData = urllib.parse.urlencode({'username':'gemanley@iastate.edu', 'password':'Epson273'})
bLoginData = loginData.encode('ascii')

#By looking at the source of your Shib login form, find the URL the form action posts back to
#hard code this URL in the mock URL presented below.
#Make sure you include the URL, port number and path
response = opener.open("https://test-idp.server.example", bLoginData)
#See what you got.
print (response.read())
