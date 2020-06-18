from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)


    config.include('pyramid_jinja2')
    config.add_static_view('assets', 'assets', cache_max_age=3600)
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')

    #routes
    config.add_route('home', '/')


    config.scan()
    return config.make_wsgi_app()
