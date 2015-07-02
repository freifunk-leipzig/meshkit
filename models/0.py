#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon.storage import Storage
from gluon import current
settings = Storage()

migrate = True
fake_migrate = False
fake_migrate_all = False

settings.migrate = migrate
# use fake_migrate to repair broken tables
settings.fake_migrate = fake_migrate
settings.title = 'Meshkit'
settings.subtitle = 'Freifunk OpenWrt Imagebuilder'
settings.author = 'soma'
settings.author_email = 'freifunk@somakoma.de'
settings.keywords = 'Freifunk,Mesh,Wireless,Wifi,OpenWrt,Imagebuilder'
settings.description = 'This imagebuilder will build firmware images for Freifunk or similar wireless mesh networks. The firmware images are preconfigured and ready to mesh out of the box.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'c50bdbb8-ada2-4398-80da-c00f555acdde'
settings.email_server = '127.0.0.1'
settings.email_sender = 'noreply@meshkit.freifunk.net'
settings.email_tls = False
settings.email_login = None
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
settings.ui_grid = dict(
    widget='',
    header='',
    content='',
    default='',
    cornerall='',
    cornertop='',
    cornerbottom='',
    button='btn btn-default',
    buttontext='',
    buttonadd='icon-plus big',
    buttonback='icon-left big',
    buttonexport='icon-down big',
    buttondelete='icon-trash big',
    buttonedit='icon-pencil big',
    buttontable='icon-right big',
    buttonview='icon-eye big'
)

settings.scheduler = dict(
    heartbeat=2,
    timeout=120,
    retry_failed=0
)

# save settings to current, so we can use it in modules
current.settings = settings

response.title = settings.title
response.subtitle = settings.subtitle
