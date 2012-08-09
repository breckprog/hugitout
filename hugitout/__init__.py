from pyramid.config import Configurator
from hugitout.views import www

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('languages', '/language/{name}')
    config.add_view(www, context='pyramid.httpexceptions.HTTPNotFound')
    config.scan('hugitout')
    return config.make_wsgi_app()

