# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

# ls=[i for i in range(100) if i%3==0]
# print(ls)
# dict1={i:f"item[{i}]" for i in range(100)}
# print(dict1)

# dict1={}
# for i in range(100):
#     print(f"item: {i}")
# print(dict1)

even=(i for i in range (100) if i%2==0)
print(even.__next__())
print(even.__next__())
print(even.__next__())


