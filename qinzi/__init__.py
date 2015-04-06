import pkg_resources

from pyramid.config import Configurator
from pyramid.threadlocal import get_current_registry
from pyramid.util import DottedNameResolver


conf_defaults = {
    'qinzi.fanstatic.qinzi_needed': 'qinzi.fanstatic.qinzi_needed'
}


conf_dotted = set([
    'qinzi.fanstatic.qinzi_needed',
])


def _resolve_dotted(d, keys=conf_dotted):
    resolved = d.copy()

    for key in keys:
        value = resolved[key]
        if not isinstance(value, basestring):
            continue

        new_value = []
        for dottedname in value.split():
            new_value.append(DottedNameResolver(None).resolve(dottedname))
        resolved[key] = new_value

    return resolved


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    # config global settings
    for k, v in conf_defaults.items():
        settings.setdefault(k, v)
    settings = _resolve_dotted(settings)

    config = Configurator(settings=settings)
    
    # add '.html' extension for chameleon
    config.add_renderer('.html', 'pyramid_chameleon.zpt.renderer_factory')

    config.add_static_view(name='static', path='static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('signin', '/signin')
    config.scan('.views')
    return config.make_wsgi_app()


def get_version():
    return pkg_resources.require('qinzi')[0].version


def get_settings():
    return get_current_registry().settings
