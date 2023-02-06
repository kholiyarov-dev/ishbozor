from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment
import datetime
# Create your views here.

class DemoListView(ListView):
    model = Post
    template_name = 'home.html'

class DemoListView2(ListView):
    model = Post
    template_name = 'xodim.html'

class DemoListView3(ListView):
    model = Post
    template_name = 'registr.html'

class DemoListView4(ListView):
    model = Post
    template_name = 'enter.html'
