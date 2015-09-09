from django import template
from datetime import date
from django.utils import timezone
from bs4 import BeautifulSoup
import urllib2
import socket

register = template.Library()


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_garfield():
    today_str = date.today().strftime('%Y-%m-%d')
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
    today_str = date.today().strftime('%Y-%m-%d')
    url_str = date.today().strftime('usa1988-%m-%d')
    return {
        'img_src':
            'http://garfield.com/uploads/usacres/' + url_str + '.jpg',
        'img_alt': 'U.S. Acres comic',
        'legend': 'U.S. Acres',
        'legend_url': 'http://garfield.com/us-acres/' + today_str,
    }

@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_tokei():
    url_str = timezone.localtime(timezone.now()).strftime('%H%M')
    return {
        'img_src':
                'http://www.bijint.com/assets/pict/jp/pc/' + url_str + '.jpg',
        'img_alt': url_str,
        'legend': 'bijin tokei',
        'legend_url': 'http://www.bijint.com/jp/'
    }

@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_apod():
    url_str = date.today().strftime('%y%m%d')
    url = 'http://apod.nasa.gov/apod/ap' + url_str + '.html'

    try:
        content = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
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
        print("apod img legend : bad html")
        img_legend = 'Astronomical Picture Of the Day',

    return {
        'img_src': 'http://apod.nasa.gov/apod/' + img_url_str,
        'img_alt': img_legend,
        'legend': img_legend,
        'legend_url': url,
    }
