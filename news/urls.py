from django.urls import path
from .views import DemoListView,DemoListView2,DemoListView3,DemoListView4,DemoListView5
urlpatterns = [
    path('', DemoListView.as_view(), name='home'),
    path('xodim/', DemoListView2.as_view(), name='xodim'),
    path('registr/', DemoListView3.as_view(), name='registr'),
    path('enter/', DemoListView4.as_view(), name='enter'),
    path('vakant/', DemoListView5.as_view(), name='vakant')
]