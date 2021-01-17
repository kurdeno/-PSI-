from django.db import models


class Klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    email = models.EmailField()
    nr_telefonu = models.IntegerField()

    def __str__(self):
        return 'Pan ' + str(self.imie) + ' ' + str(self.nazwisko)

class Pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    email = models.EmailField()
    nr_telefonu = models.IntegerField()

    def __str__(self):
        return 'Pan' + str(self.imie) + ' ' + str(self.nazwisko)

class Zamowienie(models.Model):
    status = models.CharField(max_length=45)
    data = models.DateField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status) + ' ' + str(self.data)

class Oferta(models.Model):
    nazwa = models.CharField(max_length=45)
    cena = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.nazwa) + ' ' + str(self.cena) + 'zl'

class Produkt(models.Model):
    ilosc = models.IntegerField()
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ilosc) + ' ' + str(self.oferta) + ' ' + str(self.zamowienie)
