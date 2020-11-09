import file_manager


# 1
def lists(a_list, b_list):
    c_list = []
    longer_list_len = len(a_list)
    if longer_list_len <= len(b_list):
        longer_list_len = len(b_list)

    for i in range(longer_list_len):
        if i < len(a_list) and i % 2 == 0:
            c_list.append(a_list[i])
        if i < len(b_list) and i % 2 != 0:
            c_list.append(b_list[i])
    print(c_list)


# 2
def info(data_text):
    info_text = {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }
    return info_text


# 3
def delete(text, letter):
    deleted = [x for x in text if x != letter]
    return deleted


# 4
def convert(temperature_type, degrees):
    if temperature_type == "K":
        kelvin = degrees + 273.15
        return kelvin
    if temperature_type == "F":
        fahrenheit = (9 / 5) * degrees + 32
        return fahrenheit
    if temperature_type == "R":
        rankine = (degrees + 273.15) * (9 / 5)
        return rankine
    return print("Wrong temperature type (must be K, F or R)")


# 5
class Calculator:
    def add(self, x, y):
        return x + y

    def diffeence(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


# 6
class ScienceCalculator(Calculator):
    def power(self, x, y):
        return x ** y

    def square(self, x, y):
        return x ** (1 / y)


# 7
def reverse(text):
    print(text[::-1])


# 1
list1 = [11, 12, 13, 14, 15, 16, 17, 18]
list2 = [1, 2, 3, 4, 5, 6, 7]
lists(list1, list2)

# 2
print(info("WIELKIE niewielkie"))

# 3
print(delete("Ala ma kota", "a"))

# 4
print(convert("K", 33))
print(convert("F", 43))
print(convert("R", 43))

# 5
calc1 = Calculator()
print(calc1.add(3, 4))

# 6
calc2 = ScienceCalculator()
print(calc2.square(4, 2))

# 7
reverse("to kajak")

# 8
manager1 = file_manager.FileManager("zad8.txt")
manager1.read_file()
manager1.update_file("\nAdded text")
manager1.read_file()