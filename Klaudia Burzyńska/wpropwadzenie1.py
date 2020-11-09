# 1
lipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
         "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
         "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
         "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem " \
         "Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji " \
         "druków na komputerach osobistych, jak Aldus PageMaker"
# 2
imie = "Klaudia"
nazwisko = "Burzynska"
print("W tekście jest {} liter {} oraz {} liter {}.".format(str.count(lipsum, imie[2]), imie[2], str.count(lipsum,
                                                                                                           nazwisko[3]),
                                                            nazwisko[3]))
# 3
print("Lorem {:>20}".format("ipsum"))
print('{:.10}'.format("Konstantynopolitańczykowianeczka)"))
print('{:{align}{width}}'.format('test', align='>', width='60'))
print('{:{prec}} = {:{prec}}'.format('Kurczak', 142.7182, prec='.4'))
print('{:{}{}{}.{}}'.format(3.141592653589, '>', '+', 50, 6))
# 4
zmienna = "Excepteur sint occaecat cupidatat non proident"
print(dir(zmienna))
help(zmienna.find("sint"))
# 5
print(imie[::-1], nazwisko[::-1])
# 6
lista = list(range(1, 11))
print(lista)
lista1 = lista[:len(lista) // 2]
lista2 = lista[len(lista) // 2:]
print(lista1, lista2)
# 7
lista3 = [0] + lista1 + lista2
print(lista3[::-1])
# 8
studenciaki = [(666111, "Arnold Krach"), (434343, "Helga VanKok")]
# 9
dane = dict(studenciaki)
print(dane)
dane[666111] = [dane.get(666111), 23, "elplanto@egmail.com", 1997, "Dorito 33, Texas"]
dane[434343] = [dane.get(434343), 123, "renesans@egmail.com", 1897, "Długa 5, Kraśnik"]
print(dane)
# 10
numery = [222444555, 844841211, 844841211, 999040404, 844841211, 222444555]
numery_bez_powtorzen = set(numery)
print("Lista z powtórzeniami: ", numery, "\nBez powtórzeń: ", numery_bez_powtorzen)
# 11
for x in range(1, 11):
    print(x)
# 12
for x in range(100, 19, -5):
    print(x)
# 13
mega_lista = [dict(Audi=1997, BMW=2000, Honda=2018), dict(student1=565743, student2=482573)]
for x in range(len(mega_lista)):
    print(mega_lista[x])
