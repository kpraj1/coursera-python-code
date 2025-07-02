import urllib.request, urllib.parse
import json, ssl


serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

#ignoring ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

location = input("Enter location: ")
if len(location)<1:
    print("enter valid location next time, for now we are shutting the program for wrong input")

location= location.strip()
params = dict()
params["q"]=location

url = serviceurl + urllib.parse.urlencode(params)

print("Retrieving",url)

data = urllib.request.urlopen(url,context=ctx).read().decode()
print("Retrieved",len(data),"characters")

try:
    js = json.loads(data)
except:
    js = None

if js is not None:
    #print(json.dumps(js,indent=4))
    print("Plus code",js["features"][0]["properties"]["plus_code"])
else:
    print("we got no data")