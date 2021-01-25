from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework.reverse import reverse
from . import views
from .models import Oferta, Klient
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User


class OfertaTest(APITestCase):
    def post_oferta(self, name, price):
        url = reverse(views.OfertaList.name)
        data = {'nazwa': name, 'cena': price}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_oferta(self):
        new_oferta_name = 'A1'
        new_oferta_cena = 0.3
        response = self.post_oferta(new_oferta_name, new_oferta_cena)
        print("PK {0}".format(Oferta.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Oferta.objects.count() == 1
        assert Oferta.objects.get().nazwa == new_oferta_name

    def test_post_existing_oferta_name(self):
        url = reverse(views.OfertaList.name)
        new_oferta_name = 'A3'
        new_oferta_cena = 0.1
        data = {'nazwa': new_oferta_name, 'cena': new_oferta_cena}
        response_one = self.post_oferta(new_oferta_name, new_oferta_cena)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_oferta(new_oferta_name, new_oferta_cena)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_oferta_by_name(self):
        oferta_name_one = 'B4'
        oferta_name_two = 'A4'
        oferta_price_one = 1
        oferta_price_two = 2
        self.post_oferta(oferta_name_one, oferta_price_one)
        self.post_oferta(oferta_name_two, oferta_price_two)
        filter_by_name = {'nazwa_oferty': oferta_name_one, 'max_cena': 1.5, 'min_cena': .5}
        url = '{0}?{1}'.format(reverse(views.OfertaList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwa'] == oferta_name_one

    def test_get_oferta_collection(self):
        new_oferta_name = 'A5'
        new_oferta_cena = 0.33
        self.post_oferta(new_oferta_name, new_oferta_cena)
        url = reverse(views.OfertaList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwa'] == new_oferta_name

    def test_update_oferta(self):
        oferta_name = 'A5'
        oferta_cena = 0.33
        response = self.post_oferta(oferta_name, oferta_cena)
        url = urls.reverse(views.OfertaDetail.name, None, {response.data['pk']})
        updated_oferta_name = 'B4'
        updated_oferta_cena = 0.4
        data = {'nazwa': updated_oferta_name, 'cena': updated_oferta_cena}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['nazwa'] == updated_oferta_name

    def test_oferta(self):
        oferta_name = 'A5'
        oferta_cena = 0.33
        response = self.post_oferta(oferta_name, oferta_cena)
        url = urls.reverse(views.OfertaDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['nazwa'] == oferta_name


class KlientTest(APITestCase, TestCase):

    def post_klient(self, imie, nazwisko, email, nr_tel):
        url = reverse(views.KlientList.name)
        data = {'imie': imie, 'nazwisko': nazwisko, 'email': email, 'nr_telefonu': nr_tel}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_klient(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        response = self.post_klient(fname, lname, eml, tel)

        print("PK {0}".format(Klient.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 1
        assert Klient.objects.get().imie == 'adam'

    def test_post_existing_klient_name(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        response_one = self.post_klient(fname, lname, eml, tel)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_klient(fname, lname, eml, tel)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_klient_by_name(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        fname2 = 'kun'
        lname2 = 'dasf'
        eml2 = '32@dad.pl'
        tel2 = 134421511
        self.post_klient(fname, lname, eml, tel)
        self.post_klient(fname2, lname2, eml2, tel2)
        filter_by_name = {'imie': fname}
        url = '{0}?{1}'.format(reverse(views.KlientList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['imie'] == fname

    def test_get_oferta_collection(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        self.post_klient(fname, lname, eml, tel)
        url = reverse(views.KlientList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['imie'] == fname

    def test_update_oferta(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        response = self.post_klient(fname, lname, eml, tel)
        url = urls.reverse(views.KlientDetail.name, None, {response.data['pk']})
        fnameU = 'Kuba'
        lnameU = 'Mroz'
        emlU = '32@dad.pl'
        telU = 134141543
        data = {'imie': fnameU, 'nazwisko': lnameU, 'email': emlU, 'nr_telefonu': telU}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['imie'] == fnameU

    def test_oferta(self):
        fname = 'adam'
        lname = 'dad'
        eml = '3@dad.pl'
        tel = 134141511
        response = self.post_klient(fname, lname, eml, tel)
        url = urls.reverse(views.KlientDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['imie'] == fname
