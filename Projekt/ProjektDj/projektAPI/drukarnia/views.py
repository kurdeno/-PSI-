from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Klient, Pracownik, Zamowienie, Oferta, Produkt
from .serializers import KlientSerializer, PracownikSerializer, ZamowienieSerializer, OfertaSerializer, \
    ProduktSerializer

from django.http import HttpResponse


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klienci'
    ordering_fields = ['imie', 'nazwisko']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownicy'
    ordering_fields = ['imie', 'nazwisko']


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-detail'


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienia'


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'pracownik-detail'


class ProduktList(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkty'


class ProduktDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkt-detail'


class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    name = 'oferty'


class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    name = 'oferta-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'oferty': reverse(OfertaList.name, request=request),
                         'produkty': reverse(ProduktList.name, request=request),
                         'zamowienia': reverse(ZamowienieList.name, request=request),
                         'klienci': reverse(KlientList.name, request=request),
                         'pracownicy': reverse(PracownikList.name, request=request)
                         })
