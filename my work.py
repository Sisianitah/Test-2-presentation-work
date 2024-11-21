# PYTHON DISCUSSION QUESTIONS

# Loops
# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.

#SOLN

for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
#SOLN
number = 0
while number <= 10:
    number = int(input("Enter a number greater than 10: "))
print("Thank you!")


# Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

#SOLN
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)



# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print 
# the result.

#SOLN

numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        odd_sum += num
print("Sum of odd numbers:", odd_sum)
# Lists
# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
#SOLN
fruits = ["apple", "pineapple", "cherry", "orange", "watermelon"]

for fruit in fruits:

    print(fruit)

# Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] 
# should become [1, 4, 9].
#SOLN

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

print(square_numbers([1, 2, 3]))

# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, 
# combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []

for i in range(len(list1)):
    combined.append(list1[i])
    combined.append(list2[i])

print(combined)
# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without 
# using the max() function.

numbers = [3, 1, 4, 1, 5, 9, 2]
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest, largest = largest, num
    elif num > second_largest and num != largest:
        second_largest = num

print("Two largest numbers:", largest, second_largest)
# Dictionaries
# Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value
#  pair on a new line.

#SOLN

dict = {'name'  : 'Nabwire Edith',
        'age'   :  120,
        'grade' :  'A'
}
for key,value in dict.items():

    print(key,value)

# Intermediate: Write a function that takes a dictionary of people's names and their ages, 
# {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.

#SOLN
def people_detials():
    dict ={'Alice': 24, 'Bob': 19, 'Charlie': 30}
    dict.pop('Bob')  #POP  used to remove an item in dictionary and 
                     #update used to add or replace an item in dictionary
    print(dict)




# Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, 
# write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.

#SOLN
store = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = sum(store[item] for item in items_bought)
print("Total cost:", total_cost)

# Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello,"
#  the output should be {'hello': 2, 'world': 1}.
#SOLN
sentence = "hello world hello"
word_counts = {}

for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

# Object-Oriented Programming (OOP)
# Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

#SOLN
class Car:
    def __init__(self, brand, color):
         self.brand = brand
         self.color = color
C1 = Car('Hillux', 'Red') 

print(C1.brand)
print(C1.color)
    


# Intermediate: Add a method called start_engine to the Car class that prints a message
#  saying the engine of the car has started. 
# Create an instance of Car and call the method.

#SOLN

class car:
    def __init__(self, brand , color, start_engine):
         self.brand = brand
         self.color = color
         self.start_engine = start_engine
    def my_car(pro):
        print(f'The engine of my ' + pro.brand ,' car which is ' + pro.color , 'in color has started')
        print(f'The engine of my ' + pro.brand , 'car which is ' + pro.color , 'in color with its ' + pro.start_engine , 'engine has started')
p1 = car('Hillux', 'Red' , 'Drox' ) # identified attributes.
p1.my_car()     


# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

# SOLN

class BankAccount:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount >0:
            self.balance += amount
            print(f'You have deposited {amount}and the new balance is {self.balance}')
        else:
            print(f'Invailed input,please deposite money')

    def withdraw(self, amount):
        if amount >0 and self.balance>=amount:
            self.balance-=amount
            print(f'You have withdrawn and the new balance is {self.balance}')
            
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account number is {self.account_number } and Account balance is : {self.balance}")

account = BankAccount(account_number="1234545UG",balance=8000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
   
# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed). 
# #SOLN     
class Library:
    def init(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author, 'available': True})

    def remove_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]

    def is_available(self, title):
        for book in self.books:
            if book['title'] == title:
                return book['available']
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title and book['available']:
                book['available'] = False
                return f"You've borrowed {title}."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.books:
            if book['title'] == title:
                book['available'] = True
                return f"You've returned {title}."
        return f"{title} not found in the library."

library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
print(library.borrow_book("1984"))
print(library.is_available("1984"))
library.return_book("1984")