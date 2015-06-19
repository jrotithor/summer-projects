import urllib.request
with urllib.request.urlopen("http://www.wikipedia.net") as response:
    html = response.read();
print(html);
