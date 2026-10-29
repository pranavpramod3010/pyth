#move all zero to the end

# numbers = [0,5,0,3,8,0,2,7]

# target_num = 0

# count = numbers.count(target_num)
# for i in range(count):
#     numbers.remove(target_num)
# numbers.append([target_num]*count)    

# print(numbers)



# find the missing number

numbers = [1,2,4,5,6,7,8]

missing_num = 0

for i in range(len(numbers)):
    if i+1 not in numbers:
        missing_num=i+1
        print(missing_num)     



# find duplicate numbers

numbers = [2,5,3,2,8,5,9,3,3]
seen = set()
duplicate =set()

for i in numbers:
    if i in seen:
        duplicate.add(i)      
    else:
        seen.add(i)    
print(duplicate)





# rotate a list 

numbers = [10,20,30,40,50]

print(numbers[-2:]+numbers[:-2])




# find common element from the list

a = [1,2,3,4,5,6]
b = [2,4,6,8,10]
c = [0,2,4,6,12]

A=set(a)   
B=set(b)
C=set(c)

print(A.intersection(B,C))