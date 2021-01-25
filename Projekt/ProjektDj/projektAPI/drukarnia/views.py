from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from django_filters import AllValuesFilter, NumberFilter, FilterSet
from .models import Klient, Pracownik, Zamowienie, Oferta, Produkt
from .serializers import KlientSerializer, PracownikSerializer, ZamowienieSerializer, OfertaSerializer, \
    ProduktSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from django.http import HttpResponse


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klienci'
    ordering_fields = ['nazwisko']
    filterset_fields = ['imie', 'nazwisko', 'email', 'nr_telefonu']
    search_fields = ['nazwisko']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class PracownikList(generics.ListCreateAPIView):
    login_url = 'api-auth/login/'
    redirect_field_name = 'redirect_to'
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownicy'
    ordering_fields = ['nazwisko']
    filterset_fields = ['imie', 'nazwisko', 'pesel', 'email', 'nr_telefonu']
    search_fields = ['nazwisko']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PracownikDetail(generics.RetrieveAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienia'
    ordering_fields = ['data']
    filterset_fields = ['status', 'data', 'klient', 'pracownik']
    search_fields = ['status']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProduktList(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkty'
    ordering_fields = ['zamowienie', 'ilosc', 'oferta']
    filterset_fields = ['ilosc', 'oferta', 'zamowienie']
    search_fields = ['ilosc']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkt-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    name = 'oferta-detail'


class OfertaFilter(FilterSet):
    min_price = NumberFilter(field_name='cena', lookup_expr='gte')
    max_price = NumberFilter(field_name='cena', lookup_expr='lte')
    nazwa_oferty = AllValuesFilter(field_name='nazwa')

    class Meta:
        model = Oferta
        fields = ['nazwa_oferty', 'min_price', 'max_price']


class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    name = 'oferty'
    filterset_class = OfertaFilter
    ordering_fields = ['nazwa', 'cena']

    search_fields = ['nazwa']


class UserList(LoginRequiredMixin, generics.ListAPIView):
    login_url = 'api-auth/login/'
    redirect_field_name = 'redirect_to'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.IsAdminUser]


class UserDetail(LoginRequiredMixin, generics.RetrieveAPIView):
    login_url = 'api-auth/login/'
    redirect_field_name = 'redirect_to'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAdminUser]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'oferty': reverse(OfertaList.name, request=request),
                         'produkty': reverse(ProduktList.name, request=request),
                         'zamowienia': reverse(ZamowienieList.name, request=request),
                         'klienci': reverse(KlientList.name, request=request),
                         'pracownicy': reverse(PracownikList.name, request=request),
                         'uzytkownicy': reverse(UserList.name, request=request)
                         })
