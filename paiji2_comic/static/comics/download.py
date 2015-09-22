#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

import urllib2
import socket
import tempfile
import feedparser
import os
import re
import pytz
from datetime import datetime
from bs4 import BeautifulSoup as bs


BASE_DIR = os.path.dirname(__file__)

NY_tz = pytz.timezone("America/New_York")
Metz_tz = pytz.timezone("Europe/Paris")

TIMEOUT = 10


def _NY_datetime():
    return datetime.now(NY_tz)


def _Metz_datetime():
    return datetime.now(Metz_tz)


def urlopen(url, timeout=TIMEOUT):
    request = urllib2.Request(url)
    request.add_header(
        'User-Agent',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
    )
    request.add_header('Referer', 'duckduckgo.com')
    request.add_header('DNT', '1')
    request.add_header('Connection', 'keep-alive')
    request.add_header('Cache-Control', 'max-age=0')
    request.add_header(
        'Accept-Language',
        'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    )
    request.add_header(
        'Accept',
        'text/html,application/xhtml+xml,\
            application/xml;q=0.9,*/*;q=0.8',
    )
    return urllib2.urlopen(request, timeout=TIMEOUT)


def parse(url):
    return bs(urlopen(url).read(), 'html.parser')


class Downloader:

    def __init__(self, url_pattern, filename_pattern, tz=NY_tz):
        self.url_pattern = url_pattern
        self.filename_pattern = filename_pattern 
        self.tz = tz

    def get_url(self):
        url = datetime.now(self.tz).strftime(
            self.url_pattern
        )
        return url

    def get_filename(self):
        filename = datetime.now(self.tz).strftime(
            self.filename_pattern
        )
        return filename

    def dl(self):
        print datetime.now()
        with open(self.get_filename(), 'w') as fh:
            try:
                print('downloading ' + self.get_url())
                fh.write(
                    urlopen(self.get_url()).read()
                )
            except Exception as e:
                print('Error : ' + e.message)
                return
            print('saved as ' + self.get_filename())


class GoComicDownloader(Downloader):

    def __init__(self, slug):
        self.slug = slug
        self.tz = NY_tz
        self.filename_pattern = slug + '_%Y-%m-%d'

    def get_url(self):
        http_file = urlopen('http://www.gocomics.com/' + self.slug)
        code = http_file.getcode()
        if code == 200:
            soup = bs(http_file.read(), 'html.parser')
        else:
            raise Exception('return code : ' + code)
        imgs = soup.find_all(
            'img',
            src=re.compile(r"assets\.amuniversal\.com"),
        )
        img_src = unicode(imgs[1]['src'])  # best quality
        return img_src


class APODownloader(Downloader):

    def __init__(self):
        self.filename_pattern = 'apod_%Y-%m-%d'
        self.tz = NY_tz

    def get_url(self):
        url_str = _NY_datetime().strftime('%y%m%d')
        url = 'http://apod.nasa.gov/apod/ap' + url_str + '.html'
        content = parse(url)
        img_url_str = content.img['src']
        return 'http://apod.nasa.gov/apod/' + img_url_str


class MathsDownloader(Downloader):

    def __init__(self):
        self.filename_pattern = 'maths_%Y-%m-%d'
        self.tz = Metz_tz

    def get_url(self):
        url = 'http://images.math.cnrs.fr/'
        content = parse(url)
        img_url_str =\
            content.find(attrs={"class": "block-image"}).img['src']
        return url + img_url_str


class NGDownloader(Downloader):

    def __init__(self):
        self.filename_pattern = 'ng_%Y-%m-%d'
        self.tz = NY_tz

    def get_url(self):
        url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
        content = parse(url)
        img_url_str = content.find(
            attrs={'class':'primary_photo'}
        ).img['src']
        return 'http:' + img_url_str


class EAIOTDownloader(Downloader):

    def __init__(self):
        self.filename_pattern = 'eaiotd_%Y-%m-%d'
        self.tz = NY_tz

    def get_url(self):
        url = 'http://www.earthobservatory.nasa.gov/IOTD/'
        content = parse(url)
        img_url_str = content.find(attrs={'class':'daily-image'}).img['src']
        return img_url_str


class METDownloader(Downloader):
    def __init__(self):
        self.filename_pattern = 'met_%Y-%m-%d'
        self.tz = NY_tz

    def get_url(self):
        rss_url = 'http://www.metmuseum.org/collection/artwork-of-the-day?rss=1'
        entry = feedparser.parse(rss_url).entries[0]
        html_content = parse(entry.link)
        img = html_content.find(attrs={'class': 'image-container'}).img
        img_src = img['src']
        return img_src
    

garfield = {
    'url_pattern': 'http://garfield.com/uploads/strips/%Y-%m-%d.jpg',
    'filename_pattern': 'garfield_%Y-%m-%d',
    'tz': NY_tz,
}

usacres = {
    'url_pattern': 'http://garfield.com/uploads/usacres/usa1988-%m-%d.jpg',
    'filename_pattern': 'usacres_%Y-%m-%d',
    'tz': NY_tz,
}

data = (
    garfield,
    usacres,
)

slugs = (
    'nancy',
    'calvinandhobbes',
    'that-is-priceless',
)


if __name__ == '__main__':

    for d in data:
        print '\n' + d['filename_pattern']
        try:
            Downloader(**d).dl()
        except Exception as e:
            print(
                'Error (' +\
                d['filename_pattern'] +\
                ') : ' +\
                e.message
            )

    for slug in slugs:
        print '\n' + slug
        try:
            GoComicDownloader(slug).dl()
        except Exception as e:
            print('Error (' + slug + ') : ' + e.message)

    print '\n' + 'apod'
    try:
        APODownloader().dl()
    except Exception as e:
        print('Error (apod) : ' + e.message)

    print '\n' + 'maths'
    try:
        MathsDownloader().dl()
    except Exception as e:
        print('Error (maths) : ' + e.message)

    print '\n' + 'NG'
    try:
        NGDownloader().dl()
    except Exception as e:
        print('Error (NG) : ' + e.message)

    print '\n' + 'EOTD'
    try:
        EAIOTDownloader().dl()
    except Exception as e:
        print('Error (EOTD) : ' + e.message)

    print '\n' + 'Met Artwork'
    try:
        METDownloader().dl()
    except Exception as e:
        print('Error (Met Artwork) : ' + e.message)
