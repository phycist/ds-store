from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='loja-home'),
    path('sobre/', views.sobre, name='loja-sobre'),
    path('produtos/masculino',views.masculino, name="loja-masculino"),
    path("produtos/feminino",views.feminino, name="loja-feminino") 
]


