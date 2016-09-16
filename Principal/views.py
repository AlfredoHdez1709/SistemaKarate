from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class Home(ListView):
    def get(self, request):
        template_name = "Principal/home.html"
        context = {}
        return render(request, template_name, context)


class inicio(ListView):
    def get(self, request):
        template_name = "accounts/login.html"
        context = {}
        return render(request, template_name, context)

        
class PerfilView(ListView):
    def get(self, request):
        template_name= "accounts/perfil.html"
        context = {}
        return render(request, template_name, context)

# Create your views here.
