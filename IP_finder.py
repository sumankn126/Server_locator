# finding the ip address
import socket
from urllib.parse import urlparse

def ip_finder():
    url=input('\nEnter the url for IP tracing:')
    domname = urlparse(url)
    if domname.netloc is '':
        IP_Addr = socket.gethostbyname(domname.path)
        print('\nRouting for IP address of : ',domname.path)
    else:
        IP_Addr = socket.gethostbyname(domname.netloc)
        print('\nRouting for IP address of : ',domname.netloc)
    print('\nIP Address is : ',IP_Addr)
    return IP_Addr

