# number = int(input("Enter an integer:"))
# if number <= 100:
#     print("Your number is less than or equal to 100")
# else:
#     print("Your number is greater than 100")


# amount = float(input("Enter amount:"))
# inrate = float(input("Enter Interest rate:"))
# period = int(input("Enter period:"))
# value = 0
# year = 1
# while year <= period:
#     value = amount + (inrate * amount)
#     print("Year {} Rs. {:.2f}".format(year, value))
#     amount = value
#     year += 1


# N = 10
# sum = 0
# count = 0
# print("please input 10 numbers:")
# while count < N:
#     number = float(input())
#     sum += number
#     count += 1
# average = sum / N
# print("N = {},sum = {}".format(N,sum))
# print("Average = {:.2f}".format(average))


# fahrenheit = 0
# print("Fahrenheit Celsius")
# while fahrenheit <= 250:
#     celsius = (fahrenheit - 32) / 1.8
#     print("{:5d} {:7.2f}".format(fahrenheit , celsius))
#     fahrenheit += 25


# a, b = 45, 54


# data = ("shiyanlou", "China", "Python")
# name, country ,language = data
# print(name, country, language)


basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number of input sold:"))
price = float(input("Enter the price of camera:"))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("Bonus = {:6.2f}".format(bonus))
print("Commission = {:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bonus +commission))