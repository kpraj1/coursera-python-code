import urllib.request, urllib.parse
import http, json, ssl

#proxy for geoapify.com
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) <1: break

    address= address.strip()
    params = dict()
    params['q']=address

    url = serviceurl+urllib.parse.urlencode(params)

    print("Retrieving",url)
    uh= urllib.request.urlopen(url, context=ctx)
    data= uh.read().decode()
    print("Retrieved",len(data),"characters",data[:25].replace('\n',' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('===Download Error===')
        print(data)
        break

    if len(js['features']) == 0:
        print("==object not found==")
        print(data)
        break
    #print(json.dumps(js, indent=4))
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    location = js['features'][0]['properties']['formatted']
    print('lat:',lat,'lon:',lon)
    print(location)