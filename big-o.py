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
print("***************")

#simplifying the O notation - Drop Non-Dominants

def print_items5(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)
print_items5(10)

# ran O(n**2 + n) == O(n**2)
print("***************")

## O(1) - Most efficient Big(O)
def add_items(n):
    return n+n
add_items()

def add_items2(n):
    return n+n+n+n
add_items2()

#As the number of n increases, the number of operation remains constant
print("***************")

## O(log n)
"""
eg. Having a list [1, 2, 3, 4, 5, 6, 7, 8] (sorted data),
Look for number 3


Cut the list into halves removing the half that 1 is
not present...
1. [1, 2, 3, 4] [5, 6, 7, 8] - We eliminate the second half
2. [1, 2] [3, 4] - We eliminate the first half
3. [3] [4] - We eliminate the second half and we are left with 3

How many steps (operations) did we go? - 3 steps (operations)
How many items are in the list? - 8 items

2**3 == 8 (Turning it into a logarithm) -- log2 8 = 3

log2 1073741824 == 31 
"""
print("***************")

## O(nlog n) --- Used in some sorting algorithms
def print_items2(a, b):
    for i in range(a):
        print(a)

    for j in range(b):
        print(b)
# O(a) + O(b) == O(a + b)

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)
# O(a) * O(b) == O(a * b)

print("***************")

## Big(O) of lists

# O(1) - Adding or removing items on the last index
# O(1) also occurs when you're looking for an item in a list using index
# eg. my_list[3]
"""
This is because the items originally in the 
list are not re-indexed
"""
my_list = [11, 3, 23, 7]
my_list.append(17)
# [11, 3, 23, 7, 17]
my_list.pop()
# [11, 3, 23, 7]

# O(n) - Adding or removing items on the first or middle index of the list
# O(n) also occurs when you're looping over a list to find an item
"""
This is because after adding an item, the items
in the list has to be re-indexed
"""
my_list = [11, 3, 23, 7]
my_list.pop(0)
#[3, 23, 7]
my_list.insert(0, 11)
#[11, 3, 23, 7]
my_list.insert(1, "Hi")
#[11, 'Hi', 3, 23, 7]
my_list.pop(1)
#[11, 3, 23, 7]

'''
O(n**2) -- Loop within a loop
O(nlog n) -- When one has different parameters in the function and wanna perform an operation on them.
O(n) -- Proportional
O(log n) -- Divide and conquer
O(1) - Constant
'''