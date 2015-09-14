import urllib2
import socket
import feedparser
import pytz
import subprocess
import os
import re
from django import template
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from bs4 import BeautifulSoup


TIMEOUT = 1.5
BASE_DIR = os.path.dirname(__file__)
geturl = os.path.join(BASE_DIR, 'geturl.pl')

register = template.Library()


def _NY_datetime():
    NY_tz = pytz.timezone("America/New_York")
    return NY_tz.normalize(timezone.now())


def _local_datetime():
    return timezone.localtime(timezone.now())


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_garfield():
    today_str = _NY_datetime().strftime('%Y-%m-%d')
    return {
        'img_src':
            'http://garfield.com/uploads/strips/' + today_str + '.jpg',
        'img_alt': 'Garfield comic',
        'legend': 'Garfield',
        'legend_url': 'http://garfield.com/comic/' + today_str,
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_us_acres():
    today_str = _NY_datetime().strftime('%Y-%m-%d')
    url_str = _NY_datetime().strftime('usa1988-%m-%d')
    return {
        'img_src':
            'http://garfield.com/uploads/usacres/' + url_str + '.jpg',
        'img_alt': 'U.S. Acres comic',
        'legend': 'U.S. Acres',
        'legend_url': 'http://garfield.com/us-acres/' + today_str,
    }


def get_gocomic(slug, name):

    legend_url = 'http://www.gocomics.com/' + slug

    try:

        # img_src = subprocess.check_output([geturl] + [slug])
        # (upper was the perl WWW::Mechanize solution)

        request = urllib2.Request(legend_url)

        # 403 error if you are a robot...
        # so we simulate a real browser
        request.add_header(
            'User-Agent',
            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
        )
        request.add_header('Referer', 'www.gocomics.com')
        request.add_header('Host', 'www.gocomics.com')
        request.add_header('DNT', '1')
        request.add_header('Connection', 'keep-alive')
        request.add_header('Cache-Control', 'max-age=0')
        request.add_header(
            'Accept-Language',
            'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        )
        # request.add_header('Accept-Encoding', 'gzip, deflate')
        # we do not want gzipped data
        request.add_header('Accept-Encoding', 'deflate')
        request.add_header(
            'Accept',
            'text/html,application/xhtml+xml,\
            application/xml;q=0.9,*/*;q=0.8',
        )
    
        http_file = urllib2.urlopen(
            request,
            timeout=TIMEOUT,
        )

        code = http_file.getcode()

        if code == 200:
            soup = BeautifulSoup(
                http_file.read(),
                'html.parser',
            )
        else:
            raise Exception(
                'return code : ' + code
            )

        imgs = soup.find_all('img', src=re.compile(r"assets\.amuniversal\.com"),)
        img_src = unicode(imgs[1]['src'])  # second picture : best quality

    except Exception as e:

        img_src = settings.STATIC_URL + 'comics/' + slug
        print('get_gocomic error : ' + e.message)

    return {
        'img_src': img_src,
        'img_alt': name,
        'legend': name,
        'legend_url': legend_url,
    }


@register.inclusion_tag('comic/comic_block.html')
def get_calvin_and_hobbes():
    return get_gocomic('calvinandhobbes', 'Calvin and Hobbes')


@register.inclusion_tag('comic/comic_block.html')
def get_nancy():
    return get_gocomic('nancy', 'Nancy')


@register.inclusion_tag('comic/comic_block.html')
def get_that_is_priceless():
    return get_gocomic('that-is-priceless', 'That is priceless')


@register.inclusion_tag('comic/tokei.html')
def get_tokei():
    # for those who do not have javascript enabled/installed
    url_str = _local_datetime().strftime('%H%M')
    return {
        'img_src':
                'http://www.bijint.com/assets/pict/jp/pc/' +\
                 url_str + '.jpg',
        'img_alt': url_str,
        'legend': 'bijin tokei',
        'legend_url': 'http://www.bijint.com/jp/'
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_apod():
    url_str = _NY_datetime().strftime('%y%m%d')
    url = 'http://apod.nasa.gov/apod/ap' + url_str + '.html'

    try:
        content = BeautifulSoup(urllib2.urlopen(url, timeout=TIMEOUT).read(), 'html.parser')
    except socket.timeout:
        print("apod fetcher timed out")
        return dict()
    except urllib2.URLError:
        print("apod : url failed")
        return dict()

    try:
        img_url_str = content.img['src']
    except:
        print("apod img url : bad html")
        return dict()

    try:
        img_legend = unicode(content.b.string)
    except:
        print("apod img legend : bad html")
        img_legend = 'Astronomical Picture Of the Day',

    return {
        'img_src': 'http://apod.nasa.gov/apod/' + img_url_str,
        'img_alt': img_legend,
        'legend': img_legend,
        'legend_url': url,
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_math_image():
    url = 'http://images.math.cnrs.fr/'

    try:
        content = BeautifulSoup(urllib2.urlopen(url, timeout=TIMEOUT).read(), 'html.parser')
    except socket.timeout:
        print("math img fetcher timed out")
        return dict()
    except urllib2.URLError:
        print("math img : url failed")
        return dict()

    try:
        img_url_str = content.find(attrs={"class": "block-image"}).img['src']
    except:
        print("math  img url : bad html")
        return dict()

    try:
        legend_url = url + content.find(attrs={"class": "block-image"}).a['href']
    except:
        print("math legend url : bad html")
        legend_url = url

    return {
        'img_src': url + img_url_str,
        'img_alt': 'Image des maths du jour',
        'legend': "L'image des maths du jour",
        'legend_url': legend_url,
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_ng():
    url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'

    try:
        content = BeautifulSoup(urllib2.urlopen(url, timeout=TIMEOUT).read(), 'html.parser')
    except socket.timeout:
        print("NG fetcher timed out")
        return dict()
    except urllib2.URLError:
        print("NG : url failed")
        return dict()

    try:
        img_url_str = content.find(attrs={'class':'primary_photo'}).img['src']
    except:
        print("NG img url : bad html")
        return dict()

    try:
        img_legend = content.find(attrs={'class':'primary_photo'}).img['alt']
    except:
        print("apod img legend : bad html")
        img_legend = 'National Geographic Photo Of The Day'

    return {
        'img_src': 'http:' + img_url_str,
        'img_alt': img_legend,
        'legend': img_legend,
        'legend_url': url,
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_eaiotd():
    url = 'http://www.earthobservatory.nasa.gov/IOTD/'

    try:
        content = BeautifulSoup(urllib2.urlopen(url, timeout=TIMEOUT).read(), 'html.parser')
    except socket.timeout:
        print("eaiotd fetcher timed out")
        return dict()
    except urllib2.URLError:
        print("eaiotd : url failed")
        return dict()

    try:
        img_url_str = content.find(attrs={'class':'daily-image'}).img['src']
    except:
        print("eaiotd img url : bad html")
        return dict()

    try:
        img_legend = content.find(attrs={'class':'daily-image'}).img['alt']
    except:
        print("eaiotd img legend : bad html")
        img_legend = 'Earth Observatory Image Of The Day'

    return {
        'img_src': img_url_str,
        'img_alt': img_legend,
        'legend': img_legend,
        'legend_url': url,
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_met_artwork():
    rss_url = 'http://www.metmuseum.org/collection/artwork-of-the-day?rss=1'
    try:
        entry = feedparser.parse(rss_url).entries[0]
        description = entry.description
        title = entry.title
        link = entry.link
        html_content = BeautifulSoup(urllib2.urlopen(link, timeout=TIMEOUT).read())
        img = html_content.find(attrs={'class': 'image-container'}).img
        img_src = img['src']
        img_alt = img['alt']
    except Exception as e:
        print("met artwork : unable to parse the feed")
        print("met artwork : " + e.message)
        return dict()
    
    return {
        'img_src': img_src,
        'img_alt': img_alt,
        'legend': title,
        'legend_url': link,
    }
