from pyramid.config import Configurator

from .site import Site
from .views import www

def main(global_config, **settings):
    config = Configurator(settings=settings, root_factory=Site.root_factory)
    config.include('substanced')
    config.add_route('languages', '/language/{name}')
    config.add_view(www, context='pyramid.httpexceptions.HTTPNotFound')
    config.scan('hugitout')
    return config.make_wsgi_app()

