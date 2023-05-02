from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'pages/index.html', context)