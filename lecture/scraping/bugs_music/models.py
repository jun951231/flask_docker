from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse


class BugsMusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _ = 0
        artists = soup.find_all(name='p', attrs={'class':'artist'})
        titles = soup.find_all(name='p', attrs={'class':'title'})
        print(f'List size is {len(artists)}')
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist : {i.find('a').text},  Title : {j.find('a').text}" )
