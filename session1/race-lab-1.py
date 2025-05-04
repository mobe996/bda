# 1) Assuming this list: 10, 20, 30, 40. print all the elements
elements = [10, 20, 30, 40]
for i in elements:
    print(i)

# Time complexity: O(n)/ O(4) more specifically
# Space complexity: -

# 2) Print the first and last elements of your data, separated by a comma
print(f"{elements[0]}, {elements[-1]}")

# Time complexity: O(1)
# Space complexity -

# 3) Count the number of elements in a list. You can not use a built in function

i = 0
for _ in elements:
    i += 1
print(i)

# 4) Create a function called my_len. 
# The function will accept a list and return the length of the list 

def my_len(data) -> int:
    count = 0
    for _ in data:
        count += 1
    return count

# Time: O(n)
# Space: O(1)

data = [-10, 20, -30, 40]
count = 0
for i in data:
    if i > 0:
        count += 1

# Time: O(n)
# Space: -

tot = 0
for i in data:
    if i < 0:
        tot += i
print(tot)

#Time: O(n)

# 7) Swap the first and last element of the list

temp = data[-1]
data[-1] = data[0]
data[0] = temp
print(data)

#Time: O(1)

# 8) Print the indices of the list using a for loop 

index = 0
for _ in data:
    print(index)
    index += 1

#Time: o(n)

# 9) Print the max in the list
maximum = data[0]

for i in data:
    if i > maximum:
        maximum = i
print(maximum)

# Time: O(n)

#Find the second highest number in the list

first = second = float('-inf')

for i in data:
    if i > first:
        second = first
        first = i
    elif i > second:
        second = i

print(second)