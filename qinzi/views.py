# -*- coding: utf-8 -*-

from pyramid.renderers import get_renderer
from pyramid.view import view_config
from pyramid.decorator import reify

from qinzi import get_settings


class BaseView(object):
    @reify
    def S(self):
        return get_settings()

    @reify
    def needed(self):
        if 'qinzi.fanstatic.qinzi_needed' in self.S:
            return self.S['qinzi.fanstatic.qinzi_needed'][0].need()

    @reify
    def layout(self):
        renderer = get_renderer('templates/layout.html')
        return renderer.implementation().macros['main']


@view_config(route_name='home', renderer='templates/index.html')
class HomeView(BaseView):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        return {'project': 'qinzi'}


@view_config(route_name='about', renderer='templates/about.html')
class AboutView(BaseView):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        return {'project': 'qinzi'}


@view_config(route_name='signin', renderer='templates/signin.html')
class SignInView(BaseView):
    def __init__(self, request):
        self.request = request

    def __call__(self):
        return {'project': 'qinzi'}
