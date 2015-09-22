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


BASE_DIR = os.path.dirname(__file__)

register = template.Library()

NY_tz = pytz.timezone("America/New_York")
Metz_tz = pytz.timezone("Europe/Paris")


def format(slug, tz=Metz_tz):
    return slug + '_' + datetime.now(tz).strftime('%Y-%m-%d')


def get_url(slug, tz=Metz_tz):
    return settings.STATIC_URL + 'comics/' + format(slug, tz)


@register.inclusion_tag('comic/comic_block.html')
def get_garfield():
    return {
        'img_src': get_url('garfield', NY_tz),
        'img_alt': 'Garfield strip',
        'legend': 'Garfield',
        'legend_url': 'http://garfield.com/',
    }


@register.inclusion_tag('comic/comic_block.html')
def get_us_acres():
    return {
        'img_src': get_url('usacres', NY_tz),
        'img_alt': 'U.S. Acres strip',
        'legend': 'U.S. Acres',
        'legend_url': 'http://garfield.com/us-acres/',
    }


def get_gocomic(slug, name):
    return {
        'img_src': get_url(slug, NY_tz),
        'img_alt': name + ' strip',
        'legend': name,
        'legend_url': 'http://www.gocomics.com/' + slug,
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
    url_str = datetime.now(Metz_tz).strftime('%H%M')
    return {
        'img_src':
                'http://www.bijint.com/assets/pict/jp/pc/' +\
                 url_str + '.jpg',
        'img_alt': url_str,
        'legend': 'bijin tokei',
        'legend_url': 'http://www.bijint.com/jp/'
    }


@register.inclusion_tag('comic/comic_block.html')
def get_apod():
    return {
        'img_src': get_url('apod', NY_tz),
        'img_alt': 'Astronomical Picture Of the Day',
        'legend': 'Astronomical Picture Of the Day',
        'legend_url': 'http://apod.nasa.gov',
    }


@register.inclusion_tag('comic/comic_block.html')
def get_math_image():
    return {
        'img_src': get_url('maths', Metz_tz),
        'img_alt': 'Image des maths du jour',
        'legend': "L'image des maths du jour",
        'legend_url': 'http://images.math.cnrs.fr/',
    }


@register.inclusion_tag(
    'comic/comic_block.html',
)
def get_ng():
    return {
        'img_src': get_url('ng', NY_tz),
        'img_alt': 'National Geographic Photo of the Day',
        'legend': 'National Geographic Photo of the Day',
        'legend_url': 'http://photography.nationalgeographic.com/photography/photo-of-the-day/',
    }


@register.inclusion_tag('comic/comic_block.html')
def get_eaiotd():
    return {
        'img_src': get_url('eaiotd', NY_tz),
        'img_alt': 'Earth Observatory Image Of the Day',
        'legend': 'Earth Observatory Image Of the Day',
        'legend_url': 'http://www.earthobservatory.nasa.gov/IOTD/',
    }


@register.inclusion_tag('comic/comic_block.html')
def get_met_artwork():
    return {
        'img_src': get_url('met', NY_tz),
        'img_alt': 'Met Artwork of the Day',
        'legend': 'Met Artwork of the Day',
        'legend_url': 'http://www.metmuseum.org/collection/artwork-of-the-day',
    }
