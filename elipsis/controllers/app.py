from pyramid.view import view_config
from pyramid.Response import response

class App:
    def __init__(self, req):
        self.req = req

    @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
    def my_view(request):
        return {'project': 'elipsis'}
