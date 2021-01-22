from django.db import models
from django.contrib.auth.models import User

class Klient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=45)
    nazwisko=models.CharField(max_length=45)
    nr_telefonu = models.IntegerField()

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return 'Pan ' + str(self.imie) + ' ' + str(self.nazwisko)


class Pracownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    nr_telefonu = models.IntegerField()

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return 'Pan' + str(self.imie) + ' ' + str(self.nazwisko)


class Zamowienie(models.Model):
    status = models.CharField(max_length=45)
    data = models.DateField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)

    class Meta:
        ordering = ('data',)

    def __str__(self):
        return str(self.status) + ' ' + str(self.data)


class Oferta(models.Model):
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('nazwa',)

    def __str__(self):
        return str(self.nazwa) + ' ' + str(self.cena) + 'zl'


class Produkt(models.Model):
    ilosc = models.IntegerField()
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)

    class Meta:
        ordering = ('zamowienie',)

    def __str__(self):
        return str(self.oferta) + ' ' + str(self.oferta)
