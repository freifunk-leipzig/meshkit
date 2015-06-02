from gluon.storage import Storage
settings = Storage()

migrate = False
fake_migrate = False

app_mode = "development"
if app_mode == "development":
    # enable reloading of modules when their code was modified
    from gluon.custom_import import track_changes
    track_changes(True)
    # migration settings
    migrate=True
    #fake_migrate=True
    #fake_migrate_all=True
else:
    # process js and css files
    response.optimize_css = 'concat,minify'
    response.optimize_js = 'concat,minify'

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
settings.email_server = 'localhost'
settings.email_sender = 'noreply@meshkit.freifunk.net'
settings.email_tls = False
settings.email_login = None
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

response.title = settings.title
response.subtitle = settings.subtitle


