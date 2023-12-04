# Practical 3:
# Write a
# program to do
# the following:
# a. Enter a vector u as a n-list
# b. Enter another vector v as a n-list
# c. Find the vector au+bv for different values of a and b
# d. Find the dot product of u and v




def scalarMul(x, p, y, q):
    return sum([(x[i] * p) + (y[i] * q) for i in range(len(x))])

def dotMul(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])

v = []
u = []

n = int(input("Enter the number of elements you want to enter in the vector: "))
print("Enter Elements of vector u: ")
for i in range(n):
    e = int(input("Enter element: "))
    u.append(e)

print("Vector u =", u)

print("Enter Elements of vector v: ")
for i in range(n):
    e = int(input("Enter element: "))
    v.append(e)

print("Vector v =", v)

while True:
    print("Select Vector Operation:")
    print("1: Scalar Multiplication")
    print("2: Dot Product")
    print("3: Exit")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        print("To perform Scalar Multiplication")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        print("Scalar Multiplication =", scalarMul(u, a, v, b))
    
    elif ch == 2:
        print("Dot Product of two vectors is:", dotMul(u, v))
    
    elif ch == 3:
        print("Program Terminated Successfully")
        break
