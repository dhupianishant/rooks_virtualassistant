def Weather():
    import geocoder
    import requests
    ip = geocoder.ip('me')
    city = ip.city
    print(city)
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    print(res.text)