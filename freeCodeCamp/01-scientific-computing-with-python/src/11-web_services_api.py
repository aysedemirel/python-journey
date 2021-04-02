import urllib.request, urllib.parse, urllib.error
import json

service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input('Enter location:')
    if len(address) < 1: break

    url = service_url + urllib.parse.urlencode({'address': address})
    print('Retrieving',url)
    url = url +"&key=AIz....gLXk"
   
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    
    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or "status" not in js or js["status"] != "OK":
        print(" ==== Failure to retrieve  ====")
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat",lat,"lng",lng)
    location=js["results"][0]["formatted_address"]
    print(location)