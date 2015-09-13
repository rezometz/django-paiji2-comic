from django import template
from django.conf import settings
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import os
import feedparser
from django.template.defaultfilters import urlencode


TIMEOUT = 1


register = template.Library()


@register.inclusion_tag(
    'comic/fortune_block.html',
)
def get_fortune():
    try:

        try:
            fortune_bin = settings.FORTUNE_PATH
        except Exception as e:
            print("settings.FORTUNE_PATH : error")
            print("settings.FORTUNE_PATH : " + e.message)
            fortune_bin = '/usr/games/fortune'

        fortune = unicode(os.popen(fortune_bin).read())

    except Exception as e:

        fortune = u'Were they afraid that "e" being the most widely used letter in\nthe English language was going to war out thir xpnsiv kyboards if\nthy usd it all th tim?\n\n\t- Mike A. Harris on linux-kernel\n'
        print("fortune : error reading `fortune` command")
        print("fortune : exception :" + e.message)

    return {'fortune': fortune}


@register.inclusion_tag(
    'comic/littre_block.html',
)
def get_littre():
    url = 'http://www.littre.org/recherche'
    try:
        content = bs(urlopen(url, timeout=TIMEOUT).read())
        definition = unicode(content.find(
            'section',
             attrs={'class': 'definition'},
        ))
        vedette = urlencode(unicode(
            content.find(
                'span',
                attrs={'class': 'actif'},
            ).string
        ))
        link = 'http://www.littre.org/definition/' + vedette
    except Exception as e:
        print("get_littre : " + e.message)
        return dict()

    return {'link': link, 'definition': definition}


def get_feed(name, url, nb):
    try:
        entries = feedparser.parse(url).entries
    except Exception as e:
        print(name + " feed block : unable to parse the feed")
        print(name + " feed block : " + e.message)
        return dict()
    return {
        'title': name,
        'entries': entries[:nb],
    }


@register.inclusion_tag('comic/feed_block.html')
def get_saint():
    return get_feed(
        name='Saintes et Saints du jour',
        url='http://nominis.cef.fr/rss/nominis.php',
        nb=1,
    )


@register.inclusion_tag('comic/feed_block.html')
def get_h16():
    return get_feed(
        name='Hashtable',
        url='http://h16free.com/feed',
        nb=3,
    )

@register.inclusion_tag('comic/feed_block.html')
def get_supelec():
    return get_feed(
        name='Supélec',
        url='http://www.supelec.fr/rss_actu_428.xml',
        nb=5,
    )

@register.inclusion_tag('comic/feed_block.html')
def get_metz():
    return get_feed(
        name='Metz',
        url='http://metz.fr/rss.php',
        nb=5,
    )

@register.inclusion_tag('comic/feed_block.html')
def get_opera():
    return get_feed(
        name='Opera',
        url='http://opera.metzmetropole.fr/site/_rss_agenda.php',
        nb=5,
    )

@register.inclusion_tag('comic/feed_block.html')
def get_arsenal():
    return get_feed(
        name='Arsenal',
        url='http://arsenal-metz.fr/fr/flux-rss-agendas-arsenal.rss',
        nb=2,
    )
