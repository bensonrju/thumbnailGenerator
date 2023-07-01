import urllib.request

webURL = 'https://www.te.com/usa-en/product-DTM04-2P.html'
myHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

req = urllib.request.Request(webURL, data=None, headers=myHeaders)
print(req)
#print(urllib.request.urlopen(req))

with urllib.request.urlopen(req) as response:
    print(response)
    html = response.read()

#print(rawBytes)