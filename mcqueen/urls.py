from django.urls import path
from.import views

urlpatterns = [
    path('favas',views.test,name='AMG'),
    path('head',views.head,name='RE'),
    path('mc',views.mc,name='porche'),
]