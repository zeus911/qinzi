# -*- coding: utf-8 -*-
from __future__ import absolute_import

from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group


qinzi_library = Library('qinzi', 'static')
boostrap_css = Resource(
    qinzi_library,
    'css/bootstrap.min.css')
font_css = Resource(
    qinzi_library,
    'css/font-awesome.min.css')
theme_css = Resource(
    qinzi_library,
    'css/bootstrap-theme.css',
    depends=[boostrap_css, font_css])
qinzi_css = Resource(
    qinzi_library,
    'css/main.css',
    depends=[theme_css])

jquery_js = Resource(
    qinzi_library,
    'js/jquery.min.js',
    bottom=True)
bootstrap_js = Resource(
    qinzi_library,
    'js/bootstrap.min.js',
    depends=[jquery_js],
    bottom=True)
headroom_js = Resource(
    qinzi_library,
    'js/headroom.min.js',
    depends=[bootstrap_js],
    bottom=True)
jquery_headroom_js = Resource(
    qinzi_library,
    'js/jQuery.headroom.min.js',
    depends=[headroom_js],
    bottom=True)
qinzi_js = Resource(
    qinzi_library,
    'js/template.js',
    depends=[jquery_js, bootstrap_js,
             headroom_js, jquery_headroom_js],
    bottom=True)


qinzi_needed = Group([qinzi_css, qinzi_js])
