# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on lines 4-5. Your program should work for different inputs. e.g. any two-digit number.

two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# print(type(first_digit))

result = (first_digit) + (second_digit)
# print(type(result))
print(result)
