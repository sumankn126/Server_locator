#accessing the latitude and longitude of the ip address
import requests
from bs4 import BeautifulSoup


url = 'https://www.iplocation.net/'


def lat_long_finder(IP_Addr):
    print('\nFetching IP address:',IP_Addr)
    payload = { 'query' : IP_Addr }
    page = requests.get(url, params=payload)  
    soup = BeautifulSoup(page.text, 'html.parser')
    tbody = soup.find_all('tbody')[1]
    latitude = tbody.find_all('td')[2].decode_contents()
    longitude = tbody.find_all('td')[3].decode_contents()
    print(f'\nFound GeoLocation of server is:\n latitude: {latitude}, longitude: {longitude}')
    return latitude,longitude


