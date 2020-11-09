from file_manager import FileManager

# 1. Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list.
#    Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.

def f1(a_lista, b_lista):
    x = [a_lista[i] for i in range(0, len(a_lista)) if i % 2 == 0]
    x += [b_lista[i] for i in range(0, len(b_lista)) if i % 2 == 1]
    return x


print(f1([1, 2, 3, 4], [5, 6, 7, 8, 9]))


# 2. Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące
#    informacje o parametrze w formie słownika (dict)

def f2(data_txt):
    duze = 0
    male = 0
    for i in data_txt:
        if i.isupper():
            duze += 1
        if i.islower():
            male += 1
    x = {
        'length': len(data_txt),
        'letters': len(data_txt) - data_txt.count(" "),
        'big_letters': duze,
        'small_letters': male
    }
    return x


print(f2("Ala ma Dużego Kota"))


# 3. twórz funkcję, która przyjmie jako parametry text oraz letter, a następnie zwróci wynik usunięcia wszytkich
#    wystąpień wartości w letter z tekstu text.

def f3(text, letter):
    return text.replace(letter, "")


print(f3("ala ma kota", "a"))


# 4. Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
#    Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.

def f4(temp, temperature_type):
    if temp < -273.15:
        print("NIe ma tak niskich temperatur")
    if temperature_type == "F":
        return (temp * 9 / 5) + 32
    elif temperature_type == "R":
        return (temp * 273.15) * (9 / 5)
    elif temperature_type == "K":
        return temp + 273.15
    else:
        print("Nie poprawny typ")
        return temp


print(f4(-400, "F"))
print(f4(333, "F"))
print(f4(333, "K"))
print(f4(333, "R"))
print(f4(333, "c"))


# 5. Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.

class Calculator:
    def add(self, a, b):
        return a + b

    def diffrence(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


k1 = Calculator()
print(k1.add(3, 2))
print(k1.diffrence(3, 2))
print(k1.multiply(3, 2))
print(k1.divide(3, 2))


# 6. Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.

class ScienceCalculator(Calculator):
    def power(self, a, b):
        return a ** b

    def remain(self, a, b):
        return a % b


k2 = ScienceCalculator()
print(k2.power(3, 5))
print(k2.remain(3, 5))


# 7. Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.

def reverse(text):
    return text[::-1]


print(reverse("Ala ma kota"))

# 9. Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.

fm = FileManager("plik.txt")
fm.read_file()