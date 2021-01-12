from django.db import models


class Klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.EmailField()
    nr_telefonu = models.IntegerField()


class Pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.IntegerField()
    email = models.EmailField()
    nr_telefonu = models.IntegerField()


class Zamowienie(models.Model):
    status = models.CharField(max_length=45)
    data = models.DateField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)


class Oferta(models.Model):
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=5, decimal_places=2)


class Produkt(models.Model):
    ilosc = models.IntegerField()
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
