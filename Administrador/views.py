from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class Panel(ListView):
    def get(self, request):
        template_name = "Administrador/panel.html"
        context = {}
        return render(request, template_name, context)
	