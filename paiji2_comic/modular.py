from modular_blocks import ModuleApp, TemplateTagBlock, modules


class GarfieldComicModule(ModuleApp):
    app_name = 'garfield-comic'
    name = 'garfield-comic'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='garfield-comic',
            library='comic',
            tag='get_garfield',
            cache_time=60 * 60,
        ),
    ]


modules.register(GarfieldComicModule)


class USAcresComicModule(ModuleApp):
    app_name = 'us-acres-comic'
    name = 'us-acres-comic'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='us-acres-comic',
            library='comic',
            tag='get_us_acres',
            cache_time=60 * 60,
        ),
    ]


modules.register(USAcresComicModule)


class CalvinAndHobbesComicModule(ModuleApp):
    app_name = 'calvin-and-hobbes-comic'
    name = 'calvin-and-hobbes-comic'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='calvin-and-hobbes-comic',
            library='comic',
            tag='get_calvin_and_hobbes',
            cache_time=3 * 60 * 60,
        ),
    ]


modules.register(CalvinAndHobbesComicModule)


class NancyComicModule(ModuleApp):
    app_name = 'nancy-comic'
    name = 'nancy-comic'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='nancy-comic',
            library='comic',
            tag='get_nancy',
            cache_time=3 * 60 * 60,
        ),
    ]


modules.register(NancyComicModule)


class BijinTokeiModule(ModuleApp):
    app_name = 'bijin-tokei'
    name = 'bijin-tokei'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='bijin-tokei',
            library='comic',
            tag='get_tokei',
            cache_time=30,
        ),
    ]


modules.register(BijinTokeiModule)


class APODModule(ModuleApp):
    app_name = 'Astronomical Picture Of the Day'
    name = 'Astronomical Picture Of the Day'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Astronomical Picture Of the Day',
            library='comic',
            tag='get_apod',
            cache_time=2 * 60 * 60,
        ),
    ]


modules.register(APODModule)


class MathImgModule(ModuleApp):
    app_name = 'Image des Maths'
    name = 'Image des Maths'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Image des Maths',
            library='comic',
            tag='get_math_image',
            cache_time=2 * 60 * 60,
        ),
    ]


modules.register(MathImgModule)


class FortuneModule(ModuleApp):
    app_name = 'Fortune'
    name = 'Fortune'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Fortune',
            library='fortune',
            tag='get_fortune',
            cache_time=5,
        ),
    ]


modules.register(FortuneModule)


class NGModule(ModuleApp):
    app_name = 'National Geographic Photo of the Day'
    name = 'National Geographic Photo of the Day'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='National Geographic Photo of the Day',
            library='comic',
            tag='get_ng',
            cache_time=2 * 60 * 60,
        ),
    ]


modules.register(NGModule)


class EAModule(ModuleApp):
    app_name = 'Earth Observatory Image of the Day'
    name = 'Earth Observatory Image of the Day'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Earth Observatory Image of the Day',
            library='comic',
            tag='get_eaiotd',
            cache_time=2 * 60 * 60,
        ),
    ]


modules.register(EAModule)


class MetArtworkModule(ModuleApp):
    app_name = 'Artwork of the day'
    name = 'Artwork of the day'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Artwork of the day',
            library='comic',
            tag='get_met_artwork',
            cache_time=60*60,
        ),
    ]


modules.register(MetArtworkModule)


class LittreModule(ModuleApp):
    app_name = 'Littre definition'
    name = 'Littre definition'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Littre definition',
            library='fortune',
            tag='get_littre',
            cache_time=5,
        ),
    ]


modules.register(LittreModule)


class SaintModule(ModuleApp):
    app_name = 'Saint du jour'
    name = 'Saint du jour'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Saint du jour',
            library='fortune',
            tag='get_saint',
            cache_time=60*60,
        ),
    ]


modules.register(SaintModule)
