monthConvert = {
    "Jan": "January",
    "Feb": "Fenruary",
    "Mar": "March",
    "Apr": "April"
}

print(monthConvert.get("sdf", "Not found in the dictionary"))

# while loop

i = 1

while i < 10:
    print(i)
    i += 1

# for loop

for letter in "Avocado":
    print(letter)

fruits = ["Avocado", "Grapes", "Guava"]

for i in fruits:
    print(i)

for index in range(3, 10):
    print(index)

for  index in range(len(fruits)):
    print(fruits[index])

# exponent function

print(4**3)

def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = result * base_num
    return result

print(raise_to_power(4, 3))

#  making a translation program

def translate(str):
    translated = ""
    for letter in str:
        if letter in "AEIOUaeiou":
            translated = translated + "g"
        else:
            translated = translated + letter
    return translated

print(translate("Avocado"))

# print(translate(input("Enter something: ")))

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Value Error Handled")
except ZeroDivisionError as err:
    print("Zero division error handled")
    print(err)



