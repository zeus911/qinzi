from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # add '.html' extension for chameleon
    config.add_renderer('.html', 'pyramid_chameleon.zpt.renderer_factory')

    config.add_static_view(name='static', path='static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
