from django.urls import path
from .views import DemoListView,DemoListView2,DemoListView3
urlpatterns = [
    path('', DemoListView.as_view(), name='home'),
    path('about/', DemoListView2.as_view(), name='about'),
    path('services/', DemoListView3.as_view(), name='services')
]