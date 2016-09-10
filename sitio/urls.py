from django.conf.urls import url,include
from django.contrib import admin
from Administrador import urls as AdministradorUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(AdministradorUrls)),
]
