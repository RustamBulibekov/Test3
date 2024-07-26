from django.urls import path, include
from.views import index, index2,index3

urlpatterns = [

    path('', index, name='index'),
    path('index2/', index2, name='index2'),
    path('index3/', index3, name='index3')
]