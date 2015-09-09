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
