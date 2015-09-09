from django import template
from datetime import date

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
