from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
	url(r'^$', views.Home.as_view(), name="list"),
	url(r'^login$', views.inicio.as_view(), name="inicio"),
	url(r'^logout/$', djangoViews.logout, name="logout"),
	url(r'^perfil$', views.PerfilView.as_view(), name="perfil"),
]