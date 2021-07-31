from bs4 import BeautifulSoup
from asyncio import get_event_loop
import re

from codewars.logger import Logger
from codewars.surf import Surfer


class Scraper(object):
    """Scrape website pages and return the results with this class."""
    def __init__(self, debug: bool = False):
        """
        Parameters
        ----------
        debug
            Default: False
            Type: bool
            Description: When debug is `True` all the links will be redirected
            to console.
        """
        if debug: self.__logger = Logger('Scraper', 'DEBUG')
        self.__debug = debug
        self.__surf = Surfer(get_event_loop())

    def hrefs(self, url: str = None):
        """ Scrape a url for more urls :D

        Parameters
        ----------
        url
            Default: None
            Type: String
            Description: The url to scrape.

        Returns
        -------
        List
            Type: List
            Content: String
            Description: All the endpoints found while scraping
            Returns a empty list if nothing was found.
        """
        if url is None: raise AttributeError("No url provided to scrape")
        response = self.__surf.get(url)
        if response[0] == 200:
            data = response[1].decode()
            soup = BeautifulSoup(data, 'lxml')
            list1 = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("^(http|https|/|)://")})]
            list2 = re.findall(r'(?<=<a href=")[^"]*', data)
            for link in list2: list1.append(link)
            if self.__debug:
                for item in list(set(list1)): self.__logger.debug(f"Found: {item}")
            return list(set(list1))
        else: return []