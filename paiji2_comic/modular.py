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
    app_name = 'APOD'
    name = 'APOD'
    urls = None
    templatetag_blocks = [
        TemplateTagBlock(
            name='APOD',
            library='comic',
            tag='get_apod',
            cache_time=60 * 60,
        ),
    ]
modules.register(APODModule)
