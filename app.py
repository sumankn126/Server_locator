##################################
######### Server Locator #########
###### Author: suman kn ##########
###email: skn@ysnc-socio.in#######
##################################

#importing modules 
from IP_finder import ip_finder
from LAT_LONG_finder import lat_long_finder
from GMAP_locator import gmap
import os


#main function
def main():
    os.system('clear')
    print('\n!!!...Welcome to Server Locator...!!!\n')
    #loading the IP address from user interface
    IP_or_URL =int(input('Enter your option:\n 1 for Domain Name\n 2 for IP\n Any to exit\n: '))
    if IP_or_URL is 1:
        IP_Addr = ip_finder()
    elif IP_or_URL is 2:
        IP_Addr = input('Enter the Correct IP Address : ')
    else:
        print('....Thank You....Visit Again!!!')
        exit(0)
    #Getting the GeoLocation from IP Address
    latitude,longitude=lat_long_finder(IP_Addr)
    geolocation = f'{latitude} {longitude}'
    #Opening gmaps on browser to locate the server Location
    gmap(geolocation) 
    print('\n...Thank You.....Visit Again..!!!\n')


if __name__=='__main__':
    main()
