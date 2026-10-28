# find largest number
numbers = [12,45,7,89,23]

largest = numbers[0]

for i in numbers:
    if i >largest:
        largest=i
print(largest)



# reverse a list 

numbers = [1,2,3,4,5]
reverse_list = []

print(numbers[::-1])  



# remove element

numbers = [1,2,2,3,4,3,5]
new = []

for i in numbers:
    if i not in new:
        new.append(i)
print(new)    



# find common element

a = [1,2,3,4,5]
b = [3,4,5,6,7]

for i in a:
    for j in b:
        if i==j:
         print(i)            


