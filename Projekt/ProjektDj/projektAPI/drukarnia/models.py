from django.db import models
from datetime import datetime

class Klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    nr_telefonu = models.IntegerField()

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return 'Pan(i) ' + str(self.imie) + ' ' + str(self.nazwisko)


class Pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    email = models.EmailField()
    nr_telefonu = models.IntegerField()

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return 'Pan(i) ' + str(self.imie) + ' ' + str(self.nazwisko)


class Zamowienie(models.Model):
    S1 = 'Przyjete'
    S2 = 'Przygotowywane'
    S3 = 'Gotowe do odebrania'
    STATUS_CHOICES = ((S1, 'Przyjete'), (S2, 'Przygotowywane'),(S3, 'Gotowe do odebrania'),)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=S1)
    data = models.DateField(default=datetime.now, blank=True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)




    class Meta:
        ordering = ('data',)

    def __str__(self):
        return str(self.status) + ' ' + str(self.data)


class Oferta(models.Model):
    nazwa = models.CharField(max_length=45, unique=True)
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