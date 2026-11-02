# find the cube
# list1=[1,2,3]
# cube=[]
# for i in list1:
#     cube.append(i**3)
# print(cube)    


# count the num of element in the list

# numbers=[10,20,30,40,50,20]
# for i in range(len(numbers)):
#     numbers.count(i)
# print(i)   



# find the common element
# a={1,2,3,6}
# b={6,8,9}

# print(a.intersection(b))




# find the element present in one list but not in another list

a=[10,20,30,40,50]
b=[30,40,60,70]
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)    



# find even and odd numbers
numbers=[12,7,20,9,33,44,18,5]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)   
print(even)         
print(odd)        




# find the largest end smallest element

numbers=[12,56,90,34,78.23]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest)    
print(smallest)        