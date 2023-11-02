# import pickle
# mycars=["benz","ferrari","BmW"]
# file="mycars.pk"
# f=open(file,"wb")
# pickle.dump(mycars,f)
import pickle
# mycars=["benz","ferrari","BmW"]
file="mycars.pk"
f=open(file,"rb")
print(pickle.load(f))