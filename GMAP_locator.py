#Displaying the location on the web browser
import webbrowser

url = 'https://www.google.com/maps/place/'

def gmap(geolocation):
    print('Press Enter to open the maps:')
    input() 
    webbrowser.open_new_tab(url +  geolocation )
    print('\n\nBrowser opened and server location is pointed ...!!!\n')



