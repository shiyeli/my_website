from base import *



DEBUG=False
#You must set settings.ALLOWED_HOSTS if DEBUG is False.
ALLOWED_HOSTS = ['*']

HOST='http://23.106.145.39:8000'

#when diploy nginx server , we need collect all django's static files
STATIC_ROOT = '/root/my_website_server/static'

MEDIA_ROOT='/root/my_website_server/upload_assets'

IMAGE_CACHE_ROOT='/root/my_website_server/upload_assets'