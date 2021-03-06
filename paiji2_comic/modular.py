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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
        ),
    ]


modules.register(NancyComicModule)


class ThatIsPricelessModule(ModuleApp):
    app_name = 'That is priceless'
    name = 'That is priceless'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='That is priceless',
            library='comic',
            tag='get_that_is_priceless',
            cache_time=5,
            personal=False,
        ),
    ]


modules.register(ThatIsPricelessModule)


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
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=30 + 3,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=5,
            personal=False,
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
            cache_time=10 * 60 + 7,
            personal=False,
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
            cache_time=2 * 60 * 60 + 66,
            personal=False,
        ),
    ]


modules.register(SaintModule)


class H16Module(ModuleApp):
    app_name = 'Hashtable'
    name = 'Hashtable'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Hashtable',
            library='fortune',
            tag='get_h16',
            cache_time=30 * 60,
            personal=False,
        ),
    ]


modules.register(H16Module)


class SupelecModule(ModuleApp):
    app_name = 'Supelec'
    name = 'Supelec'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Supelec',
            library='fortune',
            tag='get_supelec',
            cache_time=2 * 60 * 60 - 100,
            personal=False,
        ),
    ]


modules.register(SupelecModule)


class MetzModule(ModuleApp):
    app_name = 'Metz'
    name = 'Metz',
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Metz',
            library='fortune',
            tag='get_metz',
            cache_time=2 * 60 * 60 - 47,
            personal=False,
        ),
    ]


modules.register(MetzModule)


class OperaModule(ModuleApp):
    app_name = 'Opera',
    name = 'Opera',
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Opera',
            library='fortune',
            tag='get_opera',
            cache_time=2 * 60 * 60 + 10,
            personal=False,
        ),
    ]


modules.register(OperaModule)


class ArsenalModule(ModuleApp):
    app_name = 'Arsenal',
    name = 'Arsenal',
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='Arsenal',
            library='fortune',
            tag='get_arsenal',
            cache_time=2 * 60 * 60 + 87,
            personal=False,
        ),
    ]


modules.register(ArsenalModule)
