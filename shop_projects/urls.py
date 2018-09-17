from django.contrib import admin
from django.conf.urls import url,include
from APPS.home import urls
urlpatterns = [
    url('admin/', admin.site.urls),
    url('1/',include(urls)),
]
