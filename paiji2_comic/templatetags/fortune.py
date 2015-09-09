from django import template
import os


register = template.Library()

@register.inclusion_tag(
    'comic/fortune_block.html',
)
def get_fortune():
    try:
        fortune = unicode(os.popen('fortune').read())
    except:
        fortune = u'Were they afraid that "e" being the most widely used letter in\nthe English language was going to war out thir xpnsiv kyboards if\nthy usd it all th tim?\n\n\t- Mike A. Harris on linux-kernel\n'
        print("fortune : error reading `fortune` command")

    return { 'fortune': fortune }
