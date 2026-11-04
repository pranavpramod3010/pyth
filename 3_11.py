# group students according to their marks
# students={
#     "anu":85,
#     "rahul":76,
#     "meera":89,
#     "arun":45,
#     "john":35,
#     "sara":75
# }

# result={
#     "ecxellent":[],
#     "average":[],
#     "bad":[]
# }
# for name, marks in students.items():
#     if marks>=80:
#         result["ecxellent"].append(name)
#     elif marks>=50:
#         result["average"].append(name)
#     else:
#         result["bad"].append(name)
# print(result)





# reverse every word in a list
# word=["python","java","developer","coding"]

# result=[]
# for i in word:
#     result.append(i[::-1])
# print(result)





# find elements that appears exactly once
# numbers=[1,2,3,2,4,5,1,6,5,7]

# frequency={}
# for i in numbers:
#       if i in frequency:
#         frequency[i]+=1
#       else:
#         frequency=1
# result=[]
# for i in numbers:
#       if frequency[i]==1:
#         result.append(i)
#       print(result)