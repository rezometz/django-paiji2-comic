from django import template
from django.conf import settings
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import os


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
        content = bs(urlopen(url).read())
        definition = unicode(content.find(
            'section',
             attrs={'class': 'definition'},
        ))
    except Exception as e:
        print("get_littre : " + e.message)
        return dict()

    return {'definition': definition}
