from django.contrib import admin

# Register your models here.
from .models import Klient, Pracownik, Zamowienie, Oferta, Produkt

admin.site.register(Klient)
admin.site.register(Pracownik)
admin.site.register(Zamowienie)
admin.site.register(Oferta)
admin.site.register(Produkt)
