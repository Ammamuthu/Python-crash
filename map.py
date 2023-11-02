# def multi(a):
#     return a*a
# lst=[1,2,3,4,5,6,7]
# for i in lst:
#     print(i)
# lst=list(map(multi,lst))
# for i in lst:
#     print(i)
def multi(a):
    return a*a
num=[1,2,3,4,5]
z="and".join(num)
for i in num:
    #print(i)
    num=list(map(multi,num))
for j in num:
    #print(j)
    for k in len(num):
        print(num[i],num[j])