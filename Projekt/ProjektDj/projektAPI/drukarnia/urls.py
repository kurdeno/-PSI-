from django.urls import path

from . import views

urlpatterns = [
    path('klienci', views.KlientList.as_view(), name=views.KlientList.name),
    path('klienci/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('pracownicy', views.PracownikList.as_view(), name=views.PracownikList.name),
    path('pracownicy/<int:pk>', views.PracownikDetail.as_view(), name=views.PracownikDetail.name),
    path('zamowienia', views.ZamowienieList.as_view(), name=views.ZamowienieList.name),
    path('zamowienia/<int:pk>', views.ZamowienieDetail.as_view(), name=views.ZamowienieDetail.name),
    path('produkty', views.ProduktList.as_view(), name=views.ProduktList.name),
    path('produkty/<int:pk>', views.ProduktDetail.as_view(), name=views.ProduktDetail.name),
    path('oferty', views.OfertaList.as_view(), name=views.OfertaList.name),
    path('oferty/<int:pk>', views.OfertaDetail.as_view(), name=views.OfertaDetail.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),


    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),


    ]