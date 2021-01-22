from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from .models import Klient, Pracownik, Zamowienie, Oferta, Produkt
from .serializers import KlientSerializer, PracownikSerializer, ZamowienieSerializer, OfertaSerializer, \
    ProduktSerializer  # , UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klienci'
    ordering_fields = ['nazwisko']
    filterset_fields = [Klient.user.email, 'imie', 'nazwisko']
    search_fields = ['nazwisko']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownicy'
    ordering_fields = ['nazwisko']
    filterset_fields = ['imie', 'nazwisko', 'pesel', 'email', 'nr_telefonu']
    search_fields = ['nazwisko']


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-detail'


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienia'
    ordering_fields = ['data']
    filterset_fields = ['status', 'data', 'klient', 'pracownik']
    search_fields = ['status']


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'pracownik-detail'


class ProduktList(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkty'
    ordering_fields = ['zamowienie', 'ilosc', 'oferta']
    filterset_fields = ['ilosc', 'oferta', 'zamowienie']
    search_fields = ['ilosc']


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkt-detail'


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
        fields = ['min_price', 'max_price', 'nazwa_oferty']


class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    name = 'oferty'
    ordering_fields = ['nazwa', 'cena']
    filterset_fields = ['nazwa', 'cena']
    search_fields = ['nazwa']
    filter_class = OfertaFilter


# class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Oferta.objects.all()
#     serializer_class = OfertaSerializer
#     name = 'oferta-detail'


# class OfertaFilter(FilterSet):
#     min_price = NumberFilter(field_name='cena', lookup_expr='gte')
#     max_price = NumberFilter(field_name='cena', lookup_expr='lte')
#     nazwa_oferty = AllValuesFilter(field_name='oferta__nazwa')
#
#     class Meta:
#         model = Oferta
#         fields = ['min_price', 'max_price', 'nazwa_oferty']
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     name = 'user-list'
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'oferty': reverse(OfertaList.name, request=request),
                         'produkty': reverse(ProduktList.name, request=request),
                         'zamowienia': reverse(ZamowienieList.name, request=request),
                         'klienci': reverse(KlientList.name, request=request),
                         'pracownicy': reverse(PracownikList.name, request=request)
                         })
