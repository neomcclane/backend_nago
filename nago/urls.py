from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin

from server import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('server.urls'))
]
