from rest_framework import serializers
from datetime import date
from .models import *
from django.contrib.auth.models import User


def dlugosc_nr_telefonu(tel):
    if len(tel) != 9:
        raise serializers.ValidationError("Nr telefonu musi być 9 cyfrowy.")
    return tel


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['imie', 'nazwisko', 'email', 'nr_telefonu']

    # imie = serializers.CharField(max_length=45)
    # nazwisko = serializers.CharField(max_length=45)
    # email = serializers.EmailField()
    # nr_telefonu = serializers.IntegerField(validators=[dlugosc_nr_telefonu])

    # def create(self, validated_data):
    #     return KlientSerializer.objects.create(
    #         imie=validated_data['imie'],
    #         nazwisko=validated_data['nazwisko'],
    #         email=validated_data['email'],
    #         nr_telefonu=validated_data['nr_telefonu']
    #     )


class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = ['imie', 'nazwisko', 'pesel', 'email', 'nr_telefonu']

    # imie = serializers.CharField(max_length=45)
    # nazwisko = serializers.CharField(max_length=45)
    # pesel = serializers.IntegerField()
    # email = serializers.EmailField()
    # nr_telefonu = serializers.IntegerField(validators=[dlugosc_nr_telefonu])

    def validate_pesel(self, pesel):
        if len(pesel) != 11:
            raise serializers.ValidationError("PESEL musi być 11 cyfrowy.")
        return pesel


class ZamowienieSerializer(serializers.ModelSerializer):
    # status = serializers.CharField(max_length=45)
    # data = serializers.DateField()
    class Meta:
        model = Zamowienie
        fields = ['status', 'data','klient','pracownik']

    # klient = serializers.ForeignKey(Klient, on_delete=models.CASCADE)
    # pracownik = serializers.ForeignKey(Pracownik, on_delete=models.CASCADE)

    def validate_data(self, d):
        if d > date.today():
            raise serializers.ValidationError("Data zamówieania nie może być w przyszłości.")
        return d


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['nazwa', 'cena']

    # nazwa = serializers.CharField(max_length=45)
    # cena = serializers.DecimalField(max_digits=5, decimal_places=2)

    def validate_cena(self, cena):
        if cena < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return cena


class ProduktSerializer(serializers.ModelSerializer):
    # ilosc = serializers.IntegerField()
    class Meta:
        model = Produkt
        fields = ['ilosc', 'oferta', 'zamowienie']

    # oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    # zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)

    def validate_ilosc(self, ilosc):
        if ilosc < 0:
            raise serializers.ValidationError("Ilosc nie może być ujemna.")
        return ilosc
    #
    # class UserBookSerializer(serializers.HyperlinkedModelSerializer):
    #     class Meta:
    #         model = Produkt
    #         fields = ['url', 'title']
    #
    # class UserSerializer(serializers.HyperlinkedModelSerializer):
    #     books = UserBookSerializer(many=True, read_only=True)
    #
    #     class Meta:
    #         model = User
    #         fields = ['url', 'pk', 'username', 'books']
