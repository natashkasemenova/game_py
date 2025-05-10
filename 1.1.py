
import pickle

file = open('lear.pickle', 'rb')

str = pickle.load(file)
result = str[5877:5883]
print(result)

length = len(str)

# Виводимо результат
print(f"Рядок містить {length} символів")

file.close()

print ([1, 2] + [3, 4])

a = [1, 2, 3, 4]

a[2] = 2 #[1, 2, 2, 4]*

a.pop() #[1, 2, 2]*

a *= 2 #[1, 2, 2, 1, 2, 2]*

print (a)

b = [True, [1, 0, ["True", ["Hello", "World"], "F"]], False]
del b[1 ][ 2][ 2]
print (b)

c =[3, 1, 9, 4, 4, 3, 1, 7, 5, 2]
print(c.pop(4))

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]  

print(A[-1::-2])