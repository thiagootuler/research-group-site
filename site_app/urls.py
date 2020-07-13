from django.urls import path
from site_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('artigo/', views.artigo, name='artigo'),
    path('membros/', views.membros, name='membros'),
    path('contato/', views.contato, name='contato'),
]
