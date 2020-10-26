zm = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
     " Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki    ." \
     " Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym    ." \
     " Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty    " \
     " Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym" \
     " do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Krzysztof"
nazwisko = "Bodo"
print("W tekście jest " + str(zm.count(imie[2])) + " liter " + imie[2] + " oraz " + str(zm.count(nazwisko[3]))
      + " liter " + nazwisko[3])
print("W tekście jest {} liter {}  oraz {} liter {}".format(str(zm.count(imie[2])), imie[2], str(zm.count(nazwisko[3])),
                                                            nazwisko[3]))
print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))
print('{:{align}{width}}'.format('test', align='^', width='10'))
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))
print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))
print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))

zmienna_typu_string = "Ala ma kota"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.swapcase())

print(imie.lower()[::-1].capitalize() + " " + nazwisko.lower()[::-1].capitalize())

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowalista = lista[5:]
lista = lista[:5]
print(nowalista)
print(lista)
lista = [0] + lista + nowalista
print(lista)

studenci = [(12345, "Damian Glomb"), (12552, "Jan Kowalski"), (15252, "Tomasz Fart")]
print(studenci)

studenci3 = dict(studenci)
print(studenci3)
for x in studenci3:
    studenci3[x] = [studenci3.get(x), 20, "jk@dupa.pl", 1999, "Głowna 2"]

print(studenci3)
nrTelefonu = ["123456789", "333444555", "123654789", "123456789"]
nrTelefonu2 = list(set(nrTelefonu))
print(nrTelefonu2)

for x in range(1, 11):
    print(x)

for x in range(100, 19, -5):
    print(x)
l = [dict(jeden=1, dwa=2, trzy=3), dict(fretka="małe", pies="duże", kot="grube")]
print(l)
wynik = str(l)
print(wynik)