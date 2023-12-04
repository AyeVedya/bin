# Practical 2:
# Write a
# program to do
# the following:
# a. Enter two distinct faces as vectors u and v.
# b. Find a new face as a linear combination of u and v i.e. au+bv for a and b
# c. Find the average face of the original faces.




def scalMul(x, p):
    return [x[i] * p for i in range(len(x))]

def linCom(vlist, clist):
    s = [scalMul(vlist[i], clist[i]) for i in range(len(vlist))]
    l = []
    for j in range(len(s[0])):
        su = 0
        for i in range(len(s)):
            su = su + s[i][j]
        l.append(su)
    return l

l = int(input("Enter the length of vector: "))
u = []
v = []
c = []

print("Enter the elements of vector u:")
for i in range(l):
    n = int(input("Enter number: "))
    u.append(n)

print("Enter the elements of vector v:")
for i in range(l):
    n = int(input("Enter number: "))
    v.append(n)

print("Enter the coefficients:")
c1 = int(input("Enter the coefficient of c1: "))
c2 = int(input("Enter the coefficient of c2: "))
c.append(c1)
c.append(c2)

newFace = linCom([u, v], [c1, c2])

print("New Face of u and v: ", newFace)

avgFace = [(u[i] + v[i]) / 2 for i in range(len(u))]
print("Average Face of u and v is:", avgFace)
