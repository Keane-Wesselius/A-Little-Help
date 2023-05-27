from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}


#Grabs the first youtube video link from a google search of the query
def getYoutubeVideo(query):
    #make the url to search for google for a youtube video
    url = 'https://google.com/search?q=' + query + " youtube"

    #grabs the actual webpage from the interwebs
    page=requests.get( url, headers=headers )
    #Grabs the html out of the page
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all("a"):
        href = link.get('href')
        if href and "www.youtube.com/watch?" in href:
            return href
    return None
        
