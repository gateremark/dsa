#print("Hello World")

## O(n)

def print_items(n):
    for i in range(n):
        print(i)
print_items(10)

#ran n times == O(n)
print("***************")

#simplifying the O notation - Drop Constants

def print_items2(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)
print_items2(20)

#ran n + n times == 2n
# O(2n) == O(n)
print("***************")

## O(n**2)

def print_items3(n):
    for i in range(n):
        for j in range (n):
            print (i, j)
print_items3(10)

# n * n items were printed out == n**2 == O(n**2)

print("***************")

def print_items4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
print_items4(10)

# n * n * n == O(n**3) == O(n**2)

#simplifying the O notation - Drop Non-Dominants

def print_items5(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)
print_items5(10)

#