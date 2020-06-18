import re
from urllib.parse import urlparse

def domain_name(url):

    if url[0] == 'h' and 'www' in url:
        o = urlparse(url)
        x = o.netloc.split('.')
        return x[1]
    elif url[0] == 'w':
        o = urlparse(url)
        x = o.path.split('.')
        return x[1]
    elif url[0] == 'h':
        o = urlparse(url)
        x = o.netloc.split('.')
        return x[0]
    else:
        o =urlparse(url)
        x = o.path.split('.')
        return x[0]

print(domain_name('www.google.com'))
print(domain_name('https://google.com'))
print(domain_name('https://www.cnet.com'))
print(domain_name('icann.org'))

#other solution of this cata
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
    
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]