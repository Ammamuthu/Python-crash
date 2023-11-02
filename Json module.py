# import json
# from typing import DefaultDict
# emp={"name":" Ammamuthu","AGE":21, "matrial status": None}


# f=open("Employee.json","w")
# json.dump(emp,f)
# # f.close()
# import json
# from typing import DefaultDict
# emp={"name":" Ammamuthu","AGE":21, "matrial status": None}
# data=json.dumps(emp)
# print(data)




# "<___LOAD___>"


import json
emp={"name":" Ammamuthu","AGE":21, "matrial status": None}


f=open("Employee.json","r")
data=json.load(f)

f.close()
print(data)