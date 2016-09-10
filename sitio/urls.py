from django.conf.urls import url,include
from django.contrib import admin
from Administrador import urls as AdministradorUrls
from Principal import urls as PrincipalUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(AdministradorUrls)),
    url(r'^',include(PrincipalUrls)),
]
