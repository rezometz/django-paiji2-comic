from django import template
from datetime import date
from django.utils import timezone

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
