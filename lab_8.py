#Lab 8
#1. Use the randint function to generate 50 lines of random integers between -20 and 20. Write these
#numbers to a file called random_numbers.txt.
#random_numbers.txt
#-20
#-2
#0
#5
#...
#...
import random

fileh = open("random_numbers.txt","w")

for i in range(1,51):
    number = random.randint(-20,20)
    fileh.write(str(number))
    fileh.write(str(" "))

with open("random_numbers.txt") as fh: 
    lines = fh.readlines()
    for i in lines:
        words = i.split()
        for i in words:
            print("{}\n".format(i))

#2. Now append the file to add in the average of these 50 numbers
#random_numbers.txt
#-20
#-2
#...
#...
#The average of these 50 numbers is 0.28
import random

fileh = open("random_numbers.txt","w")

for i in range(1,50):
    number = random.randint(-20,20)
    fileh.write(str(number))
    fileh.write(str(" "))

with open("random_numbers.txt") as fh:
    numbers = 0
    print("Numbers: {}".format(numbers))
    lines = fh.readlines()
    for i in lines:
        words = i.split()
        for i in words:
            numbers += int(i)
            print("numbers = {}".format(numbers))
            print("{}\n".format(i))
        average = int(numbers) / 50
        print("The Average Of These 50 Numbers is {}".format(average))
#3. Exception
x = float('abc123')
#Output
#Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    x = float('abc123')
#ValueError: could not convert string to float: 'abc123'
#What type of error does it raise? How would improve the error message that comes with the exception?
#   ValueError: could not convert string to float

#4. Remember the Tipper program from lab 2. It asks users for the total bill amount and the program
#calculates the bill. What if the user enters a string? What exception will be raised. Please write a
#type/except handler to handle to exception
#Hint:
#try:
#...
#...
#except <Exception Type>:
#...
#...

greeting = "Hello customer. I hope you enjoyed your meal! It is time to pay now."
meal_total = float(input("How much was the total bill tonight?"))
print(meal_total)
tip_or_nah = input("Would you like to tip your server?")
if tip_or_nah in ["y","Y","yes","YES","YAY","Yeah", "Yee", "YEAH"]:
  try:
    original_tipper = True
    tip_percentage = float(input("What percentage would you like to tip your server tonight?(1% = .01, 100% = 1.0)"))
    tip_amount = (meal_total * tip_percentage)
    formatted_tip_amount = "%.2f" % tip_amount
    print(formatted_tip_amount)
    final_bill_total =  meal_total + tip_amount
    formatted_bill_total = "%.2f" % final_bill_total
    print("After your tip of $" + str(formatted_tip_amount) + ", your total is $" + str(formatted_bill_total))
  except ValueError:
      print("Tip percentage was not input properly: Please Try Again!")
elif tip_or_nah in ["n","N","no","NO","NAW","Naw", "Nope", "NOPE"]:
  tip_percentage = 0
  tip_amount = 0
  print("Seriously? You need to leave a tip! This is NOT optional!")
  while tip_percentage == 0 and tip_amount == 0:
    try:
        original_tipper = False
        tip_percentage = float(input("What percentage would you like to tip your server tonight?(1% = .01, 100% = 1.0)"))
        tip_amount = (meal_total * tip_percentage)
        formatted_tip_amount = "%.2f" % tip_amount
        print(formatted_tip_amount)
        final_bill_total =  meal_total + tip_amount
        formatted_bill_total = "%.2f" % final_bill_total
        print("After your tip of $" + str(formatted_tip_amount) + ", your total is $" + str(formatted_bill_total))
    except ValueError:
        print("Tip percentage was not input properly: Please Try Again!")
if original_tipper == True:
    print("Thank you for tipping your server!")
else:
    print("Thank you for FINALLY tipping your server, cheapo. Your total is $" + str(formatted_bill_total))