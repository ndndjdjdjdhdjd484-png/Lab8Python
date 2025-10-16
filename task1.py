s = input("Введіть рядок:")

numbers = 0

letters = 0

for char in s:

    if char.isdigit():

        numbers += 1

    elif char.isalpha():

        letters += 1


print("цифри:", numbers)
print("літери:", letters)