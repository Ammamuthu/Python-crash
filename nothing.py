import pandas as py
cars={"name":["aaaa","ss","ssss","rd"],
"age" : [2222,222,2333,33],
"valu":["yes","no","noo","no"]}
a=py.DataFrame(cars)
# print(a)


print(type(a))


print(a[["name","age"]])

print(a.iloc[1])
print(["valu"].value_counts())