# finding the ip address
import socket


def ip_finder():
    url=input('\nEnter the url for IP tracing:')
    print('\nRouting for IP address of : ',url)
    print('\nIP Address is : ')
    IP_Addr = socket.gethostbyname(url)
    print(IP_Addr)
    return IP_Addr

