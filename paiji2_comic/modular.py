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
            cache_time=60 * 60,
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
            cache_time=60 * 60,
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
            name = 'National Geographic Photo of the Day',
            library='comic',
            tag='get_ng',
            cache_time=60*60,
        ),
    ]


modules.register(NGModule)
