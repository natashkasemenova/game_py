number = int(input("Input the number: "))
print("The number is even!", number % 2 == 0) #even number - true*

a = 2
b = 8
print(number > a and number < b) #IN the interval*
#if so - true, else - false*
print(number < a or number > b) #OUTSIDE the interval*
#if so - true, else - false*

print(bool([1, 2, 3])) #true*
print(bool([])) #false - empty list*