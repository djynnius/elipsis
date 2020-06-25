from pyramid.view import view_config
from pyramid.response import Response as res
from pyramid.httpexceptions import HTTPFound as http

class App:
    res = res
    http = http

    def __init__(self, req):
        self.req = req

    @view_config(route_name='home', renderer='views/app.html')
    def my_view(request):
        return {'project': '...'}

    def db_Connect():
        from ..models.db import DB
        #dbo = DB().sqlite()
        #dbo = DB().maria()
        #dbo = DB().postgres()

        dbo = DB().sqlite()
