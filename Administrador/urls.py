from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^Administrador$', views.Panel.as_view(), name="list"),
]